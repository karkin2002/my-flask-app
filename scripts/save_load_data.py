__author__ = "Kaya Arkin"
__date__ = "21/04/2024"

from os import path as osPath
from json import load, dump
from scripts.logger import Logger

def save_json(path: str, data: dict, replace: bool = False):

    """Saves dict as a json file (include .json)

    Raises:
        Exception: File already exists
    """  
        
    if not osPath.isfile(path):
        with open(path, 'w') as json_file:
            dump(data, json_file, indent=3)
        
        Logger.log_info(f"Saved '{data}' as '{path}'.")
    
    else:
        
        Logger.log_warning(f"'{path}' already exists.")
        
        if replace:
            with open(path, 'w') as json_file:
                dump(data, json_file, indent=3)
            
            Logger.log_info(f"Overwritten '{path}'.")



def load_json(path: str) -> dict:

    """Loads dictonary saved on a json file based on the path 

    Returns:
        dict: dictonary loaded from file
    """    

    if osPath.isfile(path):
        with open(path, 'r') as json_file:
            dict = load(json_file)

        Logger.log_info(f"Loaded '{path}'.")
        
        return dict
        
    else:
        Logger.log_error(f"'{path}' doesn't exists.")
        save_json(path, {})
        return {}