from RobotArm import RobotArm
import time
robotArm = RobotArm('exercise 10')
robotArm.speed = 5
robotArm.grab()
for i in range(9):
    robotArm.moveRight()
robotArm.drop()
for p in range(8):
    robotArm.moveLeft()
robotArm.grab()
for i in range(7):
    robotArm.moveRight()
robotArm.drop()
for p in range(6):
    robotArm.moveLeft()
robotArm.grab()
for i in range(5):
    robotArm.moveRight()
robotArm.drop()
for p in range(4):
    robotArm.moveLeft()
robotArm.grab()
for i in range(3):
    robotArm.moveRight()
robotArm.drop()
for p in range(2):
    robotArm.moveLeft()
robotArm.grab()
for i in range(1):
    robotArm.moveRight()
robotArm.drop()
for p in range(1):
    robotArm.moveLeft()

robotArm.wait()
