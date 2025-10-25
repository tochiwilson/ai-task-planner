import pandas as pd
import random

# Define templates and keywords
# This teaches the model the STRUCTURE of tasks
high_templates = [
    "fix critical bug in {module}",
    "urgent call with {person}",
    "report due tomorrow",
    "deadline for {project} is tomorrow",
    "submit {assignment} by eod",
    "resolve production issue now",
    "security vulnerability found in {module}",
    "server down alert",
    "fix hotfix for {project}",
    "mandatory meeting with {person} today",
    "homework is due tomorrow",
    "critical patch for {module}",
]

medium_templates = [
    "review code for {module}",
    "write documentation for {feature}",
    "prepare for meeting about {project}",
    "follow up with {person}",
    "choose team lead",
    "research {topic}",
    "plan next sprint",
    "refactor {module} code",
    "implement new feature {feature}",
    "test {module} functionality",
    "analyze user feedback for {project}",
]

low_templates = [
    "read article about {topic}",
    "watch tutorial on {tool}",
    "clean up {place}",
    "buy {item}",
    "listen to podcast about {topic}",
    "find new {item} for {place}",
    "archive old {item_plural}",
    "update personal {item}",
    "browse {topic} news",
]

# Define the fillers
fillers = {
    "module": [
        "payment module",
        "login api",
        "analytics dashboard",
        "database",
        "ui components",
    ],
    "person": [
        "the client",
        "my manager",
        "the stakeholder",
        "the team lead",
        "professor smith",
    ],
    "project": [
        "the new feature",
        "q4 budget",
        "the marketing campaign",
        "server migration",
        "school project",
    ],
    "assignment": [
        "physics homework",
        "ml algorithms report",
        "business presentation",
        "final paper",
    ],
    "feature": ["dark mode", "user profiles", "search bar", "notifications"],
    "topic": [
        "ai and ml",
        "python 3.12",
        "mlops",
        "docker",
        "fastapi trends",
        "new frameworks",
    ],
    "tool": ["react", "kubernetes", "tensorflow", "git", "powerbi"],
    "place": ["my desktop", "the office", "my downloads folder", "google drive"],
    "item": ["laptop wallpaper", "notebook", "coffee machine", "keyboard"],
    "item_plural": ["emails", "files", "project documents", "tickets"],
}


def generate_task(template, label):
    """Fills a template with random fillers."""
    task = template
    # Find all {keys} in the template and replace them
    for key in fillers.keys():
        placeholder = "{" + key + "}"
        if placeholder in task:
            task = task.replace(placeholder, random.choice(fillers[key]))
    return {"task": task, "priority_label": label}


# --- Main script ---
DATASET_SIZE = 5000
OUTPUT_FILE = (
    "./dataset/generated_tasks.csv"
)
tasks_list = []

print(f"Starting generation of {DATASET_SIZE} unique tasks...")

for i in range(DATASET_SIZE):
    # Create a realistic distribution
    rand_num = random.random()
    if rand_num < 0.30:  # 30% High priority
        template = random.choice(high_templates)
        tasks_list.append(generate_task(template, "High"))
    elif rand_num < 0.70:  # 40% Medium priority
        template = random.choice(medium_templates)
        tasks_list.append(generate_task(template, "Medium"))
    else:  # 30% Low priority
        template = random.choice(low_templates)
        tasks_list.append(generate_task(template, "Low"))

# Create the DataFrame and save
df = pd.DataFrame(tasks_list)

# Remove any rare duplicates that the generator created
df.drop_duplicates(subset=["task"], inplace=True)

df.to_csv(OUTPUT_FILE, index=False)

print(f"\nDataset successfully generated and saved as '{OUTPUT_FILE}'.")
print(f"Total unique rows: {len(df)}")
