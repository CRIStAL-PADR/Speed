
import fallerlib


fallerlib.init("172.17.217.217")

t = fallerlib.getOtherEsp("172.17.217.217")
print("résultat est ", t)
	

#fallerlib.start(fallerlib.MotorChassis, fallerlib.MotorDirectionForward)
#fallerlib.start(fallerlib.MotorSpreader,fallerlib.MotorDirectionBackward)



fallerlib.change_speed(fallerlib.MotorSpreader, 10)
fallerlib.change_speed(fallerlib.MotorChassis, -17)


#fallerlib.stop(fallerlib.MotorSpreader)
