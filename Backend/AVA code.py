import numpy as np
import pandas as pd
from PIL import Image
from keras.models import load_model
import tensorflow as tf
import keras

filepath = ''
model = 'AVA_model_3.hdf5'

#change image to tensor for input into AVA-net

img = tf.io.read_file(filepath)
tensor_img = tf.io.decode_image(img, channels = 3)
tensor_img = tf.expand_dims(tensor_img,axis=0)

#load model, compile false for prediction not training
base_model = load_model(model, compile = False)
base_model.summary()

#create AVA map and AV map
ava_map = base_model.predict(tensor_img)
av_map = img * ava_map

ava_map.save('AVA_map.png')
av_map.save('AV_map.png')

#count number of red and blue pixels
red = (255,0,0)
red_pixels, blue_pixels = 0

image = Image.open(ava_map)
for pixel in image.getdata():
    if pixel is red:
        red_pixels += 1
width, height = image.size
total_area = width*height
blue_pixels = total_area-red_pixels

#percentage AA (red pixels/total pixels)*100
aa_percent = (red_pixels/total_area)

# percentage VA (blue pixels/total pixels)*100
va_percent = (blue_pixels/total_area)

