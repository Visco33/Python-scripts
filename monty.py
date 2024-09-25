import numpy as np

# Define the probabilities
P1 = 1 / 500000  # Probability of Event 1 happening
P2 = 1 / 100000  # Probability of Event 2 happening

# Number of trials in each simulation
trials = 1000000000  # 1 million trials

# Number of Monte Carlo simulations
simulations = 1000000000 # Run 10,000 simulations

# Simulate the outcomes for both events
event_1_outcomes = np.random.binomial(trials, P1, simulations)  # Simulate Event 1 for all simulations
event_2_outcomes = np.random.binomial(trials, P2, simulations)  # Simulate Event 2 for all simulations

# Check how many times Event 1 happens 43 times more frequently than Event 2
count_43_times = np.sum(event_1_outcomes >= 43 * event_2_outcomes)

# Calculate the probability
probability_43_times = count_43_times / simulations

# Print the result
print(f"The estimated probability that Event 1 occurs 43 times more than Event 2 is: {probability_43_times:.50f}")
