# AUTHOR: SHRIYA GANDOTRA
# This script is modified to define a function, skeletonize_image, for 
# creating a skeletonized representation of an OCTA (Optical Coherence Tomography Angiography) image.
# Refer to Backend repo for original function

from skimage import filters
from PIL import Image
import matplotlib.pyplot as plt
import os
import numpy as np
from skimage import filters
from skimage.morphology import skeletonize

#function for skeletonizing an OCTA image
def skeletonize_image(filepath):
    #takes filepath and makes it into a PIL image, grayscales, and converts to numpy array
    pillow_image = Image.open(filepath)
    Gray_image = pillow_image.convert('L')
    image_array = np.array(Gray_image)
    
    #cleans up image, threshold pixel values to be above 100
    image_array = image_array > filters.threshold_otsu(image_array)

    #create skeletonized map from image
    oct_skeleton_image = skeletonize(image_array)
    #oct_skeleton_image = remove_small_objects(oct_skeleton_image, min_size=5)
    #changes numpy array to PIL image and then saves the image
    pil_skeleton = Image.fromarray(oct_skeleton_image)

    save_path = "oct_test1/skeletonized_image/skeleton.png"

    directory = os.path.dirname(save_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
 
    pil_skeleton.save(save_path)