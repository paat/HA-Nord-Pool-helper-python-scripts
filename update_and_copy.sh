#!/bin/bash

#You need to run this script in the python_scripts/{my-repo-name}/ directory
#make sure to chmod +x update_and_copy.sh

# Pull the latest changes
git pull

# Copy .py files from python_scripts to the parent directory, excluding __init__.py
find python_scripts -maxdepth 1 -name "*.py" ! -name "__init__.py" -exec cp {} . \;