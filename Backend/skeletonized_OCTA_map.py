import numpy as np
from skimage import filters
from skimage.morphology import skeletonize, remove_small_objects
from PIL import Image

filepath = 'OCTATEST2.png'

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
    
    pil_skeleton.save('skeleton.png')

def perimeter_image(filepath):
    pillow_image = Image.open(filepath)
    Gray_img = pillow_image.convert('L')
    image_array = np.array(Gray_img)
    
    
    filtered_img = filters.frangi(image_array)
    perimeter_img = filtered_img * 100000
    perimeter_img = perimeter_img > filters.threshold_otsu(perimeter_img)
    #perimeter_img = remove_small_objects(perimeter_img, min_size=5)
    perimeter_img = Image.fromarray(perimeter_img)
    perimeter_img = perimeter_img.convert('L')
    perimeter_img.save('perimeter.png')

skeletonize_image(filepath)
perimeter_image(filepath)