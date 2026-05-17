import os

FOLDER_NAME = "./my_notes"

if not os.path.exists(FOLDER_NAME):
    os.makedirs(FOLDER_NAME)
    print(f"Create a new folder at : {FOLDER_NAME}")
    
else:
    print(f"Folder {FOLDER_NAME}")
    
print("\n--- Scanning & Reading Notes ---")
files = os.listdir(FOLDER_NAME)

if len(files) == 0:
    print("The folder is empty, drop a text file in there!")
    
for filename in files:
    if filename.endswith(".txt"):
        print(f"\n Found file: {filename}")
        
        file_path = os.path.join(FOLDER_NAME, filename)
        with open(file_path, "r", encoding ="utf-8") as f:
            file_content = f.read()
            print(f" Content inside: {file_content}")
            
            
        
        
    
