import numpy as np 
from scipy.integrate import solve_ivp



def lorenz63(t, state, sigma=10.0, rho=28.0, beta=8/3):
    x, y, z = state
    return [sigma*(y - x), x*(rho - z) - y, x*y - beta*z]

t_span = (0, 1000)
print("Generating Lorenz63 data...")
print("The time span is", t_span)
t_eval = np.linspace(*t_span, 50000)

sol = solve_ivp(lorenz63, t_span, [1.0, 1.0, 1.0], t_eval=t_eval)
X = sol.y.T
# saving the data to the Data folder
np.savez('../Data/Lorenz63.npz', X=X)
print("Data saved to ../Data/Lorenz63.npz")