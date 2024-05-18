import random
import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_integration(num_points):
    # Function to estimate the integral of: f(x) = 0.25 * x^4
    def f(x):
        return 0.25 * x**4

    # Interval for the integral: [2, 5]
    a, b = 2, 5

    # Initialize variable to store the integral estimate
    integral_estimate = 0

    # Lists to store random points for visualization
    x_points = []
    y_points = []

    # Perform the Monte Carlo simulation
    for _ in range(num_points):
        x = random.uniform(a, b)
        y = f(x)
        integral_estimate += y
        
        x_points.append(x)
        y_points.append(y)

    # Calculate the estimated integral value
    integral_estimate *= (b - a) / num_points

    # Generate x values for plotting the function
    x_values = np.linspace(a, b, 400)
    y_values = [f(x) for x in x_values]

    # Plot the function and the random points (larger size)
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label='f(x) = 0.25x^4', color='blue')
    plt.scatter(x_points, y_points, color='red', s=20, label='Random Points')
    plt.fill_between(x_values, y_values, color='lightgray', alpha=0.5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Monte Carlo Estimation of Integral ≈ {integral_estimate:.4f}')
    plt.legend()
    plt.grid(True)
    plt.show()

# First Run
num_points = 50
monte_carlo_integration(num_points)

# Second Run 
num_points = 500
monte_carlo_integration(num_points)
