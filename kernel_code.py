

from numba import cuda, int32

TPB = 16

@cuda.jit
def fast_cross_prod(Avec, Bvec, C):
    x = cuda.grid(1)
    C[x] = Avec[0]*Bvec[1]-Avec[1]*Bvec[0] 