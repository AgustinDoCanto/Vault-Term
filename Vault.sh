#!/bin/sh

main(){
   cd ./src
   # python -m venv ./venv
   source ./venv/bin/activate
   python ./vault.py
}

main

