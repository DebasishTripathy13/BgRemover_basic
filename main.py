from rembg import remove
from PIL import Image
import os

def remove_background(input_path, output_path):
    # Process the image
    input_image = Image.open(input_path)
    output_image = remove(input_image)
    output_image = output_image.convert('RGB')
    output_image.save(output_path)

def process_images(input_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        # Construct the full path for input and output images
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename.replace(".jpg", "_no_bg.jpg"))  # Adjust file extension if needed

        # Process the image and save it with a new name
        remove_background(input_path, output_path)

    print("Background removal process completed.")

# Set your input and output folder paths
input_folder_path = input("Enter the path of the input folder: ")
output_folder_path = input("Enter the path of the output folder: ")

# Process images
process_images(input_folder_path, output_folder_path)
