# Libraries
import numpy as np
import os, cv2, glob, time, math
from keras.utils import normalize
from matplotlib import pyplot as plt
from keras.models import load_model

IMG_SIZE = 640

# Capture training image info as a list
input_image = []
img_path = r'C:/Users/adams/Desktop/Adams_B_scan' #Replace with input path in final dev
png_count = 0

png_files = glob.glob(os.path.join(img_path, "*.png"))
png_count = len(png_files)

'''
denoised = []

for image_path in png_files:
    # Convert to grayscale if needed
    gray = cv2.imread(image_path, 0)

    # Apply median filter
    median_filtered = cv2.medianBlur(gray, 1)

    # Apply non-local means denoising
    denoised1 = cv2.fastNlMeansDenoising(median_filtered, None, 30, 7, 21)
    denoised.append(denoised1)
    

plt.figure(figsize=(40,80))
for i in range(5): #t_img
    plt.subplot(1, 5, i+1) #plt.subplot(rows_needed, img_per_row, i+1)
    plt.imshow(denoised[i])
    plt.axis('off')
    
plt.tight_layout()
plt.show()
'''


for image_path in png_files:
    img = cv2.imread(image_path, 0)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE)) # interpolation = cv2.INTER_NEAREST
    #img = cv2.addWeighted(img, 1.0, img, 1.0, 1.0)
    input_image.append(img)
    print(image_path)

print(png_count)

# Convert list to array for machine learning processing
input_image = np.array(input_image)

# Plot Dims
img_per_row = 20
t_img = png_count
rows_needed = math.ceil(t_img/img_per_row)


# Shows entire dataset file
plt.figure(figsize=(40,80))
for i in range(5): #t_img
    plt.subplot(1, 5, i+1) #plt.subplot(rows_needed, img_per_row, i+1)
    plt.imshow(input_image[i,:,:])
    plt.axis('off')
    
plt.tight_layout()
plt.show()


expand_img = np.expand_dims(input_image, axis=3)
norm_image = normalize(expand_img, axis=1)

#Load Model
model_location = 'Backend/Backend-Models/retina_segmentation_8_layer.hdf5'
model = load_model(model_location)

# Printing the predicted images
start = time.time()
plt.figure(figsize=(10,40))

for i in range(5):
    img = norm_image[i]
    img_norm = img[:, :, 0][:, :, None]
    img = np.expand_dims(img_norm, 0)

    prediction = (model.predict(img))
    predicted_img = np.argmax(prediction, axis=3)[0, :, :]

    plt.subplot(1, 5, i+1)
    plt.imshow(predicted_img, cmap='jet')
    plt.axis('off')

end = time.time()
plt.tight_layout() 
plt.show()
dur = end - start
print(f"Duration: {dur} seconds")
print(f"Prediction shape: {prediction.shape}")



# Indivdual Predicted layers for 1 scan
for i in range(9):
    img = norm_image[i]
    img_norm = img[:, :, 0][:, :, None]
    img = np.expand_dims(img_norm, 0)

    prediction = (model.predict(img))
    plt.subplot(2, 5, i+1)
    plt.imshow(prediction[0, :, :, i])
    plt.axis('off')

plt.tight_layout() 
plt.show()