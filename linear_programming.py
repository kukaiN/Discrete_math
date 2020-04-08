import math
import fractions

# Farkas's Lemma
# special case of duality, section 10.1 in Jiri Matousheck's Book on Discrete math

# farkas's lemma:
# either one of the following happens for a d x n matrix 


def Farkas_Lemma(d, n, matrix_A):
    # solution to Ax = 0, A is a matrix and x is what we're looking for
    pass
    # either solution is non trivial non-negative solution x in R^n
    # one is definitly positive and others non-negative


    # second option is the following:
    #  there exist a solution x such that Transpose(x)*A is a vect with all strictly negative values.
    # if we multiply jth equation by yi and add the equations together, 
    # we get an equation with no nontrivial nonnegative solutuion.  since all coefficents are negative,
    # while the right hand side is 0



    # why we get two cases:
    # either zero is in the convex set or its not


    # if the the zero element is in the conv(V), then zero is a convex combination of the points in the set 
    # if zero is not in the set, there exist a hyper plane separating V from zero.
    # ie a unit vector y in R^d, such that <y, v> < <y, 0> = 0 for each v in V.


def radon_partition(dimensions, set_A):
    if len(set_A) == dimensions+2:
        # there exist a radon partition
        pass
    else:
        # partition is not guranteed
        pass

def Hellys_theorem(dimensions, set_of_convex_set):
    if len(set_of_convex_set) > dimentions:
        pass
        # check if every d+1 is non_empty
        # then theintersection of all the sets is non_empty 


def check_intersection(set_A):
    pass
    # checks the intersection this one returns a bool

def return_intersection(set_A):
    # similar to check_intersection, but returns the elements.
    pass

def find_centerpoint(set_A):
    pass

def find_flat_that_bisect_set(dimensions, set_A):
    # center_traversal_theorem
    # if size of set_A <= dimesions
    # then using the ham sandwich thorem, theres a k-flat, 

# ham-sanwitch cu t for two n-point sets can be computed in linear time
# Lo, Matousek, and steiger

# finding center_point is also linear 

# ham-sandwich for dimensions greater than 2 has runtime slightly better than O(n^(d-1))

# an efficient randomized algorithm for finding a centerpoint in higher dimensions was made in '96


def minkowski_theorem(dimensions, set_A, symmetric=True):
    # by assumption, set needs to be bounded, convex, and symmetric
    
    
    volume = 0
    if volume > 2**dimensions:
        # there exist a lattice point in Z^dimensions thats not zero
        # there's also symmetry so points come in multiple of two C and -C
        pass

def approximate_irrational_by_rational(irrational_number):
    alpha = 0 # value between 0 and 1
    N = 1 # a natural number
    abs(alpha - m/n) < 1/(n*N)

def LLL_algorithm(basis):
    pass
    # gets the "best" basis

def find_shortest_vector(dimensions, basis):
    # this is NP-hard
    pass


def use_LLL_to_solve_cryptyography(basis, num):
    pass

def simplex_method():
    pass

def interior_angle_method():
    pass

def elipsodic_method():
    pass

def projective_method():
    pass

def input_sparsity_method():
    pass

def matrix_multi_method():
    pass

def transpose(constraints):
    return [[value for value in constraints[j]] for j in range(len(constraints))]