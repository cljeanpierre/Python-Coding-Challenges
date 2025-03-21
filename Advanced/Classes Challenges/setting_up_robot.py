#Classes Challenges (Advanced)

'''
Challenge 
Use your programming knowledge to create a new robotics company. Your idea for micro driving robots which are 
able to pick up and deliver objects was promising and now you want to start programming the logic. The Classes 
coding challenges will use your knowledge of Classes to solve some example scenarios. 

Try solving the first of these five challenges below!

First, create the class for our robot. Begin by setting up the instance variables to keep track of important 
data related to the robot. 

'''

#Setting Up Our Robot

class DriveBot:
  def __init__(self):
    self.motor_speed = 0
    self.sensor_range = 0
    self.direction = 0
  
robot_1 = DriveBot()

robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)