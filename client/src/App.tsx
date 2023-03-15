import React from 'react';
import './App.css';
import ROSLIB from 'roslib';
import Toolbar from './Toolbar';

function App() {
  const ros = new ROSLIB.Ros({ url: 'ws://localhost:9090' })
  ros.getTopics((result) => { console.log(result) });

  return (
    <div className="App">
      <div className='toolbar'>
        <Toolbar ros={ros} />
      </div>
    </div>
  );
}

export default App;
