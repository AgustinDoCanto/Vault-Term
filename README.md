# Vault-Term

<br>

![Vault-Term-Logo](./documentation/img/Vault-Term-Logo.png "Vault Term Logo")

<br>
<hr>

## About it

Vault-Term is a productivity software to manage projects in the terminal in a more comfy way.

In Vault-Term you can create and manage your projects from the terminal, it is oriented towards productivity and note taking, but you can also write code with it.

It's based on the [Obsidian](https://obsidian.md/) philosophy and it's open source, so any contribuitions are welcome :)

<hr>

## Dependencies

The project was build it in [Python 3.12.5](https://www.python.org/) and it uses the following dependencies and projects:

### Figlet - [figlet](https://github.com/cmatsuoka/figlet)

This project uses **figlet** to generate ASCII art, specifically the Vault-Term logo. You can get more information about it by visiting the [project repository](https://github.com/cmatsuoka/figlet)

### Tabulate - [tabulate](https://pypi.org/project/tabulate/)

This project uses **tabulate** to create pretty ASCII tables embebed in terminal. You can get more info about tabulate [here](https://pypi.org/project/tabulate/).

### Inquirer - [inquirer](https://pypi.org/project/inquirer/)

This project uses **inquirer** to ease the flow into the Vault-Term menu. You can visit the [python project page](https://pypi.org/project/inquirer/) to get more information.


<hr>

## Installation

Vault-Term was created in the [Arch Linux](https://archlinux.org/) but it should work in every UNIX based system, like MacOs or Ubuntu.

### Before the installation - **python and figlet**

#### Installing figlet
Vault-Term uses [figlet](https://github.com/cmatsuoka/figlet) to display the "Vault-Term" logo so you must have successfully installed **figlet** in your system. To install it you can run the command:

In Arch Linux:
```bash
sudo pacman -Syu figlet
```

In Ubuntu:
```bash
sudo apt install figlet
```

#### Installing python

Also because the script was written in python you need it installed in your system, to install it you can run the command:


In Arch Linux:
```bash
sudo apt install python3
```

In Ubuntu:
```bash
sudo apt install python3
```

<br>

### Vault-Term Installation

With **figlet** successfully installed in your system now you can:

1. **Clone this repository:**

```bash
git clone https://github.com/AgustinDoCanto/Vault-Term.git
```

2. **Open the Vault-Term folder**

```bash
cd ./Vault-Term
```

3. **Run the install.sh script**

This script would create the python enviroment and install the **inquirer** and **tabulate** dependencies into it.

```bash
./install.sh
```

And that's all!! If all went well, you should have Vault-Term successfully installed in your machine, now when you want to run it you must run the **Vault.sh** script with:

```bash
./Vault.sh
```

It script should activate the virtual enviroment with the dependencies and run the "vault.py" file that it's the Vault-Term main file and it contains all the font code. Enjoy!

