#!/usr/bin/env python3
import rospy

from std_msgs.msg import Float64
from geometry_msgs.msg import Twist

import sys, select, termios, tty

msg = """
Control Your Toy!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .
q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%
space key, k : force stop
anything else : stop smoothly
CTRL-C to quit
"""

moveBindings = {
        'i':(1,0),
        'o':(1,-1),
        'j':(0,1),
        'l':(0,-1),
        'u':(1,1),
        ',':(-1,0),
        '.':(-1,1),
        'm':(-1,-1),
           }

speedBindings={
        'q':(1.1,1.1),
        'z':(.9,.9),
        'w':(1.1,1),
        'x':(.9,1),
        'e':(1,1.1),
        'c':(1,.9),
          }

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

speed = 8
turn = 0.5

def vels(speed,turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    
    rospy.init_node('turtlebot_teleop')

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
    try:
        while not rospy.is_shutdown():
            key = getKey()
            move_cmd = Twist()

            if key == ' ' or key == 'w' :
                print(key, end=" ")
                print("forward")
                move_cmd.linear.x += 0.2
            elif key == ' ' or key == 'x' :
                print(key, end=" ")
                print("backward")
                move_cmd.linear.x -= 0.2
            elif key == ' ' or key == 'a' :
                print(key, end=" ")
                print("left")
                move_cmd.angular.z += 0.2
            elif key == ' ' or key == 'd' :
                print(key, end=" ")
                print("right")
                move_cmd.angular.z -= 0.2
            elif key == ' ' or key == 'p' :
                break
            pub.publish(move_cmd)
    
    except:
        print(speed)

    finally:
        move_cmd.angular.x = 0.1
        pub.publish(move_cmd.angular.x)
       
        # twist = Twist()
        # twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
        # twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
        # pub.publish(twist)

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)