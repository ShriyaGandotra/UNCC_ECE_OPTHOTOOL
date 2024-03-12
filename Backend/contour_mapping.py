# Libraries
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

def run_code():
    """
    The main function used to run the code
    """
    image = get_image()

    # Get the modified image
    modified_image = get_layer_data(image_in=image)


def get_image():
    """
    Gets the current working directory and accesses the image
    :returns image: ndarray -> the segmented OCT scan used for measurement
    """
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filename = "Images/test_image.png"
    filepath = os.path.join(script_dir, filename)  # Segmented image filepath
    image = cv2.imread(filepath)
    return image


def get_jet_colormap():
    """
    Generate Jet colormap as a list of RGB tuples
    :returns colors: list -> List of RGB tuples representing the Jet colormap
    """
    cmap = plt.cm.jet
    norm = plt.Normalize(vmin=0, vmax=255)
    jet_colormap = cmap(norm(np.arange(256)))
    colors = [tuple((jet_colormap[i] * 255).astype(int)) for i in range(jet_colormap.shape[0])]
    return colors


def get_layer_data(image_in):
    """
    Stores the x and y coordinates of the different pixel values in each layer.
    Creates a dataframe for each color (layer)
    :param image_in (ndarray) -> the segmented OCT scan
    :returns new_image (ndarray) -> Modified image with contours
    """
    # Get Jet colormap colors
    colors_rgb = get_jet_colormap()

    # Convert image to RGB
    img_array = cv2.cvtColor(image_in, cv2.COLOR_BGR2RGB)

    # Initialize new image array with ones (white)
    new_img_array = np.ones_like(img_array) * 255

    # Iterate through each pixel and check if it matches any of the colors
    for color_rgb in colors_rgb:
        mask = np.all(img_array == color_rgb, axis=-1)
        new_img_array[mask] = [0, 0, 0]  # Set matching pixels to black

    # Create new image from the modified array
    new_image = cv2.cvtColor(new_img_array, cv2.COLOR_RGB2BGR)

    # Save the image with contours
    script_dir = os.path.dirname(os.path.realpath(__file__))
    output_folder = os.path.join(script_dir, 'Images')
    os.makedirs(output_folder, exist_ok=True)

    output_filepath = os.path.join(output_folder, 'contoured_image.png')
    cv2.imwrite(output_filepath, new_image)

    return new_image


# Executes the code
if __name__ == '__main__':
    run_code()

