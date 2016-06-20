import os

def rename_file_names():
    # (1) Get the file names from a folder
    file_list = os.listdir(r"C:\Python27\My-File\prank")
    print file_list
    saved_path = os.getcwd()
    print "My working directory " + saved_path
    os.chdir (r"C:\Python27\My-File\prank")
    
    # (2) Rename the file name
    for file_name in file_list:
        print "Old Name - " + file_name
        print "New Name - " + file_name.translate(None, "0123456789")
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_file_names()