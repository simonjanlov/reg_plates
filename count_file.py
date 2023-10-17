import os

def count_files(folder_path,file_extension):
    """Takes a folder path and a file extension as arguments and count the number of files with
    said file extension in the folder path"""
    dir_path = folder_path
    files = [dir_path + f for f in os.listdir(dir_path) if f.endswith(f'{file_extension}')]
    print("number of files in directory: ", len(files))


if __name__ == "__main__":
    count_files('c:\\Users\\henry\\Documents\\projekt\\machine learning\\tool_box','.png')