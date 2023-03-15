cmake_minimum_required(VERSION 3.0.2)
project(mission_execution)

## Find catkin dependencies
find_package(catkin REQUIRED COMPONENTS actionlib message_generation)

## Add actions
add_action_files(DIRECTORY action FILES MissionControl.action)

## Generate messages
generate_messages(DEPENDENCIES std_msgs actionlib_msgs)

## Define catkin exports
catkin_package(
  CATKIN_DEPENDS message_runtime rospy actionlib
)


## Install scripts and executables
install(PROGRAMS
  scripts/mission_execution_server.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

catkin_package(CATKIN_DEPENDS)
