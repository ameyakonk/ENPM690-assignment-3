import rospy
import math
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

message = 0
def publishVel(pub):
    data = getData()
    
  # if laser data inrange 0.4-0.7, change direction.
    if data >= 0.4 and data < 0.7:
     #   ROS_ERROR_STREAM("Obstacle detected")
        move_cmd = Twist()
        move_cmd.linear.x  = 0.1
        move_cmd.angular.z =  -1
        pub.publish(move_cmd)
    elif data < 0.4: 
     #   ROS_ERROR_STREAM("Obstacle in close proximity")
        move_cmd = Twist()
        move_cmd.linear.x  = -0.2
        move_cmd.angular.z =  -1
        pub.publish(move_cmd)
    else:   # if laser data greater than 0.4, move straight
     #   ROS_INFO_STREAM("Laser reading: " << msg.ranges[sensor_data])
        move_cmd = Twist()
        move_cmd.linear.x  = 0.5
        move_cmd.angular.z = 0.0
        pub.publish(move_cmd)

def setData(msg_):
    global message
    message = msg_    

def getData():
    return message

def callback(msg):
    sensor_data = 90*math.pi/180
    min_ = 10
    start = 340
    for i in range(5):
        if start >= 360:
            start = 0
        min_ = min(min_, msg.ranges[start])
        start += 10
        
    setData(min_)

if __name__=="__main__":
    
    rospy.init_node('turtlebot_autonomous')

    rospy.Subscriber('scan', LaserScan, callback)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10) 
    
    # spin() simply keeps python from exiting until this node is stopped
    while not rospy.is_shutdown():
        publishVel(pub)
    #    rospy.spin()