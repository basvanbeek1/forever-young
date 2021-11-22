from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')
robotArm.speed = 5
robotArm.moveRight()
robotArm.grab()
for s in range(7):
    for c in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for m in range(8):
        robotArm.moveLeft()
    robotArm.grab()  



robotArm.wait()
