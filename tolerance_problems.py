import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from itertools import product, combinations
import math
import scipy.optimize as sci_op
import visualize_convex_sets as visual
import time
import random

def fast_list_merge(list_a, list_b):
    # this method of merging was added in python 3.7, 
    # this is slightly faster than the .extend or the "+" opperation for big lists
    return [*list_a, *list_b]

def trap_sq_generator(grid_length, sq_size):
    trap = [(i, j) for j in range(sq_size, grid_length) for i in range(j+1+((grid_length+1)&1))]
    sq = [(i, j) for j in range(1, sq_size) for i in range(sq_size+1)]
    return fast_list_merge(trap, sq)

def open_pickle():
    pass

def save_pickle():
    pass

def point_in_convex_hull(convex_hull, point):
    pass

def partition_generator(set_of_points):
    # this will return partitons that adds up to # of partitions ^ number of points
    pass

def tolerance(set_of_points, n = 7, t = 1, d = 2):
    if d == 2:
        x = np.array(set_of_points)
        z = (0, 1)
        y = np.array(z)
        print(in_hull(x, y))

    else:
        # forget about higher dimensional cases for now
        pass
def lower_bound_for_tolerance(dimension, tolerance, partitions, max_lattice_length):
    pass

def in_hull(convex_set, x):
    set_size = len(convex_set)
    #dimension =len(x)
    c=np.zeros(set_size)
    A = np.r_[convex_set.T, np.ones((1, set_size))]
    b = np.r_[x, np.ones(1)]
    print(convex_set.T)
    print(A)
    print("b", b)
    lp = sci_op.linprog(c, A_eq=A, b_eq=b)
    return lp.success

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def convex_hull(points):
    """Computes the convex hull of a set of 2D points.

    Input: an iterable sequence of (x, y) pairs representing the points.
    Output: a list of vertices of the convex hull in counter-clockwise order,
      starting from the vertex with the lexicographically smallest coordinates.
    Implements Andrew's monotone chain algorithm. O(n log n) complexity.
    """

    # Sort the points lexicographically (tuples are compared lexicographically).
    # Remove duplicates to detect the case we have just one unique point.
    points = sorted(points)
    #print(points)
    # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
    # Returns a positive value, if OAB makes a counter-clockwise turn,
    # negative for clockwise turn, and zero if the points are collinear.

    # Build lower hull 
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenation of the lower and upper hulls gives the convex hull.
    # Last point of each list is omitted because it is repeated at the beginning of the other list. 
    if lower[0] == upper[-1]:
        return lower[:-1] + upper
    return lower[:-1] + upper[:-1]

def inside_set(queue_of_set, points):
    """
    this is a O(log n) algorithm of checking if the point is in the set
    """
    for ind in range()

def start_base_case(n = 7, ll = 4, t = 1, k = 2, d = 2):
    # since the search space is going to be the shape below, we will use two generators,
    # one for the points in the square and one for the skewed trapezoidal shape
    """
    6    __________________
    5   |                /
    4   |              /    
    3   |___________ /       
    2   |          |
    1   |          |
    0   |__________|
        0  1  2  3  4  5  6
    """
    # the top row and bottom row will each have one fixed point and no point greater than it 
    grid_length = ll
    sq_size = int((grid_length+1)/2)
   
    non_fixed_points = trap_sq_generator(grid_length, sq_size)
    #print(f"saved {((grid_length+1)*(grid_length-1)) - len(non_fixed_points)+ 2} points")
    #print(non_fixed_points)
    non_fixed_size = len(non_fixed_points)
    rn_sum = 0
    for top_point in [(i, grid_length) for i in range(grid_length+1)]:
        top_free_points = [(i, grid_length) for i in range(grid_length) if i < top_point[0]]
        num_top_row = len(top_free_points)
        
        for bottom_point in [(i, 0) for i in range(sq_size+1)]:
            
            bottom_free_points = [(i, 0) for i in range(sq_size) if i < bottom_point[0]]
            num_bottom_row = len(bottom_free_points)
            search_space_size = num_bottom_row + num_top_row + non_fixed_size
            if  search_space_size < n-2:
                print(f"not enough points, require {n-2} points, the space has {search_space_size} points" , bottom_point, top_point)
            else:
                fixed_points = [top_point, bottom_point]
                #print("new space", fixed_points, search_space_size)
                search_space = top_free_points + bottom_free_points + non_fixed_points
                for permutation_of_n_points in combinations(search_space, n-2):
                    per_n_points = list(permutation_of_n_points)
                    
                    x = convex_hull(per_n_points+fixed_points)
                    for int_z in [(k, g) for g in range(grid_length+1) for k in range(grid_length+1)]:
                        if inside_set(x, int_z):
                            print("i")
                        else:
                            print("2"*20)
                    #visual.visualize(per_n_points+fixed_points, x, 2, 10, 0)
                    #tolerance(list(permutation_of_n_points) + fixed_points, n ,  t, d)
                    break
                break
        break
                #print(index)
    print(rn_sum)
    print("*" * 10)




def main():
    d = 2
    n = 12
    t = 1
    k = 2
    ll = 5
    #problem_parameters = [d, n, t, k, ll]
    #start_base_case(n=12, ll = 8)
    #t1 = time.time()
    
    list_x = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(12)]
    entry = ([a[0] for a in list_x] + [a[1] for a in list_x])
    max_x, min_x = max(entry), min(entry)
    collection_of_points = [(a, b) for a in range(min_x, max_x+1) for b in range(min_x, max_x+1)]
    for point in list_x:
        new_list = set(list_x) - set(point)
        for n in range(2, 6):
            for part_A in combinations(list(new_list), n ):
                part_B = list(new_list - set(part_A))
                conv_A, conv_B = convex_hull(part_A), convex_hull(part_B)
                point_in_A = [a for a in collection_of_points if inside_set(conv_A, a)]
                point_in_AB = [a for a in point_in_A if inside_set(conv_B, a)]
                if point_in_AB != []:
                    print("a")
                else:
                    #print("b"*20)
                    pass

if __name__ == "__main__":
    main()