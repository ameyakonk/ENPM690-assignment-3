# ENPM690-assignment-3

## Overview
The repository contains the following contents.

1. Traversing a mobile Turtlebot3 using Teleop commands.
2. Autonomous Obstacle avoidance of Turtlebot3 based on Lidar data feedback.

## Personnel
### Ameya Konkar 

UID:118191058

Master's Student at University of Maryland, College Park

## Dependencies 

1. Python 3
2. ROS Noetic/Melodic
3. Gazebo

### Building the Program and Tests

```
sudo apt-get install git
cd catkin_ws/src
git clone --recursive https://github.com/ameyakonk/ENPM690-assignment-3.git master
cd ENPM690-assignment-3/src/
chmod +x autonomous.py
chmod +x teleop.py
cd ../..
cd ..
```

#### Q1. To Run Teleoperation code:
```
roslaunch ENPM690-assignment-3 teleop_.launch
```
To Move the turtlebot3, following are the keys
1. w - Forward
2. x - Backward
3. a - Left
4. d - Right
5. p - Quit process

Ctrl+C to quit program


#### Q2. To Run Obstacle Avoidance code:
```
roslaunch ENPM690-assignment-3 autonomous_.launch
```
Ctrl+C to quit program
