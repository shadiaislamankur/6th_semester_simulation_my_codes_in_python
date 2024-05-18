import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def random_walk_2D_collision(num_steps, field_size):
    """
    Simulates a 2D random walk for three people and checks for collision.
    
    :param num_steps: Number of steps in the trial.
    :param field_size: The size of the field (field_size x field_size).
    :return: Tuple containing positions of the three people and a flag indicating collision.
    """
    # Initialize positions of the three people randomly within the field
    pos1 = [random.randint(0, field_size - 1), random.randint(0, field_size - 1)]
    pos2 = [random.randint(0, field_size - 1), random.randint(0, field_size - 1)]
    pos3 = [random.randint(0, field_size - 1), random.randint(0, field_size - 1)]
    
    positions1 = [pos1[:]]
    positions2 = [pos2[:]]
    positions3 = [pos3[:]]
    
    for _ in range(num_steps):
        # Randomly move each person in one of the four possible directions
        for pos in [pos1, pos2, pos3]:
            move = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
            if move == 'UP' and pos[1] < field_size - 1:
                pos[1] += 1
            elif move == 'DOWN' and pos[1] > 0:
                pos[1] -= 1
            elif move == 'LEFT' and pos[0] > 0:
                pos[0] -= 1
            elif move == 'RIGHT' and pos[0] < field_size - 1:
                pos[0] += 1
        
        positions1.append(pos1[:])
        positions2.append(pos2[:])
        positions3.append(pos3[:])
        
        # Check for collision
        if pos1 == pos2 == pos3:
            return positions1, positions2, positions3, True

    return positions1, positions2, positions3, False

def estimate_collision_probability(num_steps, num_trials, field_size):
    """
    Estimate the probability of collision in a 2D random walk simulation.
    
    :param num_steps: Number of steps in each trial.
    :param num_trials: Number of trials to simulate.
    :param field_size: The size of the field (field_size x field_size).
    :return: Estimated probability of collision.
    """
    collisions = 0

    for _ in range(num_trials):
        _, _, _, collision = random_walk_2D_collision(num_steps, field_size)
        if collision:
            collisions += 1

    return collisions / num_trials

# Parameters
num_steps = 100    # Number of steps in each trial
num_trials = 10000 # Number of trials
field_size = 10    # Size of the field (10x10 grid)

# Calculate the probability of collision
probability_of_collision = estimate_collision_probability(num_steps, num_trials, field_size)
print(f"Estimated Probability of Collision: {probability_of_collision:.4f}")

# Perform a single trial for visualization
positions1, positions2, positions3, collision = random_walk_2D_collision(num_steps, field_size)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, field_size - 1)
ax.set_ylim(0, field_size - 1)
ax.set_xticks(np.arange(0, field_size, 1))
ax.set_yticks(np.arange(0, field_size, 1))
ax.grid(True)

# Initialize the points
point1, = ax.plot([], [], 'ro', label='Person 1')
point2, = ax.plot([], [], 'go', label='Person 2')
point3, = ax.plot([], [], 'bo', label='Person 3')
collision_point, = ax.plot([], [], 'ko', label='Collision', markersize=10)
ax.legend()

def init():
    point1.set_data([], [])
    point2.set_data([], [])
    point3.set_data([], [])
    collision_point.set_data([], [])
    return point1, point2, point3, collision_point

def update(frame):
    point1.set_data(positions1[frame][0], positions1[frame][1])
    point2.set_data(positions2[frame][0], positions2[frame][1])
    point3.set_data(positions3[frame][0], positions3[frame][1])
    
    if collision and positions1[frame] == positions2[frame] == positions3[frame]:
        collision_point.set_data(positions1[frame][0], positions1[frame][1])
    else:
        collision_point.set_data([], [])
    
    return point1, point2, point3, collision_point

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_steps, init_func=init, blit=True, repeat=False)

plt.title('2D Random Walk Simulation')
plt.show()

# Save the animation as a video file (optional)
# ani.save('random_walk_collision.mp4', writer='ffmpeg', fps=10)
