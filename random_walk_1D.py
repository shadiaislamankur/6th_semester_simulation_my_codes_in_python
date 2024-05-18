import numpy as np
import matplotlib.pyplot as plt
import random

def randomwalk1D(n):
    x, y = 0, 0

    # Generate the time points [0, 1, 2, ..., n]
    timepoints = np.arange(n + 1)
    positions = [y]

    directions = ["UP", "DOWN"]
    for i in range(1, n + 1):

        # Randomly select either UP or DOWN
        step = random.choice(directions)
        
        # Move the object up or down
        if step == "UP":
            y += 1
        elif step == "DOWN":
            y -= 1

        # Keep track of the positions
        positions.append(y)

    return timepoints, positions

# Number of steps
n = 100

# Get the time points and positions from the random walk
timepoints, positions = randomwalk1D(n)

# Plot the random walk
plt.figure(figsize=(10, 6))
plt.plot(timepoints, positions, marker='o', linestyle='-', color='b', markersize=5)
plt.title('1D Random Walk')
plt.xlabel('Time')
plt.ylabel('Position')
plt.grid(True)
plt.show()
