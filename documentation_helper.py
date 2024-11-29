from inspect import getmembers, isfunction
from importlib import import_module
import os
import sys

PATH = "."

def print_all_functions():
    """ Outputs a neat list of all functions for each module in the Path. """
    
    # Creates a list of all files to be imported and have their functions printed 
    exempt_filenames = ['documentation_helper']

    all_filenames = get_python_filenames() # Excluding 'main.py'
    for filename in exempt_filenames:
        all_filenames.remove(filename)

    # Iterates through list of relevant files and neatly prints their functions
    for filename in all_filenames:
        current_module = import_module(filename, package=None)
        module_members = getmembers(current_module, isfunction)
        print(f"{filename}: ")
        for member in module_members:
            print(" - " + member[0])


def get_python_filenames():
    """ Returns a list of all python filenames specified in `PATH`, i.e. excluding 'main.py'. """
    python_files = []
    for item in os.scandir(PATH):
        split = item.name.split('.')
        if len(split) != 1:
            if (split[1] == "py") and (split[0] != 'main'):
                python_files.append(split[0])
    return python_files


def string_to_array(input_string:str) -> list:
    split_string = input_string.split('|')
    output = []
    for element in split_string:
        output.append(element.strip())
    return output
