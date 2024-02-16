# OCT Layer Measurement Tool
# Authors: Lauren Bourque

# Libraries
from PIL import Image
import os
import numpy as np
import pandas as pd


def run_code():
    """
    The main function used to run the code
    """
    image: Image = get_image()

    # Get the calculated thicknesses
    layer_thicknesses = calculate_thicknesses(image_in=image)

    print(layer_thicknesses)


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


def calculate_thicknesses(image_in: Image):
    """
    Stores the x and y coordinates of the different pixel values in each layer.
    Creates a dataframe for each color (layer)
    :param image_in (Image) -> the segmented OCT scan
    :returns white_pixel_arrays (list) -> A list of 9 arrays containing white pixel coordinates.
    """
    # List of RGB colors to get pixel data from
    colors = [
        '#e4ff12',  # Color 1 (Yellow)
        '#15ffe1',  # Color 2 (Teal)
        '#ff9400',  # Color 3 (Orange)
        '#0000ff',  # Color 4 (Darker Blue)
        '#ff1d00',  # Color 5 (Red)
        '#7cff79',  # Color 6 (Green)
        '#0080ff',  # Color 7 (Sky Blue)
        '#7f0000',  # Color 8 (Burgundy)
    ]

    # Corresponding English names for each color
    layer_names = [
        'Nerve Fiber Layer',
        'GCL + IPL',
        'Inner Nuclear Layer',
        'Outer Plexiform Layer',
        'Outer Nuclear Layer',
        'Ellipsoid Zone',
        'Retinal Pigment Epithelium',
        'Choroid'
    ]

    # Convert colors to RGB format
    colors_rgb = [tuple(int(color[i:i + 2], 16) for i in (1, 3, 5)) for color in colors]

    # Load image and convert to numpy array
    img_array = np.array(image_in)

    # Remove alpha channel if present
    if img_array.shape[-1] == 4:
        img_array = img_array[:, :, :3]

    # Initialize dictionary to store color information
    color_info = {}

    # Get image width and height
    img_width, img_height = img_array.shape[1], img_array.shape[0]

    # Iterate over each color
    for idx, color_rgb in enumerate(colors_rgb):
        # Check if any pixel matches the current color
        mask = np.all(img_array == color_rgb, axis=-1)
        # Calculate total number of pixels for the color
        total_pixels = np.sum(mask)
        # Divide by image width to normalize by image size
        pixels_per_width = total_pixels / img_width
        # Divide by image height and multiply by 6000 to get layer thickness in micrometers (assumes image is 6mm by 6mm)
        layer_thickness = (pixels_per_width / img_height) * 6000
        # Store color information including hexadecimal value and layer thickness
        color_info[f'Color_{idx+1}'] = {
            'Layer': layer_names[idx],  # Adding the B Scan layer names
            'RGB': color_rgb,
            'Hex': colors[idx],  # Adding the hexadecimal value
            'TotalPixels': total_pixels,
            'PixelsPerWidth': pixels_per_width,
            'LayerThickness': layer_thickness  # Adding the layer thickness
        }

    # Convert color information to DataFrame
    color_df = pd.DataFrame.from_dict(color_info, orient='index')

    return color_df


# Executes the code
if __name__ == '__main__':
    run_code()
