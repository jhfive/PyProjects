import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('../Images/image.jpeg')

plt.imshow(img)
plt.show()