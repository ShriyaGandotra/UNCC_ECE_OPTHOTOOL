import numpy as np
import pandas as pd
from PIL import Image, ImageChops, ImageOps
from keras.models import load_model
import PIL
import tensorflow as tf
import keras
import os

# filepath = 'OCTA.png'
# model = 'AVA_model_3.hdf5'

def AVA_save(filepath, model):
    pil_img = Image.open(filepath)
    pil_img = pil_img.resize([320,320])
    pil_img = pil_img.convert('RGB')

    #change image to tensor for input into AVA-net
    tensor_img = tf.convert_to_tensor(pil_img)
    tensor_img = tf.expand_dims(tensor_img,axis=0)

    #load model, compile false for prediction not training
    base_model = load_model(model, compile = False)

    #create AVA map
    ava_map = base_model.predict(tensor_img)
    ava_map = tf.squeeze(ava_map,axis = 0)
    pil_ava = keras.preprocessing.image.array_to_img(ava_map)

    #create seperate artery and vein maps
    pil_ava = pil_ava.convert('RGB')
    inverted_ava = ImageOps.invert(pil_ava)

    #create red and blue images for AV seperation
    red = Image.new('RGB', (320,320), 'red')
    blue = Image.new('RGB', (320,320), 'blue')

    #create A and V map without color
    a_map = ImageChops.multiply(pil_ava,pil_img)
    v_map = ImageChops.multiply(inverted_ava,pil_img)

    #multiply to create red vein map and blue artery map
    red_a_map = ImageChops.multiply(a_map,red)
    blue_v_map = ImageChops.multiply(v_map,blue)

    #add together to create red and blue AV map
    av_map = ImageChops.add(red_a_map,blue_v_map)

    # Create the directory if it doesn't exist
    save_directory = "oct_test1/AVA"
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # Save the images in the specified directory
    av_map.save(os.path.join(save_directory, 'av_map.png'))
    a_map.save(os.path.join(save_directory, 'a_map.png'))
    v_map.save(os.path.join(save_directory, 'v_map.png'))

#Return the paths where the images were saved
    return (os.path.join(save_directory, 'av_map.png'),
            os.path.join(save_directory, 'a_map.png'),
            os.path.join(save_directory, 'v_map.png'))


def AVA_features(a_path, v_path):
    a_map = Image.open(a_path)
    v_map = Image.open(v_path)
    
    #count pixels and intensities for arteries
    a_pixels = 0
    v_pixels = 0
    a_I = 0
    v_I = 0
    
    a_map = a_map.convert('L')
    v_map = v_map.convert('L')
    
    for pixel in a_map.getdata():
        if pixel != (0):
            a_pixels += 1
    
    a_data = a_map.getdata()
    a_I = sum(pixel for pixel in a_data)
   

    #count pixels and intensities for veins
    
    for pixel in v_map.getdata():
        if pixel != (0):
            v_pixels += 1

    v_data = v_map.getdata()
    v_I = sum(pixel for pixel in v_data)
    
    #A_PID calculation
    A_PID = 100/255 *(a_I/a_pixels)
    #V_PID calculation
    V_PID = 100/255 *(v_I/v_pixels)
    #AV_PID ratio calculation
    AV_PIDR = A_PID/V_PID

    print('A_PID: ', A_PID, 'V_PID: ', V_PID, 'AV_PIDR: ', AV_PIDR)

    return round(A_PID,4) , round(V_PID,4), round(AV_PIDR,4)
    
