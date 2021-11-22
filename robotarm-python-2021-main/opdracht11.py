from RobotArm import RobotArm
import time
robotArm = RobotArm('exercise 12')
robotArm.speed = 5

for i in range(8):
    robotArm.moveRight()
for y in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'red':
            for u in range(y+1):
                 robotArm.moveRight()
            robotArm.drop()
            for j in range(y+2):
                robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()



robotArm.wait()
