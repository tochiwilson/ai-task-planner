import pandas as pd
import re

INPUT_FILE = "./dataset/messy_tasks_dataset.csv"
OUTPUT_FILE = "./dataset/cleaned_tasks.csv"

try:
    df = pd.read_csv(INPUT_FILE)
    print(f"Data successfully loaded from: {INPUT_FILE}")
except FileNotFoundError:
    print(f"Error: {INPUT_FILE} not found. Please make sure the file is in this directory.")
    exit()

# data cleaning
df.dropna(subset=["task"], inplace=True)

def clean_text(text):    
    text = str(text).lower()
    
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    
    return text

df["task"] = df["task"].apply(clean_text)
df["priority_label"] = df["priority_label"].str.strip().str.capitalize()
df.drop_duplicates(subset=["task", "priority_label"], inplace=True)
df.to_csv(OUTPUT_FILE, index=False)

print("\nSample of the cleaned data:")
print(df.head())
