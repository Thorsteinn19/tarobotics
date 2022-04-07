#!/usr/bin/env python

import rospy
import actionlib
import sys
from move_base_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion

class Tmover():
    def __init__(self):
        pass

def simple_move(x,y):
    #create goal

    goal = MoveBaseGoal()

    #set goal
 
    rospy.loginfo("Set X = "+str(x))
    rospy.loginfo("Set W = "+str(y))
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose = Pose(Point(x-4,y+2,0),Quaternion(0,0,1,1))


    #start listner
    rospy.loginfo("Waiting for server")



    rospy.loginfo("Sending Goals")

    #send goal

    sac.send_goal(goal)
    rospy.loginfo("Waiting for server")

    #finish
    sucsess = sac.wait_for_result(rospy.Duration(20))
    state = sac.get_state()

    #print result


if __name__ == '__main__':
    try:
        rospy.init_node('nav_test', anonymous=False)
        goalsent = False
        sac = actionlib.SimpleActionClient('move_base', MoveBaseAction )
        sac.wait_for_server(rospy.Duration(5))
        
        simple_move(0,3)
        sac.wait_for_server(rospy.Duration(25))
        simple_move(0,6)
        simple_move(0,5)
        simple_move(1,5)
        simple_move(1,4)
        simple_move(0,4)
        simple_move(1,3)
        simple_move(3,6)
        simple_move(4,4)
        simple_move(2,4)
        simple_move(4,4)
        simple_move(5,3)
        simple_move(5,6)
        simple_move(7,6)
        simple_move(7,3)
        simple_move(5,3)
        simple_move(8,6)
        simple_move(8,4)
        simple_move(9,3)
        simple_move(10,3)
        simple_move(11,4)
    except rospy.ROSInterruptException:
        print("Keyboard Interrupt")