import os

from tools.pdf_reader import extract_pdf_text

def load_documents(folder_path: str):
    
    all_text =""
    
    for file in os.listdir(folder_path):
        
        path = os.path.join(folder_path, file)
        
        if file.endswith(".txt"):
            
            with open(path, "r", encoding ="utf-8") as f:
                all_text += f.read()
                
        elif file.endswith(".pdf"):
            pdf_text= extract_pdf_text(path)
            all_text += pdf_text +  "\n"
    return all_text

if __name__ == "__main__":
    text = load_documents("backend\\data")

    print("Total characters:", len(text))
    print(text[:500])


