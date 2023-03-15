#!/usr/bin/env python3
# we do not plan here, we just use the manually predefined arm positions to
# scan the fuselage.

import actionlib

import rospy
from mission_execution.msg import MissionControlFeedback, MissionControlResult, \
    MissionControlAction

TASK_FAILED = 0
TASK_STARTED = 1
TASK_ENDED = 2


class MissionControl:
    _feedback = MissionControlFeedback()
    _result = MissionControlResult()

    def __init__(self, name='mission_control'):
        self._action_name = name
        self.missions = {
            'test_mission': self.test_mission
        }

        # provide an actionlib-interface to start and monitor missions
        self._as = actionlib.SimpleActionServer(
            self._action_name, MissionControlAction,
            execute_cb=self.execute_cb, auto_start=False)
        self._as.start()

    def execute_cb(self, mission_name):
        if mission_name not in self.missions:
            rospy.logerr(f'Can not start unknown mission {mission_name}')
            return False
        else:
            self.missions[mission_name]()

    def _wait(self):
        r = rospy.Rate(1)
        r.sleep()

    def test_mission(self):
        success = True
        tasks = []
        for x in range(1, 4):
            tasks += [
                {
                    'text_start': f'start to do something ({x}/4)',
                    'text_end': 'doing something finished',
                    'func': self._wait,
                    'param': [1.0]
                }
            ]

        for task in tasks:
            if self._as.is_preempt_requested():
                self._as.set_preempted()
                success = False
                break
            rospy.loginfo(task['text_start'])
            self._feedback.text = task['text_start']
            self._feedback.type = TASK_STARTED
            self._as.publish_feedback(self._feedback)

            task['func'](*task['param'])

            rospy.loginfo(task['text_end'])
            self._feedback.text = task['text_end']
            self._feedback.type = TASK_ENDED
            self._as.publish_feedback(self._feedback)

        if success:
            self._result.success = success
            rospy.loginfo(f'{self._action_name}: succeeded')
            self._as.set_succeeded(self._result)

    def spin(self):
        rospy.spin()


if __name__ == '__main__':
    rospy.init_node('mission_control', anonymous=True)
    node = MissionControl()
    node.spin()
