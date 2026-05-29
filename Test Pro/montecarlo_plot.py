import numpy as np
import matplotlib.pyplot as plt

S0 = 100
mu = 0.07
sigma = 0.2
T = 1
dt = 1/252
N = int(T/dt)
simulations = 5

for i in range(simulations):
    prices = [S0]
    shock = np.random.normal(loc=(mu*dt), scale=(sigma*np.sqrt(dt)))
    prices.append(prices[-1] * np.exp(shock))
plt.plot(prices)

plt.title('Monte Carlo Stock Price Simulation')
plt.xlabel('Days')
plt.ylabel('Price')
plt.show()