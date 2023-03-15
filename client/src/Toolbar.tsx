import * as React from 'react';
import { Fab, Stack, Tooltip } from '@mui/material';
import PlayArrowIcon from '@mui/icons-material/PlayArrow';
import ROSLIB from 'roslib';

interface IToolbarProps {
  ros: ROSLIB.Ros
}

export default function Toolbar(props: IToolbarProps) {
  const missionControlClient = new ROSLIB.ActionClient({
    ros: props.ros,
    serverName: '/mission_execution',
    actionName: 'mission_execution/MissionControl'
  });

  const goal = new ROSLIB.Goal({
    actionClient: missionControlClient,
    goalMessage: new ROSLIB.Message({
      mission_name: 'test_mission'
    })
  });

  goal.on('feedback', function (feedback) {
    console.log('Feedback: ' + feedback.text + '(' + feedback.type + ')');
  });

  goal.on('result', function (result) {
    console.log('Final Result: ' + result.success);
  });


  return <Stack spacing={1}>
    <Tooltip title="Start" placement='right'>
      <Fab
        color={"primary"}
        onClick={() => {
          if (props.ros.isConnected) {
            console.log('START ACTION!');
            
            goal.send();
          } else {
            console.error('not connected')
          }
        }}
        aria-label="Start">
        <PlayArrowIcon />
      </Fab>
    </Tooltip>
  </Stack>
}