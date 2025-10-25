# AI Task Planner

A full-stack web application for task management, where the priority of a new task (High, Medium, Low) is automatically predicted by a Machine Learning model in the backend.

---

## 🚀 Features

* **Create Tasks:** Add new tasks with a title and a description.
* **Automatic Priority (AI):** The AI in the backend analyzes the task text and automatically assigns a 'High', 'Medium', or 'Low' priority label.
* **Display Tasks:** A clean, scrollable list of all tasks with color-coded priority badges.
* **Delete Tasks:** Remove tasks from the list.
* **Real-time Updates:** The list updates automatically after creating or deleting a task.

---

## 🛠️ Tech Stack

This project is fully containerized using Docker and Docker Compose.

### Backend
* **Framework:** FastAPI (Python)
* **Data Validation:** Pydantic
* **Database:** MongoDB
* **Server:** Uvicorn

### Frontend
* **Library:** React (with Hooks)
* **Styling:** CSS

### AI / Data Science
* **Machine Learning:** Scikit-learn
* **Data Manipulation:** Pandas
* **Model Storage:** Joblib

### DevOps
* **Containerization:** Docker & Docker Compose

---

## 🐳 How to Run (via Docker)

This application is designed to run easily with a single command.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/tochiwilson/ai-task-planner.git](https://github.com/tochiwilson/ai-task-planner.git)
    cd ai-task-planner
    ```

2.  **Build and start the containers:**
    ```bash
    docker-compose up -d --build
    ```

3.  **View the application:**
    * The **Frontend** (React) is available at `http://localhost:3000`
    * The **Backend API** (FastAPI) is available at `http://localhost:8000/docs` (for documentation)

---

## 🤖 The AI Model: From Data to Prediction

The heart of this project is the text classification model trained to "understand" the urgency of a task.

1.  **Data Generation:** A synthetic dataset of 5,000 unique tasks was generated (`generate_dataset.py`). The focus was on creating high-quality data with clear contextual indicators for urgency (e.g., "due tomorrow", "critical bug").

2.  **Feature Engineering:** The text was converted into numerical data using `TfidfVectorizer`. The **`ngram_range=(1, 2)`** parameter was crucial here. It allows the model to recognize not only single words but also two-word phrases (like "due tomorrow") as a single, powerful feature.

3.  **Model Selection & Tuning:** A **`LinearSVC`** (Support Vector Classifier) was chosen, which is highly effective for text data. **`GridSearchCV`** was used to find the optimal hyperparameters to maximize the model's F1-score.

---

## 🎓 My Learning Journey & Challenges

This project was a personal challenge to apply my skills in AI (my field of study) in a complete, production-ready MLOps environment.

* **New Technologies:** Both **FastAPI** and **React** were completely new to me. It was a valuable experience to learn how to build a REST API with FastAPI and master Pydantic's strict data validation system. Managing state in React with `useState` and `useEffect` was also an important new skill.

* **The Biggest Challenge (AI):** My main hurdle was the model's accuracy. Initially, I thought that *more data* (quantity) was the solution. I trained the model on a copied dataset of 10,000 rows, but the results remained poor (e.g., "due tomorrow" was predicted as 'Low').

* **The Solution (Data Quality):** The breakthrough came when I realized my 10,000-row dataset consisted mostly of duplicates. The model wasn't learning anything new. The solution was to write a script (`generate_dataset.py`) to generate a **high-quality dataset of 5,000 unique rows**. This project taught me in practice that the **quality and context of data** are infinitely more important than pure data quantity.
