import numpy as np
from skimage import filters, feature
from skimage.morphology import skeletonize, remove_small_objects
from skan import Skeleton, summarize
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
'''
skeletonize_image(filepath)
perimeter_image(filepath)
'''

def OCTA_Features(filepath):
    
    #creates skeletonized image
    pillow_image = Image.open(filepath)
    Gray_image = pillow_image.convert('L')
    image_array = np.array(Gray_image)
    image_array2 = image_array > filters.threshold_otsu(image_array)
    octa_skeleton = skeletonize(image_array2)
    
    #creates perimeter map
    filtered_img = filters.frangi(image_array)
    perimeter_img = filtered_img * 100000
    perimeter_img = perimeter_img > filters.threshold_otsu(perimeter_img)
    octa_perimeter = Image.fromarray(perimeter_img)
    
    #area of the scans (presumed 6mm)
    area = 6000/304
    #BVD calculation
    
    BVD = area*(np.sum(octa_perimeter)/np.sum(octa_skeleton))
    
    #VPI calculation
    temp = image_array
    temp = feature.canny(temp,sigma = 1)
    circle_area = np.sum(np.ones(temp.shape))
    circle_pixels = np.sum(temp)
    VPI = circle_pixels*100/circle_area
    
    #BVT calculations
    branch_data = summarize(Skeleton(octa_skeleton))
    branch_distance = branch_data['branch-distance'].values
    euc_distance = branch_data['euclidean-distance'].values
    temp_BVT = np.empty(len(branch_distance))
    print(branch_distance)
    print(euc_distance)
    for i in range(len(temp_BVT)):
        if euc_distance[i] != 0:
            temp_BVT[i] = branch_distance[i]/euc_distance[i]
    BVT = np.mean(temp_BVT)
    print('BVD: ', BVD, 'VPI: ', VPI, 'BVT: ', BVT)
    
OCTA_Features(filepath)
        
        
        
    
    
    
    
    