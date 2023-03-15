#!/bin/bash
set -e

# setup gazebo and ros environment
source "/root/catkin_ws/devel/setup.bash" --
exec "$@"