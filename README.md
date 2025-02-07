# Vault-Term

![Vault-Term-Logo](./docs/img/Vault-Term-Logo.png "Vault Term Logo")

---

## About Vault-Term

Vault-Term is a terminal-based productivity tool designed to help you manage projects in a more efficient and comfortable way.

With Vault-Term, you can create and manage projects directly from the terminal. While it is primarily oriented toward productivity and note-taking, you can also use it to write code.

Inspired by the [Obsidian](https://obsidian.md/) philosophy, Vault-Term is an open-source project—contributions are welcome! :)

---

## Dependencies

Vault-Term is built with [Python 3.12.5](https://www.python.org/) and relies on the following dependencies:

### [Figlet](https://github.com/cmatsuoka/figlet)

Vault-Term uses **Figlet** to generate ASCII art, particularly for the Vault-Term logo. More details can be found in the [Figlet repository](https://github.com/cmatsuoka/figlet).

### [Tabulate](https://pypi.org/project/tabulate/)

Vault-Term utilizes **Tabulate** to create structured and readable ASCII tables within the terminal. More information is available on the [Tabulate PyPI page](https://pypi.org/project/tabulate/).

### [Inquirer](https://pypi.org/project/inquirer/)

Vault-Term uses **Inquirer** to streamline navigation within its menu system. You can learn more about it on the [Inquirer PyPI page](https://pypi.org/project/inquirer/).

### [Vim](https://www.vim.org/)

Vault-Term integrates **Vim** as the default text editor for managing project files. You can install it by following the instructions in the [Vim documentation](https://www.vim.org/download.php).

---

## Installation

Vault-Term was developed on [Arch Linux](https://archlinux.org/), but it should work on any UNIX-based system, including macOS and Ubuntu.

### Prerequisites: Python and Figlet

#### Installing Figlet
Vault-Term requires [Figlet](https://github.com/cmatsuoka/figlet) for ASCII art generation. Install it using the following commands:

**Arch Linux:**
```bash
sudo pacman -Syu figlet
```

**Ubuntu:**
```bash
sudo apt install figlet
```

#### Installing Python

Ensure that Python 3 is installed on your system:

**Arch Linux:**
```bash
sudo pacman -Syu python3
```

**Ubuntu:**
```bash
sudo apt install python3
```

---

### Installing Vault-Term

Once the prerequisites are installed, follow these steps to set up Vault-Term:

1. **Clone the repository:**
```bash
git clone https://github.com/AgustinDoCanto/Vault-Term.git
```

2. **Navigate to the Vault-Term directory:**
```bash
cd Vault-Term
```

3. **Run the installation script:**
```bash
./install.sh
```

This script sets up a Python virtual environment and installs the required dependencies (**Inquirer** and **Tabulate**).

---

## Running Vault-Term

Once installed, launch Vault-Term by running:
```bash
./Vault.sh
```

This script activates the virtual environment and executes `vault.py`, the main script that powers Vault-Term. Enjoy!
