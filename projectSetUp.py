import os
import shutil

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

def create_project(project_dir, project_name):
    create_project_folder(project_dir, project_name)
    create_project_structure(project_dir, project_name)
    copy_template_files(project_dir, project_name)
    print("Project structure created successfully!")

# Specify the project directory and name
project_directory = "/Users/adamaanna/documents/www"
project_name = "projectSetup"

# Call the function with the project directory and name
create_project(project_directory, project_name)
