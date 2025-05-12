import os

# Define the desired folder structure with capitalized first letters
folders = [
    "Data",
    "Notebooks",
    "Src/Data_pipeline",
    "Src/Features",
    "Src/Models",
    "Src/Api",
    "Src/Utils",
    "Dashboard",
    "Docker",
    "Mlflow",
    ".Github"
]

def create_project_structure(base_path='.'):
    for folder in folders:
        path = os.path.join(base_path, folder)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created: {path}")
        else:
            print(f"Already exists: {path}")

if __name__ == "__main__":
    create_project_structure()
