import os

folder = "C:\\Users\\LENOVO\\OneDrive\\Masaüstü\\obj" # change the path
os.chdir(folder)

def change_text_file(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    with open(file_path, "r+") as fi:
        lines = fi.readlines()
        for item in lines:
            fi.seek(0)
            fi.truncate()
            i = item[0:2] # you can customize this
            new_text = text.replace(i, "0") # you can customize this
            
            fi.writelines(new_text)
                
for file in os.listdir():
    if file.endswith(".txt"):
        file_path = f"{folder}\{file}"
  
        change_text_file(file_path)
