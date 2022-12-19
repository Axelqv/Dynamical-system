import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange

a = 1.4
b = 0.3
n_init_vals = 100
n_iter = 1000

x0_values = np.linspace(-0.1, 0.1, n_init_vals)
y0_values = np.linspace(-0.1, 0.1, n_init_vals)
x0_matrix, y0_matrix = np.meshgrid(x0_values, y0_values)
x_values = np.zeros((n_init_vals, n_init_vals, n_iter))
y_values = np.zeros((n_init_vals, n_init_vals, n_iter))



for i in trange(n_init_vals):
    for j in range(n_init_vals):
        x = np.zeros(n_iter)
        y = np.zeros(n_iter)
        x[0] = x0_matrix[i,j]
        y[0] = y0_matrix[i,j]
        for n in range(n_iter - 1):
            x[n + 1] = y[n] + 1 - a * x[n] ** 2
            y[n + 1] = b * x[n]
            x_values[i, j, n] = x[n]
            y_values[i, j, n] = y[n]

for n in trange(100, n_iter):
    plt.plot(x_values[:,:,n], y_values[:,:,n], '.')
plt.show()




