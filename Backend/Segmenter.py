# Libraries
import numpy as np
import os, cv2, glob
from keras.utils import normalize
from matplotlib import pyplot as plt
import tensorflow as tf

IMG_SIZE = 640

# Capture training image info as a list
test_test = []
test_path = '/Users/adams/Desktop/OCT-Segmenter/Test'

for directory_path in glob.glob(test_path):
    for img_path in glob.glob(os.path.join(directory_path, "*.jpeg")):
        img = cv2.imread(img_path, 0)
        img = cv2.resize(img, (640, 640))
        test_test.append(img)
        print(img_path)

# Convert list to array for machine learning processing
test_test = np.array(test_test)
# test_test = test_test.reshape(-1, IMG_SIZE, IMG_SIZE)


'''
# Shows entire dataset file
plt.figure(figsize=(40,100))
for i in range(8):
    plt.subplot(14, 5, i+1)
    plt.imshow(test_test[i,:,:])
    plt.title("(Label: " + str(i) + ")")
plt.show()
'''

test_test = np.expand_dims(test_test, axis=3)
test_test = normalize(test_test, axis=1)

model_location = '/Users/adams/Downloads/retina_segmentation_8_layer.hdf5'
model = tf.keras.models.load_model(model_location)
# model.summary()
# print(test_test.shape)

test1 = test_test[7]
test_img_norm = test1[:, :, 0][:, :, None]
test = np.expand_dims(test_img_norm, 0)

prediction = (model.predict(test))
predicted_img = np.argmax(prediction, axis=3)[0, :, :]
print(prediction.shape)


plt.figure(figsize=(40, 20))
plt.title('Prediction<')
plt.imshow(predicted_img, cmap='jet')
plt.show()
