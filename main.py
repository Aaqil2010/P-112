import os
import shutil

from_dir = "C:/Users/sahil/Downloads"
to_dir = "C:/Users/sahil/OneDrive/Desktop/Downloads_Files"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name,ext = os.path.splitext(file_name)
    if ext == "" :
        continue
    if ext in [ ".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir+"/"+file_name
        path2 = to_dir+"/"+"document_files"
        path3 = to_dir+"/"+"document_files"+"/"+file_name
         
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else :
            os.makedirs(path2)
            shutil.move(path1,path3)

