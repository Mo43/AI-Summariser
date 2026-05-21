import os
from dotenv import load_dotenv
from smolagents import CodeAgent, InferenceClientModel, tool

#api key
load_dotenv()

@tool
def read_my_folder(folder_name: str) -> str:
    """
    A tool that opens a specific folder and reads the files inside it
    
    Args:
        folder_name: The name of the folder you want to look inside.
    """
    
    #1. if folder doesn't exist stop and tell us
    
    if not os.path.exists(folder_name):
        return  f"Cannot find {folder_name}"
    
    text_data = ""
    #2. loop through every file in folder 
    for file in os.listdir(folder_name):
        if file.endswith('.txt'):
            path = os.path.join(folder_name, file)
            
            with open(path, 'r', encoding='utf-8') as f:
                text_data += f"\n--- {file} ---\n" + f.read()
    return text_data
