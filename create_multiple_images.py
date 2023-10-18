from create_image import create_image
from create_folder import create_folders 
from generate_reg_no import generate_reg_nr
from config import *


def create_multiple_images(amount):
    create_folders(FOLDER_PATH)
    
    for i in range(amount):
        file_name = str(i + 1) + '.png'
        current_plate_number = generate_reg_nr()
        first_letter = current_plate_number[0]
        full_path = FOLDER_PATH + first_letter + '\\' + file_name
        create_image(current_plate_number, full_path)



if __name__=='__main__':
    create_multiple_images(5)
