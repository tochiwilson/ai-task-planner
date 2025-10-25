import React from "react";

const TaskList = ({ tasks, onDelete }) => {
  return (
    <div>
      <h2>Task List</h2>
      {tasks.length === 0 && <p>No tasks available</p>}
      <ul>
        {tasks.map((task) => (
          <li key={task._id}>
            <span>#{task.taskNumber} - {task.title}</span>
            <p>{task.description}</p>
            <span className={`priority-badge priority-${task.priority.toLowerCase()}`}>{task.priority}</span>
            <button onClick={() => onDelete(task._id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TaskList;
