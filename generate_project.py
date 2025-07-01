import os
import random
import subprocess
from datetime import datetime

project_ideas = [
    "Weather App with API",
    "To-Do CLI app",
    "Markdown Blog Generator",
    "Simple Chat App with Socket",
    "Currency Converter with GUI",
    "BMI Calculator",
    "File Organizer Script",
    "Text-based Adventure Game",
    "Web Scraper for News",
    "Pomodoro Timer"
]

idea = random.choice(project_ideas)
folder_name = idea.lower().replace(" ", "-")
timestamp = datetime.now().strftime("%Y-%m-%d")
project_dir = f"{timestamp}-{folder_name}"

os.makedirs(project_dir, exist_ok=True)

with open(f"{project_dir}/README.md", "w") as f:
    f.write(f"# {idea}\n\nAuto-generated project for the week of {timestamp}.")

with open(f"{project_dir}/main.py", "w") as f:
    f.write(f"# {idea}\n\nprint('Hello, this is the {idea} project!')")

os.chdir(project_dir)
subprocess.run(["git", "init"])
subprocess.run(["git", "checkout", "-b", "main"])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Initial commit for weekly project"])
subprocess.run(["gh", "repo", "create", folder_name, "--public", "--source=.", "--remote=origin", "--push"])

print(f"✅ Project '{idea}' created and pushed to GitHub!")
