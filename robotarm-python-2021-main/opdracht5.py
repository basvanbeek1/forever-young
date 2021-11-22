from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')
robotArm.speed = 3
for i in range(7):
    robotArm.moveRight()
for u in range(8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()
    




robotArm.wait()
