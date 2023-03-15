# roslibjs-react-typescript-docker
Minimal Example using ROS noetic with libjs and a React-based frontend for debugging of action execution.

## How to run

There are multiple ways to run this code:

### Run docker environment
1. install docker
1. install docker-compose
1. install terminator
1. run `docker-compose build`
1. run the `./start.bash`-script
1. open a web browser to http://localhost:3000 and click on the blue button in the top-left corner to start the action

### Run locally
(for ros)
1. install catkin and the rosbridge-server: `apt install python3-catkin-tools ros-noetic-catkin ros-noetic-rosbridge-server`
1. copy the `ros/mission_execution`-folder to a ROS-workspace
1. run `catkin build`
1. resource your workspace
1. start the ROS part with `roslaunch mission_execution mission_control.launch`

(for web)
1. install node.js
1. go into the `client/`-folder
1. run `npm i`
1. run `npm start`
1. a window with the webpage should open in your default browser, when you started the mission_control.launch before you can click on the blue button in the top-left corner to start the action