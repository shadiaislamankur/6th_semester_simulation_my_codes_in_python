import random
import matplotlib.pyplot as plt

# Define bearing life and probabilities
bearing_life = [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900]
bearing_probabilities = [0.10, 0.14, 0.24, 0.14, 0.12, 0.10, 0.06, 0.05, 0.03, 0.02]

# Calculate cumulative probabilities for bearing life
bearing_cumulative_probabilities = [bearing_probabilities[0]]
for i in range(1, len(bearing_probabilities)):
    bearing_cumulative_probabilities.append(bearing_cumulative_probabilities[i-1] + bearing_probabilities[i])

# Generate random digit assignments for bearing life
bearing_random_digits = []
count = 0
for i in range(len(bearing_probabilities)):
    bearing_random_digits.append([])
    for j in range(int(bearing_probabilities[i]*100)):
        bearing_random_digits[i].append(count)
        count += 1

# Define delay life and probabilities
delay_life = [4, 6, 8]
delay_probabilities = [0.3, 0.6, 0.1]

# Calculate cumulative probabilities for delay life
delay_cumulative_probabilities = [delay_probabilities[0]]
for i in range(1, len(delay_probabilities)):
    delay_cumulative_probabilities.append(delay_cumulative_probabilities[i-1] + delay_probabilities[i])

# Generate random digit assignments for delay life
delay_random_digits = []
count = 0
for i in range(len(delay_probabilities)):
    delay_random_digits.append([])
    for j in range(int(delay_probabilities[i]*10)):
        delay_random_digits[i].append(count)
        count += 1

# Simulation parameters
total_hours_of_operation = 30000
total_clock_hours = 0
total_delay_minutes = 0
total_changes = 0  # Total number of bearing replacements

bearing_life_distribution = []  # To store bearing life values for visualization
delay_distribution = []         # To store delay values for visualization

# Simulation loop
while total_hours_of_operation > total_clock_hours:
    total_changes += 1
    bearing_random_num_1 = random.randint(0, 99)
    bearing_random_num_2 = random.randint(0, 99)
    bearing_random_num_3 = random.randint(0, 99)
    delay_random_num = random.randint(0, 9)
    
    current_clock = float('inf')
    current_delay = 0

    # Determine bearing life based on random numbers
    for i in range(len(bearing_random_digits)):
        if bearing_random_num_1 in bearing_random_digits[i]:
            current_clock = min(current_clock, bearing_life[i])
        if bearing_random_num_2 in bearing_random_digits[i]:
            current_clock = min(current_clock, bearing_life[i])
        if bearing_random_num_3 in bearing_random_digits[i]:
            current_clock = min(current_clock, bearing_life[i])

    total_clock_hours += current_clock
    bearing_life_distribution.append(current_clock)

    # Determine delay time based on random number
    for i in range(len(delay_random_digits)):
        if delay_random_num in delay_random_digits[i]:
            current_delay = delay_life[i]
            break

    total_delay_minutes += current_delay
    delay_distribution.append(current_delay)

# Cost parameters
three_bearing_change_time_minutes = 40
cost_of_downtime_per_minute = 5
cost_of_repairman_per_hour = 25
cost_of_one_bearing = 20

# Calculate costs
total_downtime_minutes = total_delay_minutes + (total_changes * three_bearing_change_time_minutes)
cost_of_downtime = cost_of_downtime_per_minute * total_downtime_minutes
cost_of_repairman = (total_changes * three_bearing_change_time_minutes * cost_of_repairman_per_hour) / 60
total_bearings_replaced = total_changes * 3
cost_of_bearings = cost_of_one_bearing * total_bearings_replaced

# Print results
print("Total repairman delay time =", total_delay_minutes, "minutes")
print("Time spent in bearing replacement =", total_changes * three_bearing_change_time_minutes, "minutes")
print("Total downtime =", total_downtime_minutes, "minutes")
print("Cost of downtime = Rs.", cost_of_downtime)
print("Cost of repairman = Rs.", cost_of_repairman)
print("Total bearings replaced =", total_bearings_replaced)
print("Cost of bearings = Rs.", cost_of_bearings)
print("Total estimated cost = Rs.", cost_of_downtime + cost_of_repairman + cost_of_bearings)

# Visualization
plt.figure(figsize=(14, 6))

# Plot bearing life distribution
plt.subplot(1, 2, 1)
plt.hist(bearing_life_distribution, bins=bearing_life, edgecolor='black')
plt.xlabel('Bearing Life (Hours)')
plt.ylabel('Frequency')
plt.title('Distribution of Bearing Life')

# Plot delay distribution
plt.subplot(1, 2, 2)
plt.hist(delay_distribution, bins=delay_life, edgecolor='black')
plt.xlabel('Delay Time (Minutes)')
plt.ylabel('Frequency')
plt.title('Distribution of Delay Times')

plt.tight_layout()
plt.show()
