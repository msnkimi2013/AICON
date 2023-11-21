import cv2
import numpy as np
import csv

# Function to convert an image to HSV and save HSV values to a CSV file
def convert_image_to_hsv_and_save(input_image_path, output_csv_path):
    # Read the image
    image = cv2.imread(input_image_path)

    # Convert the image to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Get the height and width of the image
    height, width, _ = hsv_image.shape

    # Flatten the 2D array of HSV values
    hsv_values = hsv_image.reshape((height * width, 3))

    # Create a CSV file and write the HSV values
    with open(output_csv_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write the header
        csv_writer.writerow(['Hue', 'Saturation', 'Value'])
        # Write the HSV values for each pixel
        csv_writer.writerows(hsv_values)

    print(f"HSV values saved to {output_csv_path}")

# Example usage:
input_image_path = 'path/to/your/input/image.jpg'
output_csv_path = 'path/to/your/output/hsv_values.csv'

convert_image_to_hsv_and_save(input_image_path, output_csv_path)
