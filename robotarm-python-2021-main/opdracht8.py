from RobotArm import RobotArm
import time
robotArm = RobotArm('exercise 9')
robotArm.speed = 5
robotArm.grab()
for i in range(5):
    robotArm.moveRight()
robotArm.drop()
for x in range(3):
    for q in range(4):
        robotArm.moveLeft()
    robotArm.grab()
    for i in range(5):
        robotArm.moveRight()
    robotArm.drop()
for s in range(7):
    robotArm.moveLeft()
robotArm.grab()
for h in range(5):
        robotArm.moveRight()
robotArm.drop()
for k in range(2):
    for p in range(4):
        robotArm.moveLeft()
    robotArm.grab()
    for g in range(5):
        robotArm.moveRight()
    robotArm.drop()
for j in range(6):
    robotArm.moveLeft()
robotArm.grab()
for t in range(5):
    robotArm.moveRight()
robotArm.drop()
for u in range(4):
        robotArm.moveLeft()
robotArm.grab()
for d in range(5):
        robotArm.moveRight()
robotArm.drop()
for o in range(5):
        robotArm.moveLeft()
robotArm.grab()
for f in range(5):
        robotArm.moveRight()
robotArm.drop()






robotArm.wait()
