import numpy as np
from PIL import Image

def print_image_array(image_path):
    """Takes an image path as an argument, saves the image as an array and prints it"""
    image = Image.open(image_path)
    data = np.asarray(image)
    print(data)
    return data


if __name__ == "__main__":
    print_image_array('test_image.jpg')