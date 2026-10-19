import shutil as s
s.copy2("SK.txt","def.txt")
s.copytree("SK.txt","def.txt")
s.move("def.txt","Python")
s.rmtree("def.txt")
s.make_archive("Archives","zip","SK.txt")
s.unpack_archive("Archives","Extracted folder")
format=s.get_archive_formats()
print(format)
unpack_format=s.get_unpack_formats()
print(unpack_format)


# # Write a program to create a complete folder backup with cuurent date 
# import datetime as dt
# d=dt.date.today()
# d=str(d)
# s.copytree("Basic",f"copy+{d}")

import os
print(os.getcwd())
import shutil as s

s.make_archive(
    "Focus_Website",      # ZIP file name
    "zip",                # Format
    r"D:\shahid"          # Full path to folder
)
