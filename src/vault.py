import os
import time
import subprocess
import inquirer
from tabulate import tabulate
import stat


VAULT_MEDIA_PATH = "../Project-Vault/"

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
        else:
            print(f"This project folder name '{folder_name}' already exists.")

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
       
        table_data = []
        for file in files:
            file_path = os.path.join(path, file)
            file_stat = os.stat(file_path)
            permissions = stat.filemode(file_stat.st_mode)
            table_data.append([permissions, file])
        
       
        headers = ["Permissions", "Projects"]

        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

        # Prompt to ask for the folder name
        questions = [
            inquirer.Text('project_name', message="Enter the project name")
        ]

        # Get the user's input
        answers = inquirer.prompt(questions)
        project_name = answers['project_name']
        
        project_files = []
        for file in files:
            if file == project_name:
                try:
                    file_path = os.path.join(path, file)
                    project_files = os.listdir(file_path)
                    clear_screen()
                    print_banner()

                    for project in project_files:
                        file_path = os.path.join(path, file, project)
                        file_stat = os.stat(file_path)
                        permissions = stat.filemode(file_stat.st_mode)
                        table_data.append([permissions, project])


                    headers = ["Permissions", "Files"]
                    print(tabulate(table_data, headers=headers, tablefmt="github"))

                    # Prompt to ask for the project name to edit
                    questions = [
                        inquirer.Text('project_name_edit', message="Edit project")
                    ]

                    # Get the user's input
                    answers = inquirer.prompt(questions)
                    project_name_edit = answers['project_name_edit']

                    if project_name_edit == '':
                        main_menu()
                    else:
                        file_path = os.path.join(path, file, project_name_edit)
                        open_file_with_vim(file_path)

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
        not_implemented_yet()
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



