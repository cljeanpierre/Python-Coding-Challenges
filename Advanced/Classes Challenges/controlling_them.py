#Classes Challenges (Advanced)

'''
Challenge 
Use your programming knowledge to create a new robotics company. Your idea for micro driving robots which are 
able to pick up and deliver objects was promising and now you want to start programming the logic. The Classes 
coding challenges will use your knowledge of Classes to solve some example scenarios. 

Try solving the fourth of these five challenges below!

Add a new feature that allows the user to control multiple robots at once. The robots should be able to all 
have the same latitude and longitude GPS destination coordinates as well as a setting for disabling them all 
called all_disabled. We can accomplish this using class variables.

'''

#Controlling Them All

class DriveBot:
    all_disabled = False
    latitude = -999999
    longitude = -999999

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

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

# Change the latitude, longitude, and all_disabled values for all three robots using only three lines of code!

DriveBot.longitude = 50.0
DriveBot.latitude = -50.0
DriveBot.all_disabled = True

print(robot_1.latitude)
print(robot_2.longitude)
print(robot_3.all_disabled)