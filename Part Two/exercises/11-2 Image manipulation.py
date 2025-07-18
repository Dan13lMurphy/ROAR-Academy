import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image  # <-- You forgot to import this

# Get current file path
path = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(path, "lenna-mod.jpg")
filename2 = os.path.join(path, "zebras.jpg")

# Load images
data = mpimg.imread(filename)
data2 = mpimg.imread(filename2)

# Resize second image to fit in top-right corner (e.g., 100x100 pixels)
resized_shape = (100, 100)
data2_resized = np.array(Image.fromarray(
    (data2 * 255).astype(np.uint8)).resize(resized_shape)) / 255.0

# Replace top-right corner
data[:100, -100:] = data2_resized

# Display result
fig, ax = plt.subplots()
ax.imshow(data)
ax.axis('off')
