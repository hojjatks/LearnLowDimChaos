# load data from ../Data/Lorenz63.npz'
import numpy as np
import matplotlib.pyplot as plt

# Load the data
data = np.load('../Data/Lorenz63.npz')
print("Data loaded from ../Data/Lorenz63.npz")
X = data['X']
print("Data shape:", X.shape)
# Plot the data
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.plot(X[:, 0], X[:, 1], X[:, 2], lw=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# save figure
plt.savefig('../Figs/Lorenz63.png', dpi=300)
print("Figure saved to ../Figs/Lorenz63_attractor.png")
# plot the time series
fig, ax = plt.subplots(3, 1, figsize=(10, 10))
ax[0].plot(X[:, 0], lw=0.5)
ax[0].set_title('X')
ax[1].plot(X[:, 1], lw=0.5)
ax[1].set_title('Y')
ax[2].plot(X[:, 2], lw=0.5)
ax[2].set_title('Z')
# save figure
plt.savefig('../Figs/Lorenz63_time_series.png', dpi=300)
print("Figure saved to ../Figs/Lorenz63_time_series.png")
