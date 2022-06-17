import shutil
import os
from platform import system
operating_system = system()
files = []
file_types = {
    "Document": [".docx", ".odt"],
    "Pdf": ".pdf",
    "Image": [".jpg", ".png"],
    "Archive":[".tar", ".rar", ".zip", ".7z"]

    
    
    
    }
#change directory to desktop
if operating_system == "Windows":
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    os.chdir(desktop)
else:  
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    os.chdir(desktop)

#get all the things from desktop
for filename in os.listdir(desktop):
    if os.path.isfile(filename): #check if it is a file
        files.append(filename)



def organize_file(file, destination):
    try:
        if os.path.exists(destination):
            shutil.move(file,destination)
        else:
            os.mkdir(destination)
            shutil.move(file,destination)
    except:
        #print(f"There was an error with organizing {file}")
        pass




#iterate over the files
for file in files:
    #get file extension)
    extension = os.path.splitext(file)[1]
    #print(extension)
    if extension == ".url" or extension == '.lnk':
        continue
    if extension in file_types["Document"]:
        organize_file(file,"Documents")
    if extension in file_types["Pdf"]:
        organize_file(file,"PDFs")
    if extension in file_types["Image"]:
        organize_file(file,"Images")
    if extension in file_types["Archive"]:
        organize_file(file,"Archives")
    else:
        organize_file(file,"Other Files")



