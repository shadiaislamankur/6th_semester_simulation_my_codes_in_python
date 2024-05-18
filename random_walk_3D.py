import matplotlib.pyplot as plt
import numpy as np
import random
from mpl_toolkits.mplot3d import Axes3D

def randomwalk3D(n):
    x, y, z = np.zeros(n), np.zeros(n), np.zeros(n)

    directions = ["UP", "DOWN", "LEFT", "RIGHT", "IN", "OUT"]
    for i in range(1, n):
        step = random.choice(directions)

        if step == "RIGHT":
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
            z[i] = z[i - 1]
        elif step == "LEFT":
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
            z[i] = z[i - 1]
        elif step == "UP":
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1
            z[i] = z[i - 1]
        elif step == "DOWN":
            x[i] = x[i - 1]
            y[i] = y[i - 1] - 1
            z[i] = z[i - 1]
        elif step == "IN":
            x[i] = x[i - 1]
            y[i] = y[i - 1]
            z[i] = z[i - 1] - 1
        elif step == "OUT":
            x[i] = x[i - 1]
            y[i] = y[i - 1]
            z[i] = z[i - 1] + 1

    return x, y, z

# Number of steps
n = 100

# Get the coordinates from the random walk
x, y, z = randomwalk3D(n)

# Plot the random walk
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, marker='o', linestyle='-', color='b', markersize=4)
ax.set_title('3D Random Walk')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
