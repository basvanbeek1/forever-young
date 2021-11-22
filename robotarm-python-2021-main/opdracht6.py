from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')
robotArm.speed = 5
for v in range(6):
    for c in range(5):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
        robotArm.moveRight()
    for b in range(9):
        robotArm.moveLeft()
        

        


    


robotArm.wait()
