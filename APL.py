from PIL import Image
import numpy as np


def calculate_apl(filename):
    """Calculate the average picture level (APL) from an image.

    Keyword arguments:
    filename -- path of image
    """
    # load the image
    image = Image.open(filename)

    # convert image to numpy array
    data = np.asarray(image)

    # calculate APL slicing is to remove the 255 at the end of each pixel array so entire array can be averaged
    APL = np.average(data[:, :, :3]) / 255

    return APL


if __name__ == "__main__":
    # prompt user for image
    filepath = input("Enter the file name (including extension) of the image: ")

    result = calculate_apl(filepath)
    print("The APL is ", result)
