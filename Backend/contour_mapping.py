# Contour Mapping Tool
# Authors: Lauren Bourque

# Libraries
import cv2
import matplotlib.pyplot as plt
import os


def run_code():
    """
    The main function used to run the code
    """
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filename = "Images\\predicted_40.png"
    filepath = os.path.join(script_dir, filename)  # Segmented image filepath

    # Read the original B-scan image
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

    # Save the image with contours
    output_folder = os.path.join(script_dir, 'ContouredImages')
    os.makedirs(output_folder, exist_ok=True)

    output_filepath = os.path.join(output_folder, 'contoured_image.png')
    cv2.imwrite(output_filepath, result_image)

    # Display the result
    plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))
    plt.title("Original B-Scan Image with Contours")
    plt.show()


# Executes the code
if __name__ == '__main__':
    run_code()

