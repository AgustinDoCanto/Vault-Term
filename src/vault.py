import os
import time
import subprocess
import inquirer
from tabulate import tabulate
import stat


VAULT_MEDIA_PATH = "../Project-Vault/"
VAULT_BASE_NAME = "Project-Vault"

def figlet_print(text, font="standard"):
    result = subprocess.run(['figlet', '-f', font, text], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def print_banner():
	banner_print = figlet_print("Vault-Term", "standard")	
	print(banner_print)

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Unix/Linux or macOS
    else:
        os.system('clear')

def make_backup_os(backup_path):
    def get_unique_path_name(base_name, backup_path):
        backup_folder_path = os.path.join(backup_path, base_name)
        counter = 1
        
        while os.path.exists(backup_folder_path):
            backup_folder_path = os.path.join(backup_path, f"{base_name}_{counter}")
            counter += 1
        
        return backup_folder_path
    
    BACKUP_PATH = get_unique_path_name(VAULT_BASE_NAME, backup_path)

    result = subprocess.run(['cp', '-r', VAULT_MEDIA_PATH, BACKUP_PATH], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode == 0:
        print(f"Backup completed successfully. \n Folder saved as: {BACKUP_PATH}")
    else:
        print(f"Backup failed. \n Error: {result.stderr.decode('utf-8')}")
    
    return result.stdout.decode('utf-8')

##################
# CREATE PROJECT #
##################

def create_project_folder():
    # Prompt to ask for the folder name
    questions = [
        inquirer.Text('folder_name', message="Enter the name")
    ]
    
    # Get the user's input
    answers = inquirer.prompt(questions)
    folder_name = answers['folder_name']
    
    if folder_name == '':
        main_menu()
    else:
        # Define the path where the folder will be created
        base_path = VAULT_MEDIA_PATH
        full_path = os.path.join(base_path, folder_name)
        
        # Create the folder if it doesn't exist
        if not os.path.exists(full_path):
            os.makedirs(full_path)
            print(f"Project '{folder_name}' created successfully.")
            time.sleep(1)
            main_menu()
        else:
            print(f"This project folder name '{folder_name}' already exists.")
            time.sleep(1)
            main_menu()

def not_implemented_yet():
    print("Not implemented yet :(")
    time.sleep(1)
    main_menu()
   

def open_file_with_vim(file_path):
    try:
        # Executes vim with the path provided
        subprocess.run(['vim', file_path])
    except Exception as e:
        print(f"An error occurred while trying to open the file: {e}")


def list_directory_contents_with_permissions(path):
    try:
        files = os.listdir(path)
        
        # Lists all the projects
        table_data = []
        for file in files:
            file_path = os.path.join(path, file)
            file_stat = os.stat(file_path)
            permissions = stat.filemode(file_stat.st_mode)
            table_data.append([permissions, file])
        
       
        headers = ["PERMISSIONS", "PROJECTS"]

        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

        # Prompt to ask for the project name
        questions = [
            inquirer.Text('project_name', message="Enter the project name")
        ]

        # Get the user's input
        answers = inquirer.prompt(questions)
        project_name = answers['project_name']
        
        if project_name == '':
            main_menu()
        else:
            for file in files:
                # Select the project
                if file == project_name:
                    try:
                        project_files = []
                        # Join the project name to path
                        file_path = os.path.join(path, project_name)
                        project_files = os.listdir(file_path)
                        clear_screen()
                        print_banner()

                        table_data = []
                        # List all the files and folders in the project
                        for project in project_files:
                            file_path = os.path.join(path, project_name, project)
                            file_stat = os.stat(file_path)
                            permissions = stat.filemode(file_stat.st_mode)
                            table_data.append([permissions, project])


                        headers = ["PERMISSIONS", "FILES"]
                        print(tabulate(table_data, headers=headers, tablefmt="github"))

                        project_name_edit = ''

                        while project_name_edit != 'back':
                            # Prompt to ask for the project name to edit
                            questions = [
                                inquirer.Text('project_name_edit', message="Edit project")
                            ]

                            # Get the user's input
                            answers = inquirer.prompt(questions)
                            project_name_edit = answers['project_name_edit']

                            # Open for edit the file or folder selected
                            if project_name_edit == '':
                                main_menu()
                                return
                            elif project_name_edit != 'back':
                                file_path = os.path.join(path, file, project_name_edit)
                                open_file_with_vim(file_path)

                        main_menu()
                    except Exception as e:
                        print(f"An unexpected error occurred: {e}")

    except FileNotFoundError:
        print(f"Error: The directory {path} does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for directory {path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


###################
# MANAGE PROJECTS #
###################
def manage_projects_function():
    clear_screen()
    print_banner()
    list_directory_contents_with_permissions(VAULT_MEDIA_PATH)
    

#################
# CREATE BACKUP #
#################

def create_backup():
    # Prompt to ask for the folder name
    questions = [
        inquirer.Text('backup_path', message="Enter Backup Path")
    ]
    # Get the user's input
    answers = inquirer.prompt(questions)
    backup_path = os.path.expanduser(answers['backup_path'])

    if not os.path.exists(backup_path):
        print(backup_path)
        print("The given path doesn't exists")
        input("Press Enter to continue...")
        main_menu()
    else:
        make_backup_os(backup_path)
        input("Press Enter to continue...")
        main_menu()


def create_backup_function():
    clear_screen()
    print_banner()
    create_backup()

#############
# MAIN MENU #
#############

MAIN_MENU_OPTIONS = ['Create Project', 'Create Backup', 'Set Media Path', 'Manage projects', 'Exit']

def main_menu():
    clear_screen()
    print_banner()
    questions = [
        inquirer.List('option',
                      message="Option menu",
                      choices=MAIN_MENU_OPTIONS
                     ),
    ]
    
    answers = inquirer.prompt(questions)
    if answers['option'] == MAIN_MENU_OPTIONS[0]:
        clear_screen()
        print_banner()   
        create_project_folder()
    elif answers['option'] == MAIN_MENU_OPTIONS[1]:
        create_backup_function()
    elif answers['option'] == MAIN_MENU_OPTIONS[2]:
        not_implemented_yet()
    elif answers['option'] == MAIN_MENU_OPTIONS[3]:
        manage_projects_function()
    elif answers['option'] == MAIN_MENU_OPTIONS[4]:
        print("Goodbye :)")
        print("Leaving ...")
        return





if __name__ == "__main__":
    clear_screen()
    print_banner()
    main_menu()



