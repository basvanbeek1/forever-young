import time 
from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')
robotArm.grab();
for c in range(9):
    robotArm.moveRight()
robotArm.drop()
for c in range(5):
    robotArm.moveLeft()
robotArm.grab()
for c in range(5):
    robotArm.moveRight()
robotArm.drop()
for c in range(2):
    robotArm.moveLeft()
robotArm.grab()
for c in range(2):
    robotArm.moveRight()
robotArm.drop()

robotArm.wait()




