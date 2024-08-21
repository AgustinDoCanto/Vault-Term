#!/bin/sh

main(){
    cd ./src
    python -m venv ./venv
    pip install inquirer
}

main
