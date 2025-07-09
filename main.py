import os
from PIL import Image
import numpy as np


images_folder = 'images'
target_size = (200, 150)

def checkjpg(folder):
    files = os.listdir(folder)
    jpg_files = [file for file in files if file.lower().endswith(('.jpg', '.jpeg'))]
    return jpg_files

jpg_files = checkjpg(images_folder)
rgb_arrays = []

for file in jpg_files:
    image = Image.open(os.path.join(images_folder, file)).convert('RGB')
    image = image.resize(target_size)
    rgb_array = np.array(image, dtype=np.float32)
    rgb_arrays.append(rgb_array)

if not rgb_arrays:
    print("No JPG images found in the folder.")
else:
    # Stack images into a 4D array: (num_images, height, width, channels)
    all_images = np.stack(rgb_arrays, axis=0)
    # Compute pixel-wise average across all images
    avg_image = np.mean(all_images, axis=0)
    # Convert averaged pixels to uint8 (0-255)
    avg_image_uint8 = avg_image.astype(np.uint8)
    # Convert NumPy array to PIL Image
    avg_pil_image = Image.fromarray(avg_image_uint8, 'RGB')
    # Save as JPEG
    avg_pil_image.save('average_image.jpg', format='JPEG')
    print("Average image saved as 'average_image.jpg'.")
