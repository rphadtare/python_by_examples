# This file provides demo of OS module

import os

file_path = ""


def getDetails():
    # to get OS name
    print(f"OS name: {os.name}")

    # to get CWD
    print(f"Current working dir: {os.getcwd()}")


def createDir():
    global file_path
    file_path = os.getcwd() + "/os_demo/"
    is_dir_exist = os.access(file_path, os.F_OK)
    print("directory {} exist: {}".format(file_path, is_dir_exist))
    # to create new dir
    if not is_dir_exist:
        print(f"Creating dir {file_path}")
        os.mkdir(file_path)


def deleteDir():
    global file_path
    print(f"Deleting dir {file_path}")
    os.rmdir(file_path)


def read_or_write(operation_name):
    global file_path

    if operation_name == "w":
        file = open(file_path + "test.txt", "w")
        print("File obj:", file)
        print("Writing info into file..")
        file.write("This is OS module demo!!")
        file.close()
    else:
        file = open(file_path + "test.txt", "r")
        print(file.__dict__)
        print("File obj:", file)
        print("Reading info from file..")
        info = file.read()
        print(info)
        file.close()


def checkAccess():
    global file_path
    txt_file_path = file_path + "test.txt"
    print(f"Access to file path {txt_file_path}: {os.access(txt_file_path, os.F_OK)}")
    print(f"Access to read file {txt_file_path}: {os.access(txt_file_path, os.R_OK)}")
    print(f"Access to write into file {txt_file_path}: {os.access(txt_file_path, os.W_OK)}")
    print(f"Access to execute file {txt_file_path}: {os.access(txt_file_path, os.X_OK)}")


def renameDir():
    global file_path
    # renaming existing dir
    print(f"Existing dir: {file_path}")
    new_dir = file_path.replace("os_demo", "os_rename_demo")
    print(f"New dir: {new_dir}")
    os.rename(file_path, new_dir)


def main():
    getDetails()
    createDir()
    read_or_write("r")
    checkAccess()
    renameDir()


if __name__ == "__main__":
    main()
