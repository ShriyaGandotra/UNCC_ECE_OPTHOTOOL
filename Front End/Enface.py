############### ENFACE ##############
from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt
import Config as CONFIG

def create_projection(images):
    return np.max(CONFIG.images, axis=1).astype(np.uint8)

def save_image(image_array, save_path):
    img = Image.fromarray(image_array)
    img.save(save_path)

def display_image(image_array):
    # Ensure the save directory exists
    save_dir = "oct_test1/enface_image"  # Name of the folder to save images
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    # Prediction Save Path
    save_path = os.path.join(save_dir, "projection.png")
    plt.imshow(image_array, cmap='gray')
    plt.axis('off')
    plt.savefig(save_path, bbox_inches='tight')
    return save_path
    # plt.show() is removed to prevent displaying the image

def enface_conversion():
    folder_path = "oct_test1/raw_images"

    # Ensure folder_path exists or handle it appropriately
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist. Please check the path.")
    else:
        img = sorted(os.listdir(folder_path))
        CONFIG.images = []

        for image in img:
            image_path = os.path.join(folder_path, image)
            if os.path.isfile(image_path):  # Ensure it's a file
                image = Image.open(image_path)
                CONFIG.images.append(np.asarray(image))

    # Create 2D projection
    projection = create_projection(np.array(CONFIG.images))
    display_image(projection)