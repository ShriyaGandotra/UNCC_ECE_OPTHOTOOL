# Contour Mapping Tool
# Authors: Lauren Bourque

# Libraries
from PIL import Image
import os
import numpy as np


def run_code():
    """
    The main function used to run the code
    """
    image: Image = get_image()

    # Get the modified image
    modified_image = get_layer_data(image_in=image)


def get_image():

    """
    Gets the current working directory and accesses the image
    :returns image: Image -> the segmented OCT scan used for measurement
    """
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filename = "Images/test_image.png"
    filepath = os.path.join(script_dir, filename)  # Segmented image filepath
    image = Image.open(filepath)
    return image


def get_layer_data(image_in: Image):
    """
    Stores the x and y coordinates of the different pixel values in each layer.
    Creates a dataframe for each color (layer)
    :param image_in (Image) -> the segmented OCT scan
    :returns layers (list[pd.Dataframe]) -> A list of 8 DataFrames representing each layer.
    Each DataFrame contains the x and y coordinates for all the pixels in this layer
    """
    # List of RGB colors to get pixel data from
    colors = [
        '#00007f',  # Background color (Dark Blue)
        '#e4ff12',  # Color 1 (Yellow)
        '#15ffe1',  # Color 2 (Teal)
        '#ff9400',  # Color 3 (Orange)
        '#0000ff',  # Color 4 (Darker Blue)
        '#ff1d00',  # Color 5 (Red)
        '#7cff79',  # Color 6 (Green)
        '#0080ff',  # Color 7 (Sky Blue)
        '#7f0000',  # Color 8 (Burgundy)
    ]

    # Convert colors to RGB format
    colors_rgb = [tuple(int(color[i:i + 2], 16) for i in (1, 3, 5)) for color in colors]

    # Load image and convert to numpy array
    img_array = np.array(image_in)

    # Remove alpha channel if present
    if img_array.shape[-1] == 4:
        img_array = img_array[:, :, :3]

    # Initialize new image array with ones (white)
    new_img_array = np.ones_like(img_array) * 255

    # Iterate through each pixel and check if it matches any of the colors
    for color_rgb in colors_rgb:
        mask = np.all(img_array == color_rgb, axis=-1)
        new_img_array[mask] = [0, 0, 0]  # Set matching pixels to black

    # Create new image from the modified array
    new_image = Image.fromarray(new_img_array.astype(np.uint8), 'RGB')

    # Save the image with contours
    script_dir = os.path.dirname(os.path.realpath(__file__))
    output_folder = os.path.join(script_dir, 'Images')
    os.makedirs(output_folder, exist_ok=True)

    output_filepath = os.path.join(output_folder, 'zeroed_image.png')
    new_image.save(output_filepath)

    return new_image


# Executes the code
if __name__ == '__main__':
    run_code()

