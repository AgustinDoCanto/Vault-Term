# Vault-Term Documentation

<br>

![Vault-Term-Logo](./img/Vault-Term-Logo.png "Vault Term Logo")

<br>
<hr>

## Notes of the software

All the changes are made in the filesystem of your machine so you can move and create folders as you wish for create or delete projects or create a new Project-Vault but the goal of this sofware is to simplify that process oriented to notetaking and productivity. 

Also the software is in a development fase so may not have all the bounds checks and validations so made changes on your own risk.

## Definitions

### What is the Project-Vault?

The Project-Vault is the central piece of the software and is created when you create your first Project. Is the folder where all the Projects are saved.

For now you can only have one Project-Vault where Vault-Term was installed but you can create how many backups you want in another directorys.

To create backups of the Project-Vault pick on the "Create Backup" option in the main menu.


### What is a Project?

A Project is a folder created into the Project-Vault and it contains all the .md files (or with another extension), 

The Projects would be created into the Project-Vault and is basically a folder where you would create and save all the .md files, or files with another extension, for after edition or consulting.  


### Project-Vault and Projects structure tree

The Project-Vault tree should be like this:

![Project-Vault, Projects and files tree](./img/Projects-And-Project-Vault-Diagram.png "Project-Vault, Projects and files tree")


## How to use

Once you has successfully installed Vault-Term run the "Vault.sh" with ./Vault.sh script to launch the main program.

## Main menu

After you ran the "Vault.sh" script you would see the main menu:

![Vault Term Main menu](./img/main-menu.png.png "Vault Term Main menu")

For now the following options are available:

- Create Project
- Create Backup
- Set Media Path
- Manage projects
- Exit

Use the arrow keys up and down to choose an option.

## Options description

### Create Project

To Create a new Project pick the "Create Project" option in the main menu. It would ask you for a project name and then creates a new project with that name in the Project-Vault.

To Manage your Projects see the "Manage Projects" option.

If you choose this option for error click the enter key without writing anything and that will take you to the main menu.


![Create Project option selected](./img/CreateProject/vault-term-create-project-option.png "Create Project option selected")


![Create Project enter name](./img/CreateProject/create-project-option-selected.png "Create Project enter name")

### Create Backup

The "Create Backup" option creates a backup of the Project-Vault in the target directory path.

This option creates a folder labeled "Projet-Vault" in the target path and it another "Project-Vault" exists in the target it will relabel the Vault with an a N suffix.


"Create Backup" option in the main menu:

![Create Backup option](./img/CreateBackup/create-backup-option-main-menu.png "Create Backup option")

Into the "Create Backup" option:

![Create Backup option selected](./img/CreateBackup/create-backup-option-selected-main-menu.png "Create Backup option selected")


### Set Media Path

![Set Media Path option](./img/SetMediaPath/set-media-path-main-menu-option.png "Set Media Path option")

When you create the first Project, Vault-Term creates a Project-Vault in the media path that you set. 

By default the media path is setted in the path that is installed Vault-Term but with this option you can create a vault in another path that could be in a live media or in the current device but in another directory. So you can work and create Projects into a live media and carry with these wherever you like.

![Set Media Path option selected](./img/SetMediaPath/set-media-path-option-selected.png "Set Media Path option selected")

For now the media path is restored to the current path that is installed Vault-Term every time you restart but in the future it could be changed.




### Manage projects

### Exit


