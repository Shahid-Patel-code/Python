import os 
'''current_dir=os.getcwd
print(current_dir) 
item=os.listdir(current_dir)
for i in item:
    print(f"-{i}")'''

# use 
f'''older="A"
subfolder="B"
filename="C"
Path=os.path.join(folder,subfolder,filename)
'''
# creating a file form command
'''os.mkdir("ab")
'''

# creating a new derectry 
current=os.getcwd()
'''new=os.path.join(current,"folder")
if os.path.exists(new):
    print("File Already exist")
else:
    os.mkdir(new)
'''

# renaming a directry
'''rename=os.path.join(current,"rename")
if os.path.exists(rename):
    print("Folder already exist")
else:
    os.rename("folder" ,rename)'''

# multiple directries

nested=os.path.join(current,"my","your","shy")
'''if os.path.exists(nested):
    print("Path already exist")
else:
    os.makedirs(nested)
    print("Directries created")'''

# removing the directries

"""os.rmdir(nested)
os.removedirs(nested)"""

# opning a file 
'''os.system("notepad")'''

# user info 
print(os.getlogin())
print(os.name)

# """os.path.isfile=used to get true or False if file exist 
# os.path.isdir= use get true and false answer if exist
# """

# changing a directry 
'''
curr=os.chdir("you")
print(os.getcwd())
'''

num=int(input("Enter number of student: "))
for i in range(num):
    n=input(f"Enter Name of {i+1} student: ")
    new=os.getcwd()
    new1=os.path.join(new,n)
    if os.path.exists(new1):
        print("Already exist")
        continue
    else:
        os.mkdir(new1)



import zipfile
folder_path = "shahid"
zip_path = "my_folder.zip"

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path,
                       os.path.relpath(file_path, folder_path))

print("Folder zipped successfully!")
