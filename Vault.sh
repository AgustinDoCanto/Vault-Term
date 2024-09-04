#!/bin/sh

# __     __          _ _      _____                   
# \ \   / /_ _ _   _| | |_   |_   _|__ _ __ _ __ ___  
#  \ \ / / _` | | | | | __|____| |/ _ \ '__| '_ ` _ \ 
#   \ V / (_| | |_| | | ||_____| |  __/ |  | | | | | |
#    \_/ \__,_|\__,_|_|\__|    |_|\___|_|  |_| |_| |_|
#                                                     

# IMPORTANT! You must run the "install.sh" script before running this script, if not it would not work.

main(){
   cd ./src

   # Activating the python virtual enviroment
   source ./venv/bin/activate

   # Running the main Vault-Term script
   python ./vault.py
}

main

