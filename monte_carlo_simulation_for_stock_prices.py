import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt

# Parameters
S0 = 100  # Initial stock price
mu = 0.08  # Expected return
sigma = 0.2  # Volatility
T = 1  # Time period (1 year)
N = 252  # Number of time steps (daily intervals)
simulations = 10000  # Number of Monte Carlo simulations

# Time increment
dt = T / N

# Simulate stock price paths
price_paths = np.zeros((simulations, N + 1))
price_paths[:, 0] = S0

for t in range(1, N + 1):
    # Generate random normal values
    Z = np.random.standard_normal(simulations)
    price_paths[:, t] = price_paths[:, t - 1] * np.exp((mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * Z)

# Save plot to file
plt.figure(figsize=(10, 6))
plt.plot(price_paths.T[:, :50])  # Plot 50 simulated paths
plt.title("Monte Carlo Simulation of Stock Prices")
plt.xlabel("Time Steps")
plt.ylabel("Stock Price")
plt.savefig('monte_carlo_simulation.png')  # Save the plot as an image file

# Calculate metrics
expected_price = price_paths[:, -1].mean()
prob_below_90 = (price_paths[:, -1] < 90).mean()

print(f"Expected price after 1 year: {expected_price:.2f}")
print(f"Probability that the price falls below $90: {prob_below_90:.2%}")
