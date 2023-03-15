cmake_minimum_required(VERSION 2.8.3)
project(mission_execution)

find_package(catkin REQUIRED genmsg actionlib_msgs actionlib)
add_action_files(DIRECTORY action FILES MissionControl.action)
generate_messages(DEPENDENCIES actionlib_msgs)

catkin_package(CATKIN_DEPENDS)
