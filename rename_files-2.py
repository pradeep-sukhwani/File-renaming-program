import os

def rename_file_names():
    # Get the files from folder
    get_file = os.listdir(r"C:\Python27\My-File\alphabet")
    #print get_file
    get_file_location = os.getcwd()
    os.chdir(r"C:\Python27\My-File\alphabet")
    print get_file_location

    # rename the files
    for file_name in get_file:
        print ("Old name - " + file_name)
        print ("Old name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(get_file_location)

rename_file_names()
