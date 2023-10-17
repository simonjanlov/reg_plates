import matplotlib.pyplot as plt

def create_images(reg_nr):
    """Takes a first name, surname and a filename as arguments. Adds first name surname to the image and saves it as the given filename"""
    plt.figure(figsize=(10,4))
    im = plt.imread("empty_sign.png")
    plt.text(100,60,reg_nr)

    plt.imshow(im)
    # plt.savefig(filename)
    plt.show()

if __name__ == "__main__":
    create_images('ABC 123')
