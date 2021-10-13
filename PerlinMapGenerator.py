import random
import matplotlib.pyplot as plt
import numpy as np

import GeneratePerlinNoise
import ColorPerlinNoise
import GenerateCircularGradient

height = 512
width = 512
persistivity = 0.5  # Should be between 0 and 1
lac = 2  # Should be more than one
octa = 3  # Should be more than one
scale = 100  # The Higher the scale the more zoomed in map will be
seed = 128  # Can be any value
gradientRadius = 100  # The higher the value, smaller gradient will be formed

random.seed(seed)
# Behaves weirdly if value is larger than 100000
ow = random.uniform(-100000, 100000)
oh = random.uniform(-100000, 100000)

world = GeneratePerlinNoise.generateNoiseMap(
    width, height, persistivity, lac, octa, scale, ow, oh)
colored_world = ColorPerlinNoise.colorNoiseMap(world, width, height)
circular_gradient = GenerateCircularGradient.generateCircularGradient(
    width, height, gradientRadius)
circular_world = world * circular_gradient
for i in range(width):
    for j in range(height):
        if circular_world[i][j] <= 0:
            circular_world[i][j] = 0
circular_world = circular_world/np.amax(circular_world)
colored_circular_world = np.zeros_like(colored_world)
colored_circular_world = ColorPerlinNoise.colorNoiseMap(
    circular_world, width, height)

plt.subplot(2, 3, 1)
plt.imshow(world, cmap='gray')
plt.title('Perlin Noise Map')
plt.subplot(2, 3, 3)
plt.imshow(colored_world)
plt.title('Colored Noise Map')
plt.subplot(2, 3, 4)
plt.imshow(circular_gradient, cmap='gray')
plt.title('Circular Gradient')
plt.subplot(2, 3, 5)
plt.imshow(circular_world, cmap='gray')
plt.title('Circular World Noise')
plt.subplot(2, 3, 6)
plt.imshow(colored_circular_world)
plt.title('Colored Circular Noise Map')
plt.show()
