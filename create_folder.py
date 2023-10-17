import os
import shutil


def create_folder(folder_names):
    """Takes a list of folder names as argument and creates folders in your current working directory!
    Deletes and recreates folders if they exists"""
    path = f'./{folder_names}'
    for path in folder_names:
        try:
            os.makedirs(path)
            print("Folder %s created" % path)
        except FileExistsError:
            shutil.rmtree(path)
            os.makedirs(path)
            print("Deleted and remade folders %s! " % path)



if __name__ == "__main__":
    list = ['test1','test2', 'test4']
    create_folder(list)