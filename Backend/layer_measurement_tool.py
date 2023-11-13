# OCT Layer Measurement Tool
# Authors: Lauren Bourque & Yousef Abualeinan

# Libraries
from PIL import Image
import os
import pandas as pd


def run_code():
    """
    The main function used to run the code
    """
    image: Image = get_image()
    print(image)
    layer_data: list[pd.DataFrame] = get_layer_data(image_in=image)
    print(layer_data[0].head())
    all_layer_thicknesses: list[pd.Series] = calculate_thicknesses(layers_in=layer_data, image_in=image)
    avg_thicknesses: list[int] = calculate_avg_thicknesses(layer_thicknesses_in=all_layer_thicknesses)


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
        (228, 255, 18),  # Color 1 (Yellow)
        (21, 255, 225),  # Color 2 (Teal)
        (255, 148, 0),  # Color 3 (Orange)
        (0, 0, 255),  # Color 4 (Darker Blue)
        (255, 29, 0),  # Color 5 (Red)
        (124, 255, 121),  # Color 6 (Green)
        (0, 128, 255),  # Color 7 (Sky Blue)
        (127, 0, 0),  # Color 8 (Burgundy)
    ]

    # List of dataframes
    layers = []

    width, height = image_in.size

    for color in colors:
        # Lists to store the x and y coordinates
        x_coordinates = []
        y_coordinates = []

        # Loop through the pixels
        for y in range(height):
            for x in range(width):
                # Get the RGB value of the current pixel
                pixel_value = image_in.getpixel((x, y))

                if pixel_value == color:  # RGB Color
                    x_coordinates.append(x)
                    y_coordinates.append(y)

        # Create the dataframe for the layer and add it to the list of layers
        pixel_df = pd.DataFrame({'x': x_coordinates, 'y': y_coordinates})
        layers.append(pixel_df)

    return layers


def calculate_thicknesses(layers_in: list[pd.DataFrame], image_in: Image):
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
    for layer in layers_in:
        # Create a Pandas Series called layer_thicknesses to store the thicknesses for one layer
        layer_thicknesses = pd.Series(name='layer_thicknesses')

        for x_val in range(width):
            # Filter the DataFrame for the given x value
            subset_layer = layer[layer['x'] == x_val]

            if not subset_layer.empty:
                # Find the biggest and smallest y values
                biggest_y = subset_layer['y'].max()
                smallest_y = subset_layer['y'].min()

                # Calculate the difference
                thickness = biggest_y - smallest_y

                # Append the value to the Series
                layer_thicknesses[x_val] = thickness

        # Add the thickness values for the one layer to the list of layer thicknesses
        all_layer_thicknesses.append(layer_thicknesses)

    return all_layer_thicknesses


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
