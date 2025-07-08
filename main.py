from PIL import Image
import numpy as np

IMAGES = 3
target_size = (200, 150)  # Width x Height; adjust as needed

rgb_arrays = []

# Load and resize images to the same size
for i in range(IMAGES):
    image = Image.open(f'image{i}.jpg').convert('RGB')
    image = image.resize(target_size)
    rgb_array = np.array(image, dtype=np.float32)  # Use float for averaging
    rgb_arrays.append(rgb_array)

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
