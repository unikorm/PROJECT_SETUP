import os
import shutil
import subprocess

def create_project_folder(project_dir, project_name):
    os.makedirs(os.path.join(project_dir, project_name))

def create_project_structure(project_dir, project_name):
    folders = ["src", "assets"]
    for folder in folders:
        os.makedirs(os.path.join(project_dir, project_name, folder))

def copy_template_files(project_dir, project_name):
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
    shutil.copy(os.path.join(template_dir, "index.html"), os.path.join(project_dir, project_name, "src/index.html"))
    shutil.copy(os.path.join(template_dir, "main.js"), os.path.join(project_dir, project_name, "src/main.js"))
    shutil.copy(os.path.join(template_dir, "style.css"), os.path.join(project_dir, project_name, "src/style.css"))

def initialize_git_repository(project_dir, project_name):
    os.chdir(os.path.join(project_dir, project_name))  # Change the current working directory to the project directory
    subprocess.run(["git", "init"])  # Initialize a Git repository
    subprocess.run(["git", "branch", "-m", "main"]) # Change name of initial branch
    subprocess.run(["git", "add", "."])  # Stage all files
    subprocess.run(["git", "commit", "-m", "Initial commit"])  # Commit the changes

def add_remote_repository(project_dir, project_name, remote_url):
    os.chdir(os.path.join(project_dir, project_name))  # Change the current working directory to the project directory
    subprocess.run(["git", "remote", "add", "origin", remote_url])  # Add the remote repository URL

def push_to_remote_repository(project_dir, project_name):
    os.chdir(os.path.join(project_dir, project_name))  # Change the current working directory to the project directory
    subprocess.run(["git", "push", "-u", "origin", "main"])  # Push to the remote repository

def create_project():
    project_dir = input("Enter the project directory path: ")
    project_name = input("Enter the project name: ")
    remote_url = input("Enter URL of your remote repository.")
    
    create_project_folder(project_dir, project_name)
    create_project_structure(project_dir, project_name)
    copy_template_files(project_dir, project_name)
    initialize_git_repository(project_dir, project_name)
    add_remote_repository(project_dir, project_name, remote_url)
    push_to_remote_repository(project_dir, project_name)

    print("Project structure created successfully.... you bitch! Now you must code until your death")
    print("Git repository initialized with initial commit")
    print(f"Remote repository {remote_url} added as origin.")
    print("Initial commit pushed to the remote repository. Now you can continue to program some great stuff")

# Call the function to create the project interactively
create_project()