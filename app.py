import os

FOLDER_NAME = "./my_notes"

if not os.path.exists(FOLDER_NAME):
    os.makedirs(FOLDER_NAME)
    print(f"📁 Created a new folder at: {FOLDER_NAME}")
    print("👉 Put a couple of test .txt files in there before you go to work!")
else:
    print(f"✅ Folder {FOLDER_NAME} is ready.")

print("\n--- Scanning for Notes ---")
files = os.listdir(FOLDER_NAME)
if len(files) == 0:
    print("Folder is empty, no data to structure yet!")
    for filename in files:
        if filename.endswith(".txt"):
            print(f"Found data: {filename}")
            
            


    