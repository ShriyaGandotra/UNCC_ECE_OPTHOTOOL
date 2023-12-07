import cv2
import numpy as np

def split_bscan(image_path):
    # Read the color image
    bscan_image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Define regions based on image size
    height, width, _ = bscan_image.shape
    region_height = int(height * 0.2)  # Adjust the height of the regions

    perifovea_line = width // 3
    parafovea_line = 2 * width // 3

    # Draw lines on the original image to mark the regions
    cv2.line(bscan_image, (perifovea_line, region_height), (perifovea_line, height - region_height), (255, 255, 255), 2)  # Perifovea Line
    cv2.line(bscan_image, (parafovea_line, region_height), (parafovea_line, height - region_height), (255, 255, 255), 2)  # Parafovea Line

    # Display the marked image
    cv2.imshow("Marked B-Scan", bscan_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Replace 'your_image_path.jpg' with the path to B-Scan image
    image_path = r"C:Images\color_test.png"
    split_bscan(image_path)