# OCT Layer Measurement Tool
# Authors: Lauren Bourque & Yousef Abualeinan

# Libraries
from PIL import Image
import os
import pandas as pd
import colorir.color_class
import numpy as np


def run_code():
    """
    The main function used to run the code
    """
    image: Image = get_image()
    print(image)
    layer_data: dict[pd.DataFrame] = get_layer_data(image_in=image)
    all_layer_thicknesses: list[pd.Series] = calculate_thicknesses(layers_in=layer_data, image_in=image)
    avg_thicknesses: list[int] = calculate_avg_thicknesses(layer_thicknesses_in=all_layer_thicknesses)
    print(avg_thicknesses)


def get_image():
    """
    Gets the current working directory and accesses the image
    :returns image: Image -> the segmented OCT scan used for measurement
    """
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filename = "Images/test_image.png"
    filepath = os.path.join(script_dir, filename) # Segmented image filepath
    image = Image.open(filepath)
    return image


def get_layer_data(image_in: Image):
    """
    Stores the x and y coordinates of the different pixel values in each layer. Creates a dataframe for each color (layer)
    :param image_in (Image) -> the segmented OCT scan
    :returns layers (list[pd.Dataframe]) -> A list of 8 DataFrames representing each layer. Each DataFrame contains the x and y coordinates for all the pixels in this layer
    """
    # List of RGB colors to get pixel data from
    colors = [
        '#00007f',  # Background color (Dark Blue)
        '#e4ff12',  # Color 1 (Yellow)
        '#15ffe1',  # Color 2 (Teal)
        '#ff9400',  # Color 3 (Orange)
        '#0028ff',  # Color 4 (Darker Blue)
        '#ff1d00',  # Color 5 (Red)
        '#7cff79',  # Color 6 (Green)
        '#0080ff',  # Color 7 (Sky Blue)
        '#7f0000',  # Color 8 (Burgundy)
    ]

    # Dictionary of lists (Starts with Color 1 [Yellow])
    layers = {hex_color: [] for hex_color in colors[1:]}

    width, height = image_in.size

    # Convert the image to a NumPy array for faster processing
    image_array = np.array(image_in)

    # Loop through the pixels
    for y in range(height):
        for x in range(width):
            # Get the RGB value of the current pixel and convert to hex
            pixel_value = image_array[y, x]
            hex_value = rgb_to_hex(pixel_value)
            closest_color = calculate_hue(target=hex_value, tints=colors)

            # Make sure the color isn't the background color
            if closest_color is not None and closest_color != colors[0]:  # Hex Color
                layers[closest_color].append({'x': x, 'y': y})

    # Convert lists of dictionaries to DataFrames
    layers = {color: pd.DataFrame(data) for color, data in layers.items()}

    return layers


def rgb_to_hex(rgb):
    """
    Convert RGB tuple to hexadecimal color code
    :param rgb (RGB) -> the rgb value to convert
    :returns hex_color: str -> the RGB color represented in hexadecimal format
    """
    hex_color = "#{:02x}{:02x}{:02x}".format(*rgb)
    return hex_color


def calculate_hue(target, tints):
    """
    Finds the closest color in a list of provided hues
    :param target: str -> the color value to match to the hues in hexadecimal format
    :param tints: list(str) -> the list of hues in hexadecimal format
    :returns closest[0]: str -> the color best matching the target represented in hexadecimal format
    """
    target_hue = colorir.color_class.HexRGB(target).hsl()[0]
    closest = (None, 180)
    for tint in tints:
        hue = colorir.color_class.HexRGB(tint).hsl()[0]
        hue_dist = (min(target_hue, hue) - max(target_hue, hue)) % 360
        if hue_dist < closest[1]:
            closest = (tint, hue_dist)
    return closest[0]


def calculate_thicknesses(layers_in: dict[pd.DataFrame], image_in: Image):
    """
    Stores the x and y coordinates of the different pixel values in each layer. Creates a dataframe for each color (layer)
    :param layers_in (list of DataFrame) -> the list of DataFrames representing each layer
    :param image_in: Image -> the segmented OCT scan
    :returns all_layer_thicknesses -> list of 8 pandas Series objects containing the layer thicknesses for each pixel along the x axis for each layer
    """
    width, height = image_in.size

    # A list of 8 pandas Series objects containing the layer thickness for each pixel width in each layer
    all_layer_thicknesses: list = []

    # Loop through the Dataframes
    for key, layer in layers_in.items():
        # Create a Pandas Series called layer_thicknesses to store the thicknesses for one layer
        layer_thicknesses = pd.Series(name='layer_thicknesses')

        for x_val in range(width):
            # Filter the DataFrame for the given x value
            subset_layer = layer[layer['x'] == x_val]

            if not subset_layer.empty:
                # Find the biggest and smallest y values
                biggest_y = find_max_y_val(subset_in=subset_layer)
                smallest_y = find_min_y_val(subset_in=subset_layer)

                if biggest_y is not None and smallest_y is not None:
                    # Calculate the difference
                    thickness = biggest_y - smallest_y + 1

                    # Append the value to the Series
                    layer_thicknesses[x_val] = thickness

        # Add the thickness values for the one layer to the list of layer thicknesses
        all_layer_thicknesses.append(layer_thicknesses)

    return all_layer_thicknesses


def find_min_y_val(subset_in: pd.DataFrame):
    """
    Finds the minimum y value in the DataFrame, making sure that there's another pixel next to it so we're not choosing a random pixel
    :param subset_in: pd.DataFrame -> the x column of values to find the minimum y value for 
    :returns current_value -> the minimum y value
    """
    # Sort values in the 'y' column from least to greatest
    subset_sorted = subset_in.sort_values(by='y')

    # Iterate through the sorted values using the index
    for index, value in subset_sorted.iterrows():
        current_value = value['y']

        # Check if there is a value 1 greater than the current value
        has_one_greater = (subset_sorted['y'] == current_value + 1).any()

        # If there is, return the current value
        if has_one_greater:
            return current_value


def find_max_y_val(subset_in: pd.DataFrame):
    """
    Finds the maximum y value in the DataFrame, making sure that there's another pixel next to it so we're not choosing a random pixel
    :param subset_in: pd.DataFrame -> the x column of values to find the maximum y value for 
    :returns current_value -> the maximum y value
    """
    # Sort values in the 'y' column from greatest to least
    subset_sorted = subset_in.sort_values(by='y', ascending=False)

    # Iterate through the sorted values using the index
    for index, value in subset_sorted.iterrows():
        current_value = value['y']

        # Check if there is a value 1 greater than the current value
        has_one_less = (subset_sorted['y'] == current_value - 1).any()

        # If there is, return the current value
        if has_one_less:
            return current_value


def calculate_avg_thicknesses(layer_thicknesses_in: list[pd.Series]):
    """
    Calculates the average thicknesses for the provided thickness values
    :param layer_thicknesses_in (list[pd.Series]) -> list of 8 pandas Series objects containing the layer thicknesses for each pixel along the x axis for each layer
    :returns avg_thicknesses (list[int]) -> list of 8 average thickness values
    """
    avg_thicknesses = []

    # Calculates the mean value for each Pandas Series
    for layer in layer_thicknesses_in:
        mean_value = layer.mean()
        avg_thicknesses.append(mean_value)

    return avg_thicknesses


# Executes the code
if __name__ == '__main__':
    run_code()
