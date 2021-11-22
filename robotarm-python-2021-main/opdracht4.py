from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')
for t in range(2):
    robotArm.grab()
    for i in range(2):
        robotArm.moveRight()
    robotArm.drop() 
    for g in range(2):
        robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for k in range(2):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()

robotArm.wait()
