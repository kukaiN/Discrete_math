import numpy as np
import cupy as cp

print("hello")
x_gpu = cp.array([1, 2, 3])

x_cpu = np.array([1, 2, 3])
l2_cpu = np.linalg.norm(x_cpu)
l2_gpu = cp.linalg.norm(x_gpu)

#cp.cuda.device(1).use()
x = cp.array([1, 2, 3, 4, 5]) # this is generated in the memory  of the GPU
print(type(x))
print(type(cp.asnumpy(x))) # this .asnumpy converst cupy array to numpy, but it also have the funciton to move where the item is stord from the gpu to the cpu
print(x.device)


x_gpu = cp.array([1, 2, 3])
x_cpu = x_gpu.get()
print(x_cpu)

print("jesus")