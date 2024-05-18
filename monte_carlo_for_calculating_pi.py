import random
import numpy as np
import matplotlib.pyplot as plt

def estimate_pi_with_dartboard_visualization(num_darts):
    inside_circle = 0
    x_inside, y_inside = [], []

    # Define the radius and center of the dartboard
    dartboard_radius = 1.0
    dartboard_center = (0, 0)

    for _ in range(num_darts):
        x = random.uniform(-dartboard_radius, dartboard_radius)
        y = random.uniform(-dartboard_radius, dartboard_radius)
        distance = x**2 + y**2

        if distance <= dartboard_radius**2:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)

    estimated_pi = 4 * inside_circle / num_darts

    # Visualization
    fig, ax = plt.subplots(figsize=(8, 8))
    circle = plt.Circle(dartboard_center, dartboard_radius, color='b', fill=False, label='Dartboard')
    ax.add_patch(circle)
    plt.scatter(x_inside, y_inside, color='r', marker='o', label='Dart Throws')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title(f'Monte Carlo Estimation of π: {estimated_pi:.4f} for dart throws: {num_darts}')
    plt.legend(loc='upper right')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim(-dartboard_radius - 0.1, dartboard_radius + 0.1)
    plt.ylim(-dartboard_radius - 0.1, dartboard_radius + 0.1)
    plt.grid(True)
    plt.show()

    return estimated_pi

#First Run
num_darts = 100
estimated_pi = estimate_pi_with_dartboard_visualization(num_darts)
print(f"Estimated π with {num_darts} dart throws: {estimated_pi}")

#Second Run
num_darts = 1000
estimated_pi = estimate_pi_with_dartboard_visualization(num_darts)
print(f"Estimated π with {num_darts} dart throws: {estimated_pi}")




#third run
num_darts = 100000
estimated_pi = estimate_pi_with_dartboard_visualization(num_darts)
print(f"Estimated π with {num_darts} dart throws: {estimated_pi}")