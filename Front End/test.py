import cv2
import numpy as np
from PIL import Image
import os
import pandas as pd

def run_code():
    """
    The main function used to run the code
    """
    image_path = "oct_test1/segmented_images/predicted_middle.png"
    bscan_image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Split B-scan image into regions and get cropping boundaries
    perifovea_line, fovea_start, fovea_end, parafovea_line = split_bscan(bscan_image)

    # Get user input for layer range
    layer1 = 1
    layer2 = 8

    # Get user input for region of interest
    region = "parafoveal" # foveal, perifoveal, parafovael, all

    # Define layers based on the specified region
    if region == "foveal":
        cropped_image = crop_foveal_region(bscan_image, fovea_start, fovea_end)
    elif region == "perifoveal":
        cropped_image = crop_perifoveal_region(bscan_image, perifovea_line)
    elif region == "parafoveal":
        cropped_image = crop_parafoveal_region(bscan_image, parafovea_line)
    elif region == "all":
        cropped_image = bscan_image

    # Get the calculated thicknesses
    layer_thicknesses = calculate_thicknesses(cropped_image, layer1, layer2)
    print(f"{region.capitalize()} Thickness: {layer_thicknesses} micrometers")

def split_bscan(bscan_image):
    # Define regions based on image size
    _, width, _ = bscan_image.shape

    perifovea_line = width // 3
    fovea_start = perifovea_line
    fovea_end = 2 * perifovea_line
    parafovea_line = 2 * width // 3

    return perifovea_line, fovea_start, fovea_end, parafovea_line

def crop_foveal_region(bscan_image, fovea_start, fovea_end):
    cropped_image = bscan_image[:, fovea_start:fovea_end, :]
    return cropped_image

def crop_perifoveal_region(bscan_image, perifovea_line):
    cropped_image = bscan_image[:, :perifovea_line, :]
    return cropped_image

def crop_parafoveal_region(bscan_image, parafovea_line):
    cropped_image = bscan_image[:, parafovea_line:, :]
    return cropped_image

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

# Updated run_code to reflect the removal of filepath dependency
def run_code():
    """
    The main function used to run the code
    """
    image_path = "oct_test1/segmented_images/predicted_middle.png"
    bscan_image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Split B-scan image into regions and get cropping boundaries
    perifovea_line, fovea_start, fovea_end, parafovea_line = split_bscan(bscan_image)

    # Get user input for layer range
    layer1 = 1
    layer2 = 8

    # Get user input for region of interest
    region = "parafoveal"  # foveal, perifoveal, parafovael, all

    # Cropping based on the specified region
    if region == "foveal":
        cropped_image = crop_foveal_region(bscan_image, fovea_start, fovea_end)
    elif region == "perifoveal":
        cropped_image = crop_perifoveal_region(bscan_image, perifovea_line)
    elif region == "parafoveal":
        cropped_image = crop_parafoveal_region(bscan_image, parafovea_line)
    elif region == "all":
        cropped_image = bscan_image

    # Calculate and print the thicknesses
    layer_thicknesses = calculate_thicknesses(cropped_image, layer1, layer2)
    print(f"{region.capitalize()} Thickness: {layer_thicknesses}")


# Executes the code
if __name__ == '__main__':
    run_code()
