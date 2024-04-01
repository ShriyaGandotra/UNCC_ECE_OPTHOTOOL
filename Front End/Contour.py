# AUTHOR: SHRIYA GANDOTRA
# Features include:
# - Processing of OCT images by resizing and normalizing them for model input
# - Predicting the segmentation of these images using a pre trainined model
# - Contour mapping on segmented images to detedt and hilight edges within the image

import numpy as np
import os, cv2, glob, time, math
from keras.utils import normalize
from keras.models import load_model

IMG_SIZE = 640

def process_and_save_segmented_images(output_path, model_location):
    # Capture training image info as a list
    input_image = []
    img_path = "oct_test1/raw_images" 
    png_count = 0

    # Ensure the segmented images directory exists
    # output_path = r'oct_test1/segmented_images'
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    png_files = glob.glob(os.path.join(img_path, "*.png"))
    middle_index = len(png_files) // 2  # Index of the middle image
    png_count = 1  # Since you're only processing one image

    if png_files:  # Check if there are any png files
        image_path = png_files[middle_index]
        img = cv2.imread(image_path, 0)
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))  # interpolation=cv2.INTER_NEAREST
        input_image.append(img)

    print(f"Processing {png_count} images...")

    # Convert list to array for machine learning processing
    input_image = np.array(input_image)

    expand_img = np.expand_dims(input_image, axis=3)
    norm_image = normalize(expand_img, axis=1)

    # Load Model
    model_location = 'retina_segmentation_8_layer.hdf5'
    model = load_model(model_location)

    # Printing (saving) the predicted images
    start = time.time()
 
    # Assuming input_image contains just the middle image after your adjustments
    img_norm = norm_image[0][:, :, None]  # Adding the channel dimension
    img_expanded = np.expand_dims(img_norm, 0)  # Expanding the batch size dimension

    # Perform prediction
    prediction = model.predict(img_expanded)
    predicted_img = np.argmax(prediction, axis=3)[0, :, :]

    # Normalize the predicted image to 0-255 to apply colormap
    predicted_img_normalized = cv2.normalize(predicted_img, None, 0, 255, cv2.NORM_MINMAX)
    predicted_img_normalized = predicted_img_normalized.astype('uint8')

    # Apply 'jet' colormap to the normalized image
    colored_image = cv2.applyColorMap(predicted_img_normalized, cv2.COLORMAP_JET)

    # Prepare file path
    file_name = f"predicted_middle.png"
    file_path = os.path.join(output_path, file_name)
    
    # Save the predicted, color-mapped image
    cv2.imwrite(file_path, colored_image)

    end = time.time()
    dur = end - start
    print(f"Duration: {dur} seconds")
    print(f"Saved predicted images in {output_path}")

    return output_path

############# CONTOUR MAPING #########
def contour_mapping(filepath):
    """
    The main function used to run the code
    """
    # Read the B-scan image
    original_image = cv2.imread(filepath)

   # Convert the original image to grayscale
    grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(grayscale_image, (9, 9), 1)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred, 30, 70)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original color image
    result_image = original_image.copy()
    cv2.drawContours(result_image, contours, -1, (0, 0, 0), 2)

    # Save the image with contoursS
    output_folder = os.path.join("oct_test1", 'contoured_images')
    os.makedirs(output_folder, exist_ok=True)

    output_filepath = os.path.join(output_folder, 'contoured_image.png')
    cv2.imwrite(output_filepath, result_image)

def contour_conversion():
    process_and_save_segmented_images('oct_test1/segmented_images', 'retina_segmentation_8_layer.hdf5')
    contour_path = os.path.join('oct_test1/segmented_images', "predicted_middle.png")
    contour_mapping(contour_path)