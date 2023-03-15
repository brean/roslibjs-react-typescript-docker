#! /usr/bin/env python3
import time

from roslibpy import Message, Ros
from roslibpy.actionlib import ActionClient, Goal


def main():
    # ros = Ros("mission_execution", 9090)
    ros = Ros("localhost", 9090)
    ros.run()

    client = ActionClient(
        ros, "/mission_control",
        "mission_execution/MissionControlAction")
    goal = Goal(client, Message({"mission_name": 'test_mission'}))

    goal.on('feedback', lambda f: print(f))

    goal.send()
    result = goal.wait(10)

    assert result["success"]

    client.dispose()
    time.sleep(2)
    ros.close()


if __name__ == '__main__':
    main()
