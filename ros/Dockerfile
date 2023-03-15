FROM ros:noetic

ENV CATKIN_WS=/root/catkin_ws
ENV CATKIN_WS_SRC=${CATKIN_WS}/src

RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends \
        python3-catkin-tools \
        ros-noetic-catkin \
        ros-noetic-rosbridge-server \
    && rm -rf /var/lib/apt/lists/*

COPY ./mission_execution ${CATKIN_WS_SRC}/mission_execution

RUN . /opt/ros/noetic/setup.sh && cd ${CATKIN_WS} && catkin build

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x entrypoint.sh
ENTRYPOINT /entrypoint.sh