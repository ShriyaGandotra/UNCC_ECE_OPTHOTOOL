# AUTHOR: SHRIYA GANDOTRA
# This Python script includes a function calculate_thicknesses that processes 
# segmented OCT images to calculate the thickness of retinal layers. 
# Refer to Backend code for original function

import pandas as pd
import numpy as np
from tkinter import *
from PIL import Image

def calculate_thicknesses(image_data, layer1: int, layer2: int):
    """
    Calculates the thicknesses of specified layers within an image region.
    :param image_data (numpy.ndarray): The cropped segmented OCT scan image data.
    :param layer1 (int): Start layer index.
    :param layer2 (int): End layer index.
    :returns (str): Total thickness of the layers from 'layer1' to 'layer2'.
    """
    # Define the color codes for different layers
    colors = [
        '#feff01',  # Color 1 (Yellow)
        '#02fffe',  # Color 2 (Teal)
        '#ff8000',  # Color 3 (Orange)
        '#0000ff',  # Color 4 (Blue)
        '#ff0000',  # Color 5 (Red)
        '#82ff7e',  # Color 6 (Green)
        '#0080ff',  # Color 7 (Sky Blue)
        '#800000',  # Color 8 (Maroon)
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

    # Convert colors to RGB tuples
    colors_rgb = [tuple(int(color[i:i+2], 16) for i in (1, 3, 5)) for color in colors]

    # Initialize dictionary to store layer thickness data
    layer_data = []

    # Get image dimensions
    img_height, img_width, _ = image_data.shape

    # Calculate layer thicknesses
    for idx, color_rgb in enumerate(colors_rgb):
        # Create a mask for pixels matching the layer color
        mask = np.all(image_data == np.array(color_rgb), axis=-1)

        # Calculate the thickness of the layer
        total_pixels = np.sum(mask)
        pixels_per_width = total_pixels / img_width
        layer_thickness = (pixels_per_width / img_height) * 6000  # Assume image size to represent 6mm

        # Append the data for this layer
        layer_data.append({
            'Layer': idx + 1,
            'LayerName': layer_names[idx],  # from the predefined list of layer names
            'LayerThicknessMicrometers': layer_thickness
        })

    # Create DataFrame from the layer data
    df_layers = pd.DataFrame(layer_data)
    selected_layers = df_layers[(df_layers['Layer'] >= min(layer1, layer2)) & (df_layers['Layer'] <= max(layer1, layer2))]

    # Calculate the total thickness of selected layers
    total_thickness = selected_layers['LayerThicknessMicrometers'].sum()

    # Return total thickness as a formatted string
    return f"{total_thickness:.2f} um"

