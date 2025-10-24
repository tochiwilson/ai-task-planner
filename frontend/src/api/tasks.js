const API_URL = "http://127.0.0.1:8000"; // backend FastAPI

export const getTasks = async () => {
    const res = await fetch(`${API_URL}/task`);
    return res.json();
};

export const createTask = async (task) => {
    const res = await fetch(`${API_URL}/task`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(task),
    });
    return res.json();;
};

export const updateTask = async (id, updates) => {
    const res = await fetch(`${API_URL}/task/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(updates),
    });
    return res.json();
};

export const deleteTask = async (id) => {
    const res = await fetch(`${API_URL}/task/${id}`, {
        method: "DELETE",
    });
    return res.json();
};
