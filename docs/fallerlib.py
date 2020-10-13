""" Commentaire pour toute la lib """
import requests
IP_master= "172.17.217.217"
IP_slave= "172.17.217.61"

def startM(sNr,turn):
     """ Commentaire sur la fonction  (ce qu'elle fait)
      
     Details:
		sNr: 1,2,3, 
		turn: -1, 1 
		la vitesse est fixée par changePWM()
		
     Example:
		startM(1, -1) # to turn right
     """
     if sNr == 1 and turn == 1:
             r= requests.get("http://"+IP_master+"/startM?sNr=1&turn=1")
     elif sNr == 2 and turn ==1:
             r= requests.get("http://"+IP_master+"/startM?sNr=2&turn=1") 
     elif sNr == 1 and turn == -1:
             r= requests.get("http://"+IP_master+"/startM?sNr=1&turn=-1")
     elif sNr== 2 and turn == -1:
             r= requests.get("http://"+IP_master+"/startM?sNr=2&turn=-1")
     elif sNr == 3 and turn == 1:
             r= requests.get("http://"+IP_slave+"/startM?sNr=3&turn=1")
     elif sNr == 3 and turn == -1:
             r= requests.get("http://"+IP_slave+"/startM?sNr=3&turn=-1")
     else:
             raise Exception ("Error!!! sNr must be 1 , 2, 3 or turn must be -1 , 1")
 
     if r.status_code ==200:
             print(r.status_code)

     else:
             raise Exception("There must be an Error in your code")


def stopM(sNr):
    if sNr == 1:
		     r= requests.get("http://"+IP_master+"/stopM?sNr=1")
    elif sNr == 2:
             r= requests.get("http://"+IP_master+"/stop?sNr=2")
    elif sNr == 3:
             r= requests.get("http://"+IP_slave+"/stopM?sNr=3")
    else:
             raise Exception("....")

    if r != 200: 
             raise Exception("....")
    else:
		     print(r.status_code)

def changePWM(sNr, diff):

     if sNr == 1 and diff == 5: 
             r= requests.get("http://"+IP_master+"/changePWMTV?sNr=1&diff=5")
     elif sNr == 2 and diff == 5:
             r = requests.get("http://"+IP_master+"/changePWMTV?sNr=2&diff=5")
     elif sNr == 3 and diff == 5:
             r= requests.get("http:"+IP_slave+"/changePWMTV?sNr=3&diff=5")
     elif sNr == 1 and diff == -5:
            r= request.get("http://"+IP_master+"/changePWMTV?sNr=1&diff=-5")
     elif sNr == 2 and diff == -5:
            r= requests.get("http://"+IP_slave+"/changePWMTV?sNr=2&diff=-5")
     elif sNr ==3 and diff == -5:
          r= requests.get("http://"+IP_slave+"/changePWMTV?sNr=3&diff=-5")
     else:
          raise Exception ("Error")

   
     if r != 200: 
             raise Exception("....")
     else:
		     print(r.status_code)

def getBat(n):
    if n==1:
        r=requests.get("http://"+IP_master+"/getBat?n=1")
    elif n==2:
        r=requests.get("http://"+IP_slave+"/getBat?n=2")
    else:
        raise Exception ("Error")


def init(IP):
    IP_master= IP
    IP_slave = getOtherEsp(IP)
    
def getOtherEsp(IP):
    r = requests.get("http://" + IP +"/getOtherEsp")
    if r.status_code != 200:
       raise Exception ("....")

    return r.text 

	
