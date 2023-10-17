import os
import shutil
import string


def create_folders(path):
    
    folder_names = list(string.ascii_uppercase)
    remove = ['I','V','Q']
    for char in remove:
        folder_names.remove(char)
        
    for name in folder_names:
        try:
            os.makedirs(path + name)
        except FileExistsError:
            shutil.rmtree(path + name)
            os.makedirs(path + name)

if __name__=='__main__':

    # path = "C:\projekt\MachineLearning\create_folders\\"
    
    create_folders('.\\test_folders\\')

