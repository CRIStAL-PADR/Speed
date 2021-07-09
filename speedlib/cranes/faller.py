# -*-coding: <Utf-8> -*-
""" Comments for all the librairy """
import queue
import threading
import re
import time
import requests
from pint import UnitRegistry

TIME_OUT = 3
ureg = UnitRegistry()
MOTOR_SPREADER = 2
MOTOR_CRAB = 1
MOTOR_CHASSIS = 3
MOTOR_DIRECTION_BACKWARD = -1
MOTOR_DIRECTION_FORWARD  = 1




class Crane():
    def __init__(self):
        self.slave_ip = None
        self.master_ip = None
        self.dict_q = {}
        for i in range(1,4):
            self.dict_q[i] = queue.Queue()
            threading.Thread(target = self.run_start_for, daemon = True, args=(i,)).start()


    def run_start_for(self, id_moteur):
        while True:
            if id_moteur in self.dict_q.keys() :
                arguments = self.dict_q[id_moteur].get()
                init_time = time.time()*ureg.second
                print("start")
                while time.time()*ureg.second - init_time < arguments[0]:
                    self.start(arguments[1], arguments[2])
                print("stop")
                self.stop(arguments[1])
                self.dict_q[id_moteur].task_done()
            else:
                raise RuntimeError("motor_id Error")



    def get_motor_info_from_number(self, snr):
        """
        It takes the crane as input and returns the  number of the motor with its IP address.
        :param : see def start (sNr, turn) parameters
        """
        if not isinstance(snr, int):
            raise TypeError(" The value of n must be an integer but got " +str(snr))



        if MOTOR_SPREADER == snr:
            return (self.slave_ip, 2)
        if MOTOR_CRAB == snr:
            return (self.slave_ip, 1)
        if MOTOR_CHASSIS  == snr:
            return (self.master_ip, 1)
        raise RuntimeError("""Invalid motor number, must be MOTOR_SPREADER, MOTOR_CRAB or
                               MOTOR_CHASSIS , got """+str(snr))


    def start (self, snr, turn):
        """
        :param sNr: This is the first of the arguments. It indicates the engine number that we would
        like to start.
        It takes the values ​​1 2 3 which indicates motors 1 2 and 3 respectively
        :param turn: It indicates the direction in which we would like to run the engine.
         1 for moving forward and -1 for moving backward
        """
        if turn not in [MOTOR_DIRECTION_FORWARD , MOTOR_DIRECTION_BACKWARD ]:
            raise RuntimeError("""Invalid parameter, turn must be either MOTOR_DIRECTION_FORWARD  or
                                  MOTOR_DIRECTION_BACKWARD . Got """ +str(turn))

        i_p, num_motor = self.get_motor_info_from_number(snr)
        request_answer = requests.get("http://"+i_p+"/startM?sNr="+str(num_motor)+
                                      "&turn="+str(turn), timeout=TIME_OUT)

        if request_answer.status_code !=200:
            raise RuntimeError("Unable to control the motor, "+str(request_answer.status_code))

        if request_answer.text != "ok":
            raise RuntimeError("""Able to controle the motor but got not OK
                                   answer: """+request_answer.text)
        return request_answer.text

    def stop(self, snr):
        """
        :param sNr: This is the first of the arguments. It indicates the engine number that
        we would like to start. It takes the values ​​1 2 3 which indicates motors 1 2 and 3
        respectively
        """

        i_p, num_motor = self.get_motor_info_from_number(snr)
        request_answer = requests.get("http://"+i_p+"/stopM?sNr="+str(num_motor), timeout=TIME_OUT)
        if request_answer.status_code !=200:
            raise RuntimeError("Unable to control the motor, "+str(request_answer.status_code))

        if request_answer.text != "ok":
            raise RuntimeError("""Able to controle the motor but got not OK answer: """+
                               request_answer.text)
        return request_answer.text


    def step (self, snr, turn):
        """
        :param sNr: see start function
        :param turn: see start function
        Example:
        step(MOTOR_SPREADER, MOTOR_DIRECTION_BACKWARD )  turns the spreader backwards
        """
        return (self.start(snr, turn), self.stop(snr))


    def start_for(self, time_, snr, turn ):

        """:param t : This is the time during which we decide to run a
            motor. The syntax is t * ureg.second
        It is noted that we can also write t * ureg.millisecond in case
        we decide to run the engine for t millisecond.
        :param sNr : See the start function
        :param turn :See the start function

        example
        start_for(5000*ureg.nanosecond,MOTOR_CHASSIS ,MOTOR_DIRECTION_FORWARD )
        Here we decide to rotate the Chassis forward for 5000 nanosecond
        """
        if snr not in [MOTOR_CHASSIS , MOTOR_SPREADER, MOTOR_CRAB]:
            raise RuntimeError("""Invalid parameter, sNr must be either MOTOR_CHASSIS  or
                                MOTOR_SPREADER or MOTOR_CRAB . Got """ +str(snr))

        if time_ < 0:
            raise ValueError("t must be greater than 0 but got "+str(time_))

        arguments = [time_, snr, turn]
        self.dict_q[snr].put(arguments)

    def fswitch(self, value):

        request_answer=requests.get("http://"+self.slave_ip+"/fswitch?nr=3"+"&v="+str(value)+
                                    "&dim=1", timeout=TIME_OUT)
        return request_answer.text

    def _get_battery(self):
        """
        This function returns the battery state : the state of
        the master's battery as well as that of the slave
        """

        answer_1 = requests.get("http://"+self.master_ip+"/getBat?n=1", timeout=TIME_OUT)
        answer_2 = requests.get("http://"+self.slave_ip+"/getBat?n=2", timeout=TIME_OUT)

        if answer_1.status_code != 200:
            raise RuntimeError("Please check if the battery  1 is correctly powered")

        if answer_2.status_code != 200:
            raise RuntimeError("Please check if the battery 2 is correctly powered")

        return (int(answer_1.text), int(answer_2.text))

    battery = property(_get_battery)

    def change_speed(self, snr, diff):
        """
        This function allows us to modify the engine speed while varying its cyclic ratio.
        :param sNr:  see def start (sNr, turn) parameters
        :param diff: This parameter is used to vary the speed of the motor. it is an integer
        It should be noted that the maximum speed that the motor can reach is 100 and the
         motor speed cannot drop below 30
        Example:
		change_speed( MOTOR_SPREADER, -60 ) : allows to decrease the motorspeed 3 by 60
        """


        if not isinstance (diff, int):
            raise TypeError("diff must be an int but got "+str(diff))

        i_p, num_motor = self.get_motor_info_from_number(snr)
        request_answer = requests.get("http://"+i_p+"/changePWMTV?sNr="+str(num_motor)+"&diff="+
                                      str(diff), timeout=TIME_OUT)

        if request_answer.status_code != 200:
            raise RuntimeError(""""Unable to change the speed of the motor,"""+
                                str(request_answer.status_code))

        result = re.search("neuer Speed=\s+(\d+)", request_answer.text)
        num = int(result.groups()[0])
        return num

    def get_speed(self , snr):
        """ Returns the current speed for a motor """

        return self.change_speed(snr, 0)

    def set_speed(self , snr, speed):

        """ set the speed for a motor """
        current = self.change_speed(snr, 0)
        diff = speed - current
        return self.change_speed(snr, diff)

    def init (self, i_p):
        """
        The purpose of this function is to initialize the IP address of
        the master and once the IP address of the master is
        initialized to obtain that of the slave thanks to the getOtherEsp function
        """

        self.master_ip = i_p
        self.slave_ip = self.get_other_esp(i_p)

    def get_other_esp(self, i_p):
        """
        This function has the role of launching a request to obtain the IP address of the slave
        """
        request_answer = requests.get("http://" + i_p + "/getOtherEsp", timeout = TIME_OUT)
        if request_answer.status_code != 200:
            raise RuntimeError ("""I failed to get the IP address of the slave.
            Check if the latter is correctly supplied then try again""")
        return request_answer.text



if __name__ == "__main__":


    crane1_ip = "172.17.217.217"
    crane2_ip = "172.17.217.217"

    crane_1 = Crane()
    crane_2 = Crane()

    crane_1.init(crane1_ip)
    crane_2.init(crane2_ip)


    #crane_1.start_for(0.01*ureg.second, MOTOR_SPREADER, MOTOR_DIRECTION_BACKWARD )
    #crane_2.start_for(0.01*ureg.second, MOTOR_CRAB, MOTOR_DIRECTION_FORWARD )

    #crane_1.start_for(2*ureg.second, MOTOR_CRAB, MOTOR_DIRECTION_FORWARD )
    print(crane_1.fswitch(10))

    #print(crane_1.battery)
    #print(crane_1.change_speed(MOTOR_CRAB, 40))
    #crane_2.start_for(0.01*ureg.second, MOTOR_CHASSIS , MOTOR_DIRECTION_FORWARD )

    #print(crane_2.change_speed(MOTOR_SPREADER,20))
    #print(crane_2.battery)
    #crane_2.step(MOTOR_CHASSIS  ,MOTOR_DIRECTION_BACKWARD )
    #crane_1.step(MOTOR_CRAB, MOTOR_DIRECTION_BACKWARD )
    #print (crane_1.get_speed(MOTOR_CRAB))
