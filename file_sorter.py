import os

import shutil 


download_folder = r"c:\Users\Irwin\Downloads"
dir_list = os.listdir(download_folder)
pdf_folder = "PDF"
pdf_format = ".pdf"
img_folder = "Image" 
img_format = ".jpg"
rar_folder = "RAR"
rar_format = ".zip"

rar_path = os.path.join(download_folder,rar_folder)
pdf_path = os.path.join(download_folder,pdf_folder)
img_path = os.path.join(download_folder,img_folder)

if img_folder not in dir_list:
    os.mkdir(img_path)

if pdf_folder not in dir_list:
    os.mkdir(pdf_path)

if rar_folder not in dir_list:
    os.mkdir(rar_path)


for files in dir_list:
    if files.endswith(".png") or files.endswith(".jpg") :
        file_path = os.path.join(download_folder,files)
        shutil.move(file_path,img_path)


for files in dir_list:
    if files.endswith(".pdf") or files.endswith(".docx"):
        file_path = os.path.join(download_folder,files)
        shutil.move(file_path,pdf_path)

for files in dir_list:
    if files.endswith(".zip"):
        file_path = os.path.join(download_folder,files)
        shutil.move(file_path,rar_path)
