# AUTHOR: SHRIYA GANDOTRA
# This Python script includes a function calculate_thicknesses that processes 
# segmented OCT images to calculate the thickness of retinal layers. 
# Refer to Backend code for original function

import pandas as pd
import numpy as np
from tkinter import *
from PIL import Image

def calculate_thicknesses(filepath, layer1: int, layer2: int):
    """
    Stores the x and y coordinates of the different pixel values in each layer.
    Creates a dataframe for each color (layer)
    :param image_in (Image) -> the segmented OCT scan
    :returns white_pixel_arrays (list) -> A list of 9 arrays containing white pixel coordinates.
    """

    image = Image.open(filepath)

    # List of RGB colors to get pixel data from
    colors = [
        '#feff01',  # Color 1 (Yellow)
        '#02fffe',  # Color 2 (Teal)
        '#ff8000',  # Color 3 (Orange)
        '#0000ff',  # Color 4 (Darker Blue)
        '#ff0000',  # Color 5 (Red)
        '#82ff7e',  # Color 6 (Green)
        '#0080ff',  # Color 7 (Sky Blue)
        '#800000',  # Color 8 (Burgundy)
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
    img_array = np.array(image)

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

    # Select the relevant rows based on indices layer1 and layer2
    if layer1 > layer2:
        selected_layers = color_df.iloc[layer2 - 1:layer1]
    else:
        selected_layers = color_df.iloc[layer1 - 1:layer2]

    # Sum the layer thickness values
    total_thickness = str(selected_layers['LayerThickness'].sum()) + " um"

    print(total_thickness)

    return total_thickness

