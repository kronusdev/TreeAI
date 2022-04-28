#!/bin/bash

until python3 treeai.py 
do
    echo "Restarting...."
    sleep 2
done