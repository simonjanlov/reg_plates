import joblib as jb
import os
import numpy as np

def save_to_file(object,file_path):
    """Takes an object and a file path as arguments and saves object in the file path
    using joblib.dump"""
    file_path = file_path + '.pkl'
    jb.dump(object,file_path)


def load_file(file_path):
    """takes a file path as argument and load said file in to a variable using joblib.load"""
    file = jb.load(file_path)
    print(file)
    return file
    


if __name__ == "__main__":
    array = np.array([1,2,3,4,5,6,7,8,3])
    save_to_file(array,'c:\\Users\\henry\\Documents\\projekt\\machine learning\\tool_box\\test')
    load_file('c:\\Users\\henry\\Documents\\projekt\\machine learning\\tool_box\\test.pkl')