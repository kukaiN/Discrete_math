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


def CCW_from_determinant(point1, point2, point3):
    return (point1[0]-point2[0])*(point3[1]-point2[1]) - (point1[1]-point2[1])*(point3[0]-point2[0])
    

def get_distance(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])

def find_angle(point_list, lowest_point):
    low_x, low_y = lowest_point
    return [(math.atan2(point[1]-low_y, point[0]-low_x), point) for point in point_list]

def grahams_method(set_of_points, list_size, min_x = None, max_x = None, sorted=True):
    lowest_y = min(set_of_points, key = lambda a: a[1])[1]
    points_with_lowest_y = [point for point in set_of_points if point[1] == lowest_y]
    points_with_lowest_y.sort(key= lambda a: a[0])
    smallest_point = points_with_lowest_y[0]
    angles_and_points = find_angle(set_of_points, smallest_point)
    angles_dict = dict()
    print(smallest_point)
    for item in angles_and_points:
        value = angles_dict.get(item[0], None)
        if value == None: angles_dict[item[0]] = item[1]
        elif get_distance(smallest_point, item[1]) > get_distance(smallest_point, value):
            print(angles_dict[item[0]], item)
            angles_dict[item[0]] = item[1]
        else:
            print(angles_dict[item[0]], item)
    angle_list = [(key, value) for key, value in angles_dict.items()]
    angle_list.sort(key = lambda a: a[0])
    print(angle_list)
    print(len(angle_list))
    stack = []
    for point in angle_list:
        while len(stack)>1 and CCW_from_determinant(stack[-1], stack[-2], point[1]) < 0:
            del stack[-1]
        stack.append(point[1])
    print(stack)
    new_stack = [smallest_point]+stack+[smallest_point]
    visual.visualize(set_of_points, new_stack, 2, maxVal=max_x, minVal=min_x, angles=False, min_point=smallest_point)


def main():
    num_of_points = 20
    min_x, max_x = 0 , 40 
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
