from math import sin, cos
from pylx16a.lx16a import *
import time

LX16A.initialize("COM6", 0.1)

try:
    #head
    servo1 = LX16A(1)
    #right leg
    servo10 = LX16A(10)
    servo12 = LX16A(12)
    #left leg
    servo11 = LX16A(11)
    servo13 = LX16A(13)   

    #servo1.set_angle_limits(0, 240)
    #servo2.set_angle_limits(0, 240)
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

t = 0
#head
try:
    print(servo1.get_physical_angle())
except ServoTimeoutError as i:
    print(f"Servo {e.id_} is not connected")


#right leg
try:
    print(servo10.get_physical_angle())
except ServoTimeoutError as i:
    print(f"Servo {e.id_} is not connected")
try:
    print(servo12.get_physical_angle())
except ServoTimeoutError as i:
    print(f"Servo {e.id_} is not connected")

#left leg
try:
    print(servo11.get_physical_angle())
except ServoTimeoutError as i:
    print(f"Servo {e.id_} is not connected")
try:
    print(servo13.get_physical_angle())
except ServoTimeoutError as i:
    print(f"Servo {e.id_} is not connected")

#Default Stage

#right leg
servo10.move(188.01)
servo12.move(43.01)
#left leg
servo11.move(151.01)
servo13.move(151.01) 




while True:
   servo1.move(120+(sin(5*t)*30))
   servo2.move(cos(t) * 60 + 60)


#right leg
    servo10.move(188 + (sin(t) * 14))
    servo12.move(43 + (sin(t)* 14))
#left leg
    servo11.move(151 + (sin(t)* 14))
    servo13.move(174 + (sin(t)* 14)) 
    
    time.sleep(0.1)
    t += 1

    if t>20: #figure out the number/cycle that it completes a step in
        print("finito")
        #right leg
        print(servo10.get_physical_angle())
        print(servo12.get_physical_angle())
        #left leg
        print(servo11.get_physical_angle())
        print(servo13.get_physical_angle())
        quit()

