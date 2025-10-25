import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

INPUT_FILE = "./dataset/cleaned_tasks.csv"
MODEL_FILENAME = "./model/priority_classifier_model.pkl"

try:
    df = pd.read_csv(INPUT_FILE)
    print(f"Data successfully loaded from: {INPUT_FILE} (Size: {len(df)})")
except FileNotFoundError:
    print(f"Error: {INPUT_FILE} not found. Please make sure you have run clean_data.py.")
    exit()

# features and labels
X = df["task"]  # input: task + descriptions
y = df["priority_label"]  # outpuy: (High/Medium/Low)

# split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# pipeline: vectorizer for text + classifier for priority
model_pipeline = Pipeline(
    [("vectorizer", TfidfVectorizer()),
    ("classifier", LinearSVC(random_state=42))]
)

# hyperparameter grid
param_grid = {
    # 2 word combinations
    'vectorizer__ngram_range': [(1,2)],
    
    # complexity parameter for SVM
    'classifier__C': [0.5, 1.0, 5.0, 10.0],
    
    # min document frequency for the vectorizer
    'vectorizer__min_df': [1, 5]
}

# grid search
grid_search = GridSearchCV(
    model_pipeline,
    param_grid,
    cv=5,
    scoring="f1_weighted", 
    n_jobs=-1,
    verbose=2
)

# train model
grid_search.fit(X_train, y_train)
model_pipeline = grid_search.best_estimator_

# model evaluation
y_pred = model_pipeline.predict(X_test)

# classification report
print("\n" + "=" * 50)
print("MODEL EVALUATION REPORT ON TEST DATA")
print("=" * 50)
print(classification_report(y_test, y_pred))

# save model
joblib.dump(model_pipeline, MODEL_FILENAME)
print("=" * 50)
print(f"Model successfully saved as '{MODEL_FILENAME}'.")
