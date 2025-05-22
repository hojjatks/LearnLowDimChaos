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
# saving the input data to the Data folder
np.savez('../Data/InputLorenz63.npz', X=X)
print("Input Data (x) saved to ../Data/InputLorenz63.npz")
# saving the output data to the Data folder
dX = np.gradient(X, t_eval, axis=0)
print("Dimension of the input is", X.shape)
np.savez('../Data/OutputLorenz63.npz', dX=dX)
print("Output Data (dx/dt) saved to ../Data/OutputLorenz63.npz")
print('Dimension of the output is', dX.shape)