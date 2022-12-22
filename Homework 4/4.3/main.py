import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange

a = 1.4
b = 0.3
n_init_vals = 100
n_iter = 1000
min_val = -0.2
max_val = 0.2

x0_values = np.linspace(min_val, max_val, n_init_vals)
y0_values = np.linspace(min_val, max_val, n_init_vals)
x0_matrix, y0_matrix = np.meshgrid(x0_values[:, np.newaxis], y0_values[:, np.newaxis])

x_values = np.zeros((n_init_vals, n_init_vals, n_iter))
y_values = np.zeros((n_init_vals, n_init_vals, n_iter))

x_values[:, :, 0] = x0_matrix
y_values[:, :, 0] = y0_matrix

for n in trange(n_iter-1):
    x_values[:, :, n + 1] = y_values[:, :, n] + 1 - a * x_values[:, :, n] ** 2
    y_values[:, :, n + 1] = b * x_values[:, :, n]

for n in trange(100, n_iter):
    plt.plot(x_values[:,:,n], y_values[:,:,n], '.')


plt.ylabel('y')
plt.xlabel('x')
plt.show()