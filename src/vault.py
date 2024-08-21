import os
import time
import subprocess
import inquirer

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
        base_path = "../Project-Vault/"
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
        not_implemented_yet() 
    elif answers['option'] == MAIN_MENU_OPTIONS[4]:
        print("Goodbye :)")
        print("Leaving ...")
        return





if __name__ == "__main__":
    clear_screen()
    print_banner()
    main_menu()



