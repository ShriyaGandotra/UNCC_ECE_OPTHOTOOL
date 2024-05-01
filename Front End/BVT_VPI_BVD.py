import numpy as np
from skimage import filters, feature
from skimage.morphology import skeletonize
from skan import Skeleton, summarize
from PIL import Image
from tkinter import Label, mainloop

filepath = 'OCTA.png'

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
    
    return round(BVD,4) , round(VPI,4), round(BVT,4)
     