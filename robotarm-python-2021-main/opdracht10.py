from RobotArm import RobotArm
import time
robotArm = RobotArm('exercise 11')
robotArm.speed = 5
for i in range(8):
    robotArm.moveRight()
for y in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'white':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()



robotArm.wait()
