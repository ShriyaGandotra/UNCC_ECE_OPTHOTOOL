import numpy as np
import pandas as pd
from PIL import Image, ImageChops, ImageOps
from keras.models import load_model
import PIL
import tensorflow as tf
import keras

filepath = '/Users/hunte/Documents/Python/OCTATEST.png'
model = 'Backend/Backend-Models\AVA_model_3.hdf5'

def AVA_features(filepath, model):
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
    pil_ava.save('AVA_map.png')

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
    #av_map.save('av_map.png')
    #a_map.save('a_map.png')
    #v_map.save('v_map.png')

    #count pixels and intensities for arteries
    a_pixels = 0
    v_pixels = 0
    a_I = 0
    v_I = 0
    for pixel in a_map.getdata():
        if pixel != (0,0,0):
            a_pixels += 1
    a_I = sum(list(sum(list(a_map.getdata()),())))

    #count pixels and intensities for veins
    for pixel in v_map.getdata():
        if pixel != (0,0,0):
            v_pixels += 1

    v_I = sum(list(sum(list(v_map.getdata()),())))
    
    #A_PID calculation
    A_PID = 100/255 *(a_I/a_pixels)
    #V_PID calculation
    V_PID = 100/255 *(v_I/v_pixels)
    #AV_PID ratio calculation
    AV_PIDR = A_PID/V_PID
    '''
    print('A_PID = ', A_PID)
    print('V_PID = ', V_PID)
    print('AV_PIDR = ', AV_PIDR)
    '''
    return A_PID, V_PID, AV_PIDR


