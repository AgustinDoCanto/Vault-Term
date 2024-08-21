#!/bin/sh

main(){
    cd ./src/
    python -m venv ./venv
    source ./venv/bin/activate
    pip install inquirer
    pip install tabulate
}

main
