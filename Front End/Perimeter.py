# AUTHOR: SHRIYA GANDOTRA
# This script is modifed to define a function, perimeter_image, that processes an image to highlight 
# its perimeter using image processing techniques. It reads an image from a given file path, converts 
# it to grayscale, and then applies the Frangi filter to enhance ridges or vessel-like structures in the image. 
# Refer to Backend repo for original function

from PIL import Image
import matplotlib.pyplot as plt
import os
import numpy as np
from skimage import filters

def perimeter_image(filepath):
    pillow_image = Image.open(filepath)
    Gray_img = pillow_image.convert('L')
    image_array = np.array(Gray_img)
    
    
    filtered_img = filters.frangi(image_array)
    perimeter_img = filtered_img * 100000
    perimeter_img = perimeter_img > filters.threshold_otsu(perimeter_img)
    perimeter_img = Image.fromarray(perimeter_img)
    perimeter_img = perimeter_img.convert('L')

    save_path = "oct_test1/perimeter_image/perimeter.png"

    directory = os.path.dirname(save_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    perimeter_img.save(save_path)