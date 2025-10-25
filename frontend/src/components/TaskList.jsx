import React from "react";

const TaskList = ({ tasks, onDelete }) => {
  return (
    <div className="list-container">
      <h2>Task List</h2>
      {tasks.length === 0 && <p>No tasks available</p>}
      <ul>
        {tasks.map((task) => (
          <li key={task._id}>
            <div className="task-content">
              <span>#{task.taskNumber} - {task.title}</span>
              <p>{task.description}</p>
            </div>

            <div className="task-actions">
              <span className={`priority-badge priority-${task.priority.toLowerCase()}`}>
                {task.priority}
              </span>
              <button onClick={() => onDelete(task._id)}>Delete</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TaskList;
