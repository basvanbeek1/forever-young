from RobotArm import RobotArm
import time
robotArm = RobotArm('exercise 13')
robotArm.speed = 5
for t in range(9):
    robotArm.grab()


robotArm.wait()
