#Classes Challenges (Advanced)

'''
Challenge 
Use your programming knowledge to create a new robotics company. Your idea for micro driving robots which are 
able to pick up and deliver objects was promising and now you want to start programming the logic. The Classes 
coding challenges will use your knowledge of Classes to solve some example scenarios. 

Try solving the third of these five challenges below!

It can be tedious manually setting the values for each instance variable after we have created an object from 
the DriveBot class. We can enhance our constructor to automatically assign the values we provide to the 
instance variables. Instead of taking zero parameters, we are going to make the constructor take three 
parameters.
'''

#Enhanced Logic

class DriveBot:
    # Update this constructor!
    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

# Create robot_2 here!
robot_2 = DriveBot()
robot_2.motor_speed = 35
robot_2.direction = 75
robot_2.sensor_range = 25

print(robot_2.motor_speed)
print(robot_2.direction)
print(robot_2.sensor_range)