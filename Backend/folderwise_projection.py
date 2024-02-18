import numpy as np
from PIL import Image
import os
import re
import matplotlib.pyplot as plt

def create_projection(images):
    return np.max(images, axis=1).astype(np.uint8)

def save_image(image_array, save_path):
    img = Image.fromarray(image_array)
    img.save(save_path)

def display_image(image_array):
    # Prediction Save Path
    save_path = r"C:\Users\youse\OneDrive\Desktop\School\Senior Spring\VS Code\Senior Design\projections/projection.png"
    plt.imshow(image_array, cmap='gray')
    plt.axis('off')
    plt.savefig(save_path, bbox_inches='tight')
    plt.show()

# Folder containing PNG Folder
folder_path = "C:/Users/youse/OneDrive/Desktop/School/Senior Spring/VS Code/Senior Design/raw_images"


img = sorted(os.listdir(folder_path))
images = []

for image in img:
    image = Image.open(folder_path + '/' + image)
    images.append(np.asarray(image))

# Create 2D projection
projection = create_projection(images)

# Display and optionally save the projection
display_image(projection)
