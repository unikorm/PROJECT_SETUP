#!/usr/bin/env python3

import os
import shutil
import subprocess
import json

def initialize_npm(project_dir, project_name):
    os.chdir(os.path.join(project_dir, project_name))
    subprocess.run(["npm", "init", "-y"])

def create_project_folder(project_dir, project_name):
    os.makedirs(os.path.join(project_dir, project_name))

def create_project_structure(project_dir, project_name):
    folders = ["src"]
    for folder in folders:
        os.makedirs(os.path.join(project_dir, project_name, folder))

def copy_template_files(project_dir, project_name):
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
    shutil.copy(os.path.join(template_dir, "index.html"), os.path.join(project_dir, project_name, "src/index.html"))
    shutil.copy(os.path.join(template_dir, "main.js"), os.path.join(project_dir, project_name, "src/main.js"))
    shutil.copy(os.path.join(template_dir, "style.css"), os.path.join(project_dir, project_name, "src/style.css")) 
    shutil.copy(os.path.join(template_dir, ".gitignore"), os.path.join(project_dir, project_name, ".gitignore"))
    shutil.copy(os.path.join(template_dir, "LICENSE"), os.path.join(project_dir, project_name, "LICENSE"))
    shutil.copy(os.path.join(template_dir, "README.md"), os.path.join(project_dir, project_name, "README.md"))

def initialize_git_repository(project_dir, project_name):
    os.chdir(os.path.join(project_dir, project_name))  # Change the current working directory to the project directory
    subprocess.run(["git", "init"])  # Initialize a Git repository
    subprocess.run(["git", "branch", "-m", "main"]) # Change name of initial branch
    subprocess.run(["git", "add", "."])  # Stage all files
    subprocess.run(["git", "commit", "-m", "Initial mother fucker (commit)"])  # Commit the changes

def add_remote_repository(project_dir, project_name, remote_url):
    os.chdir(os.path.join(project_dir, project_name))  # Change the current working directory to the project directory
    subprocess.run(["git", "remote", "add", "origin", remote_url])  # Add the remote repository URL

def push_to_remote_repository(project_dir, project_name, commit_message):
    os.chdir(os.path.join(project_dir, project_name))
    subprocess.run(["git", "commit", "-am", commit_message])  # Commit all changes
    subprocess.run(["git", "push", "-u", "origin", "main"])  # Push to the remote repository

def update_package_json(project_dir, project_name, description):
    package_file = os.path.join(project_dir, project_name, 'package.json')
    with open(package_file, 'r') as file:
        data = json.load(file)
    
    data['description'] = description
    data['author'] = 'adamko69'
    
    with open(package_file, 'w') as file:
        json.dump(data, file, indent=2)

def update_readme(project_dir, project_name, description):
    readme_file = os.path.join(project_dir, project_name, "README.md")
    with open(readme_file, "w") as f:
        f.write(f"# {project_name}\n\n{description}\n")

def create_project():
    project_dir = input("Enter the local project path in this computer: ")
    project_name = input("Enter the project name: ")
    description = input("Enter main description of this site: ")
    remote_url = input("Enter URL of your remote repository from Github: ")
    
    create_project_folder(project_dir, project_name)
    initialize_npm(project_dir, project_name)
    create_project_structure(project_dir, project_name)
    copy_template_files(project_dir, project_name)
    initialize_git_repository(project_dir, project_name)
    add_remote_repository(project_dir, project_name, remote_url)
    update_package_json(project_dir, project_name, description)
    update_readme(project_dir, project_name, description)
    push_to_remote_repository(project_dir, project_name, "update README file")

    print("Project structure created successfully!")
    print("Git repository initialized with initial commit")
    print(f"Remote repository {remote_url} added as origin.")
    print("Initial commit pushed to the remote repository. Now you can continue to program some great stuff.... you bitch! Now you must code until your death")
    print("Project created successfully!")

# Call the function to create the project interactively
create_project()