
import os
import shutil

src = r'C:\Users\Owner\Desktop\PythonZip\PyUnzip01\child_dir\unzip_test2'
dest = r'C:\Users\Owner\Desktop\PythonZip\PyUnzip01\child_dir'
pdir = '../PyUnzip01'

os.replace(r"C:\Users\Owner\Desktop\PythonZip\PyUnzip01\child_dir\unzip_test2.zip", r"C:\Users\Owner\Desktop\PythonZip\PyUnzip01\unzip_test2.zip")

for root, subdirs, files in os.walk(src):
    for file in files:
        path = os.path.join(root, file)
        shutil.move(path, dest)

os.replace(r"C:\Users\Owner\Desktop\PythonZip\PyUnzip01\unzip_test2.zip", r"C:\Users\Owner\Desktop\PythonZip\PyUnzip01\child_dir\unzip_test2.zip")
