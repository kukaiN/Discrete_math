import numpy as np
import cupy as cp

print("hello")
x_gpu = cp.array([1, 2, 3])

x_cpu = np.array([1, 2, 3])
l2_cpu = np.linalg.norm(x_cpu)

l2_gpu = cp.linalg.norm(x_gpu)
print("jesus")