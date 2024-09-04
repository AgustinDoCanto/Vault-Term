#!/bin/sh

#  ____                            _                 _           
# |  _ \  ___ _ __   ___ _ __   __| | ___ _ __   ___(_) ___  ___ 
# | | | |/ _ \ '_ \ / _ \ '_ \ / _` |/ _ \ '_ \ / __| |/ _ \/ __|
# | |_| |  __/ |_) |  __/ | | | (_| |  __/ | | | (__| |  __/\__ \
# |____/ \___| .__/ \___|_| |_|\__,_|\___|_| |_|\___|_|\___||___/
#            |_|                                                 
#

main(){
    cd ./src/
    # Creating the python virtual enviroment
    python -m venv ./venv

    # Activating the python virtual enviroment
    source ./venv/bin/activate

    # Installing inquirer into the enviroment
    pip install inquirer
    
    # Installing tabulate into the enviroment
    pip install tabulate
}

main
