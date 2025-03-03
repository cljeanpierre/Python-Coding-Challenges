#Classes Challenges (Advanced)

'''
Challenge 
Use your programming knowledge to create a new robotics company. Your idea for micro driving robots which are 
able to pick up and deliver objects was promising and now you want to start programming the logic. The Classes 
coding challenges will use your knowledge of Classes to solve some example scenarios. 

Try solving the last of these five challenges below!

In order to keep track of the robots we are creating, we want to be able to assign an ID value to each robot 
when it is created. If we create five robots in a row, we want the IDs of each robot to be 1, 2, 3, 4, and 5 
respectively. This can be accomplished by using a class variable counter which increments and is assigned to 
an instance variable for the ID whenever the constructor is called. 

'''

#Identifying Robots

class DriveBot:
  # Create a counter to keep track of how many robots were created
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        # Assign an `id` to the robot when it is constructed by incrementing the counter and assigning the value to `id`
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count

    
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

print(robot_1.id)
print(robot_2.id)
print(robot_3.id)
