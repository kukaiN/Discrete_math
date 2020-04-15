from itertools import combinations, product
import operator
import math
import numpy as np
import random
import matplotlib.pyplot as plt
import visualize_convex_sets as visual

def set_of_points(min_num, max_num, dimensions, num_of_points):
    return combinations(product(range(min_num, max_num+1), repeat=dimensions), num_of_points)

def new_set_of_points(min_num, max_num, num_of_points,  dimensions=2):
    for _ in range(num_of_points):
        pass    


def ccw(base_point, p1, p2):
    # use the cross product to get z value and check the sign
    return (p1[0]-base_point[0])*(p2[1]-base_point[1]) - (p1[1]-base_point[1])*(p2[0]-base_point[0])





def grahams_method(set_of_points, list_size, min_x = None, max_x = None, sorted=True):
    if not sorted:
        set_of_points.sort(key= lambda a: a[1])
    smallest_point = min(set_of_points, key=lambda a: a[1])
    smallest_y = smallest_point[1]
    candidates = [tup for tup in set_of_points if tup[1] == smallest_y]
    candidates.sort(key = lambda a: a[0])
    candidates.reverse()
    starting_point = candidates[0]    
    x_coor, y_coor  = starting_point
    base_vec = [1, 0]
    absolute_points = [point for point in set_of_points if point != starting_point]
    relative_points = [[coor[0]-x_coor, coor[1]-y_coor] for coor in absolute_points]
    angles = [np.arccos(np.dot(base_vec, vec/np.linalg.norm(vec))) for vec in relative_points]
    angles_and_coor = [[ang, coor] for ang, coor in zip(angles, absolute_points)]
    angles_and_coor.sort(key = lambda a: a[0])
    print([a[0] for a in angles_and_coor])
    stack = [starting_point]
    for coor in angles_and_coor:
        while len(stack) > 1 and ccw(stack[-2], starting_point, stack[-1]) < 0:
            del stack[-1]
        stack.append(coor[1])
        print(stack)

    visual.visualize(set_of_points, stack, 2, maxVal=max_x, minVal=min_x)

num_of_points = 12
min_x, max_x = 0 , 30 
stuff = [(random.randint(min_x, max_x), random.randint(min_x, max_x)) for _ in range(num_of_points)]
stuff = list(set(stuff))
print(stuff)
grahams_method(stuff, num_of_points,min_x, max_x, sorted=False)


def check_tverberg(list_of_points, num_of_points):
    for index, list_b in enumerate(list_of_points):
        if index %100000 == 0:print("working on", index)
        if check_size(list_b, num_of_points):
            yield list_b
    print(index)

def check_size(list_of_points, size):
    # returns the bool of the size and the size after hashing
    return len(set(list_of_points)) == size 

def main():
    max_num = 7
    min_num = 0
    dimensions = 2
    num_of_points = 5
    #for a in check_tverberg(set_of_points(min_num, max_num, dimensions, num_of_points), num_of_points):
    #    pass
    print("finished")

"""
import time

t1 = time.time()
nump = 5
for i, a in  enumerate(set_of_points(0, 10, 2, nump)):
    pass
print(i)
print(time.time() - t1)
"""
if __name__ == "__main__":
    main()
