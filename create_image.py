import matplotlib.pyplot as plt

def create_images(reg_nr, save_path):
    """Takes a first name, surname and a filename as arguments. Adds first name surname to the image and saves it as the given filename"""
    # to do: check if includes the space and the rest is all alphanumerical
    # do this with try / except instead
    if len(reg_nr) == 7:
        plt.figure(figsize=(10,4))
        ax = plt.gca()
        plt.axis('off')
        im = plt.imread("empty_sign.png")
        plt.text(100, 110, reg_nr, fontsize=120)

        plt.imshow(im)
        plt.tight_layout()
        plt.savefig(save_path)
        # plt.show()

    else:
        print("Invalid plate number")    
    
    
    # try:
    #     len(reg_nr) != 7 
    #     raise Exception("Invalid plate number")
    
    # except Exception:
    #     plt.figure(figsize=(10,4))
    #     ax = plt.gca()
    #     plt.axis('off')
    #     im = plt.imread("empty_sign.png")
    #     plt.text(100, 110, reg_nr, fontsize=120)

    #     plt.imshow(im)
    #     plt.tight_layout()
    #     plt.savefig(save_path)
    #     # plt.showw()

if __name__ == "__main__":
    create_images('ABC 123', 'test_plate.png')