#Classes Challenges (Advanced)

'''
Challenge 
Use your programming knowledge to create a new robotics company. Your idea for micro driving robots which are 
able to pick up and deliver objects was promising and now you want to start programming the logic. The Classes 
coding challenges will use your knowledge of Classes to solve some example scenarios. 

Try solving the second of these five challenges below!

Add some logic to our robot. It would be very useful to be able to control our robot, so we are going to create 
a control_bot method which changes the speed and direction. We are also going to create a method called 
adjust_sensor. This method is used to change the range of our robot’s sensors which are used to detect obstacles. 

'''

#Adding Robot Logic

class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0
    
    # Add the methods here!
    def control_bot(self, new_speed, new_direction):
      self.motor_speed = new_speed
      self.direction = new_direction
    def adjust_sensor(self, new_sensor_range):
      self.sensor_range = new_sensor_range

robot_1 = DriveBot()
# Use the methods here!
robot_1.control_bot(10, 180)
robot_1.adjust_sensor(20)
print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)