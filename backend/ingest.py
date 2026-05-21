import os

from backend.tools.pdf_reader import extract_pdf_text

def load_documents(folder_path: str):
    
    all_text =""
    
    for file in os.list.dir(folder_path):
        
        path = os.path.join(folder_path, file)
        
        if file.endswith(".txt"):
            
            with open(path, "r", encoding ="utf-8") as f:
                all_text += f.read()
                
        elif file.endswith(".pdf"):
            pdf_text= extract_pdf_text(path)
            all_text += pdf_text +  "\n"
    return all_text


