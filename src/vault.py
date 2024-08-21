import os
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
    
    # Define the path where the folder will be created
    base_path = "../Project-Vault/"
    full_path = os.path.join(base_path, folder_name)
    
    # Create the folder if it doesn't exist
    if not os.path.exists(full_path):
        os.makedirs(full_path)
        print(f"Project '{folder_name}' created successfully.")
    else:
        print(f"This project folder name '{folder_name}' already exists.")

def main_menu():
    questions = [
        inquirer.List('option',
                      message="Option menu",
                      choices=['Create Project', 'Open Project', 'Exit'],
                     ),
    ]
    
    answers = inquirer.prompt(questions)
    if answers['option'] == 'Create Project':
        clear_screen()
        print_banner()   
        create_project_folder()
    elif answers['option'] == 'Open Project':
        clear_screen()
        print_banner()   
        print("You choose option 2")
    elif answers['option'] == 'Exit':
        print("Goodbye :) ...")
        print("Leaving ...")
        return

    
if __name__ == "__main__":
    clear_screen()
    print_banner()
    main_menu()



