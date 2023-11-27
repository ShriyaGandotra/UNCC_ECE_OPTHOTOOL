import numpy as np
import pandas as pd
from PIL import Image, ImageChops, ImageOps
from keras.models import load_model
import PIL
import tensorflow as tf
import keras

filepath = '/Users/hunte/Documents/Python/OCTATEST.png'
model = 'AVA_model_3.hdf5'

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

#create AV map with color seperation
a_map = ImageChops.multiply(pil_ava,pil_img)
v_map = ImageChops.multiply(inverted_ava,pil_img)

#multiply to create red vein map and blue artery map
red_a_map = ImageChops.multiply(a_map,red)
blue_v_map = ImageChops.multiply(v_map,blue)

av_map = ImageChops.add(red_a_map,blue_v_map)

av_map.save('av_map.png')
#a_map.save('a_map.png')
#v_map.save('v_map.png')


#count number of red and blue pixels
red = (255,0,0)
red_pixels, blue_pixels = 0

image = Image.open(ava_map)
for pixel in image.getdata():
    if pixel is red:
        red_pixels += 1
width, height = image.size
total_area = width*height

#red pixels is arteries, blue pixels is veins
blue_pixels = total_area-red_pixels

#percentage AA (red pixels/total pixels)*100
aa_percent = (red_pixels/total_area)

# percentage VA (blue pixels/total pixels)*100
va_percent = (blue_pixels/total_area)

#A-PID
I_sum = 0
#for pixel in pil_amap.getdata():
#    I_sum += pil_amap.getdata()
#A_PID = 100/255*(1/red_pixels)*I_sum

