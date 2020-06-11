from itertools import combinations, product
import operator
import math
import numpy as np
import scipy.optimize as sci_op
import random
import matplotlib.pyplot as plt
import visualize_convex_sets as visual
import os
import pickle
import pandas as pd
import time

def set_of_points(min_num, max_num, dimensions, num_of_points):
    return itertools.combinations(itertools.product(range(min_num, max_num+1), repeat=dimensions), num_of_points)

def CCW_from_determinant(point1, point2, point3):
    return (point1[0]-point2[0])*(point3[1]-point2[1]) - (point1[1]-point2[1])*(point3[0]-point2[0])

def get_distance(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])

def make_angle_list(point_list, lowest_point):
    low_x, low_y = lowest_point
    # using atan2 because it takes the adjacient side and the opposite side separately
    # there's a division by zero for normal atan(y / x) if the point in consideration is directly above
    return [(math.atan2(point[1]-low_y, point[0]-low_x), point) for point in point_list]

def get_smallest_point(set_of_points):
    # getting the smallest element, O(n)
    smallest_point = set_of_points[0]
    for point in set_of_points:
        if smallest_point[1]+1>point[1] and smallest_point[0]+1 > point[0]:
            smallest_point = point
    return smallest_point

def grahams_method(set_of_points, list_size, min_x = None, max_x = None, list_sorted=True):
    
    smallest_point = get_smallest_point(set_of_points)

    # making a dictionary with angles from the smallest point
    angles_dict = dict()
    for angle in make_angle_list(set_of_points, smallest_point):
        if not angles_dict.get(angle[0], False): angles_dict[angle[0]] = angle[1]
        elif get_distance(smallest_point, angle[1]) > get_distance(smallest_point, angles_dict[angle[0]]):
            angles_dict[angle[0]] = angle[1]
        # if same angle, but with shorter distace, then dont add it to the dictionary

    # use a stack to decide if
    stack = []
    for point in sorted(angles_dict.items(), key=operator.itemgetter(0)):
        while len(stack)>1 and CCW_from_determinant(stack[-1], stack[-2], point[1]) < 0:
            del stack[-1]
        stack.append(point[1])
    new_stack = [smallest_point]+stack+[smallest_point]
    return (new_stack, smallest_point)

def in_hull(convex_set, x):
    set_size = len(convex_set)
    #dimension =len(x)
    c=np.zeros(set_size)
    A = np.r_[convex_set.T, np.ones((1, set_size))]
    b = np.r_[x, np.ones(1)]
    lp = sci_op.linprog(c, A_eq=A, b_eq=b)
    return lp.success

def save_pickle(filepath, content):
    content.to_pickle(filepath)

def load_pickle(filepath, default):
    """load an existing pickle file or make a pickle with default data and return the pickled data"""
    try:
        with open(filepath, "rb") as f:
            x = pickle.load(f)
    except Exception:
        x = default
        print("exception")
        with open(path, "wb") as f:
            pickle.dump(x, f)
    return x

def get_cd():
    scriptpath, filename = os.path.realpath(__file__), "" 
    for i in range(1,len(scriptpath)+1):
        if scriptpath[-i] == "\\":
            scriptpath = scriptpath[0:-i]
            break
    if os.getcwd() != scriptpath: filename = scriptpath + "\\"
    return filename

def reducible_slope(del_x, del_y):
    # simple check to see if the partition is even worthy of checking
    reduced_slope = math.gcd(del_x, del_y) 
    if reduced_slope == 1:
        return 0
    else: # if there's a reducible slope, then theres an integer point in between, given both input points have integer coordinates
        return reduced_slope

def Z_radon_counter_example(min_x, max_x, number_of_points, dimension):
    t1 = time.time()
    found_counter_examples = []
    number_generator = []
    
def partition_set(integer_tup_set, set_size, partition_size):
    pass

def find_examples(min_x, max_x, number_of_points, pickle_name):
    t1 = time.time()
    found_examples = []
    for index, candidate_points in enumerate(set_of_points(min_x, max_x, 2,  number_of_points)):  
        if index%100000 == 0: print(index)
        sets_overlap = False
        
        for ind, partition in enumerate(combinations(candidate_points, 2)): # partition contains two points that we want to use
            # find the slope of the integer points
            p1, p2 = partition
            delta_x, delta_y = p2[0] - p1[0], p2[1] - p1[1]
            points_in_between = reducible_slope(delta_x, delta_y)
            
            if points_in_between:
                delta_x, delta_y = int(delta_x/points_in_between), int(delta_y/points_in_between)
            points = [[p1[0]+i*delta_x, p1[1]+i*delta_y] for i in range(points_in_between+1)] if points_in_between else partition
            # integer points on the line
          
            # the other set of 3 points that makes a convex hull
            other_partition = np.array([point for point in candidate_points if point not in partition])
            for point in points:
                if in_hull(other_partition, np.array(point)):
                        sets_overlap = True
        # go to next candidate points
        if not sets_overlap:
            found_examples.append(candidate_points)
    if found_examples != []:
        df = pd.DataFrame(data_points, columns=["p1", "p2", "p3", "p4", "p5"])
        save_pickle(pickle_name, df)
    time_took = t1-time.time() 
    print(time_took)
    print("index", index)
    return found_examples

def probable_intersection(list_of_sets_of_points, number_of_set):
    """
    returns m, n and the bottom left point of a m x n grid where the intersection would lie if it exist
    if you have sets A and B that intersect on the 2d space, 
    then you can restrict the search space by the minimum of the maximum x and y and the maximum of the minimum of x and y of the sets

    its really easy to get the max and min, per set
    """


def filter_same_shape(data, min_x, max_x):
    base_shape = data[0]
    set_of_shapes = []
    for convex_set in data:
        outside_stack = grahams_method(convex_set, 1, min_x, max_x)[0]
        angles_list = []
        length_list = []
        stack_size = len(outside_stack)
        for i in range(stack_size):
            #print(outside_stack)
            x1, y1 = outside_stack[i%stack_size]
            x2, y2 = outside_stack[(i+1)%stack_size]
            length_list.append(math.hypot(x2-x1, y2-y1))
        if set_of_shapes == []:
            set_of_shapes.append((convex_set , length_list))
        else:
            # check the distances between points if they're the same, then they're the same 
            temp_bool = True
            for tup_item in set_of_shapes:
                if set(tup_item[1]) != set(length_list):
                    temp_bool = False
            if temp_bool:
                set_of_shapes.append((convex_set , length_list))

    
    return set_of_shapes

def rotations(points):
    new_points = [points]
    new_points.append([[-point[1], point[0]] for point in points])
    new_points.append([[-point[0], -point[1]] for point in points])
    new_points.append([[point[1], -point[0]] for point in points])
    return new_points

def xy_flip(points):
    return [[point[1], point[0]] for point in points]


def filter_same_shape2(data, min_x, max_x):
    variation_set = []
    unique_sets = []
    for potential_set in data:
        add_to_set = True
       
        for transformed_set in rotations(potential_set) + rotations(xy_flip(potential_set)):
            smallest_point = get_smallest_point(transformed_set)
            x_sm, y_sm = smallest_point
            
            scaled_data = [(point[0]-x_sm, point[1]-y_sm) for point in transformed_set]
            break_bool = True
            for known_set in variation_set:
                if break_bool:
                    if set(known_set) == set(scaled_data):
                        break_bool = False
                    
                variation_set.append(scaled_data)
            if not break_bool:
                add_to_set = False
        if add_to_set:
            unique_sets.append(potential_set)
    return unique_sets

def play_with_pickle(current_dir, min_x, max_x):
    # open pkl file
    data = load_pickle(current_dir+"tverberg_keep7.pkl", [])
    new_data = []
    for index, row in data.iterrows():
        current_row = []
        for pt in row:
            current_row.append(pt)
        new_data.append(current_row)
        
    new_data = filter_same_shape(new_data, min_x, max_x)
    #print(new_data)
    counter = 0
    for data in new_data:
        
        smallest_point = get_smallest_point(data[0])
        visual.visualize(data[0], data[0], 2, maxVal=max_x, minVal=min_x, angles=True, min_point=smallest_point, other_point=True)

def main():
    current_dir = get_cd()
    num_of_points = 10
    min_x, max_x = 0 , 7
    dimensions = 2
    repetition = 1
    pickle_name = current_dir+"tverberg"
    pickle_name+=".pkl"

    """
    examplesss = [[(0, 0), (0, 1), (1, 0), (2, 3), (3, 2)], [(0, 0), (0, 1), (1, 2), (2, 0), (3, 2)], [(0, 0), (0, 1), (1, 2), (3, 0), (3, 2)], [(0, 0), (0, 1), (1, 3), (2, 0), (3, 2)], [(0, 0), (0, 1), (1, 3), (3, 0), (3, 2)], [(0, 0), (0, 1), (2, 0), (2, 3), (3, 2)], [(0, 0), (0, 1), (2, 3), (3, 0), (3, 2)], [(0, 0), (0, 2), (1, 0), (2, 1), (2, 3)], [(0, 0), (0, 2), (1, 0), (2, 3), (3, 1)], [(0, 0), (0, 2), (1, 0), (2, 3), (3, 2)], [(0, 0), (0, 2), (1, 3), (2, 0), (2, 3)], [(0, 0), (0, 2), (1, 3), (2, 1), (2, 3)], [(0, 0), (0, 2), (1, 3), (2, 1), (3, 3)], [(0, 0), (0, 2), (1, 3), (2, 3), (3, 0)], [(0, 0), (0, 2), (1, 3), (2, 3), (3, 1)], [(0, 0), (0, 2), (1, 3), (3, 0), (3, 1)], [(0, 0), (0, 2), (1, 3), (3, 0), (3, 3)], [(0, 0), (0, 2), (2, 0), (3, 1), (3, 2)], [(0, 0), (0, 2), (2, 2), (3, 0), (3, 1)], [(0, 0), (0, 2), (2, 3), (3, 0), (3, 1)], [(0, 0), (0, 3), (1, 0), (2, 1), (2, 3)], [(0, 0), (0, 3), (1, 0), (2, 3), (3, 1)], [(0, 0), (0, 3), (1, 0), (2, 3), (3, 2)], [(0, 0), (0, 3), (1, 3), (2, 0), (2, 2)], [(0, 0), (0, 3), (1, 3), (2, 0), (3, 1)], [(0, 0), (0, 3), (1, 3), (2, 0), (3, 2)], [(0, 0), (0, 3), (2, 0), (3, 1), (3, 2)], [(0, 0), (0, 3), (2, 0), (3, 1), (3, 3)], [(0, 0), (0, 3), (2, 3), (3, 0), (3, 2)], [(0, 0), (0, 3), (2, 3), (3, 1), (3, 2)], [(0, 0), (1, 2), (2, 0), (3, 1), (3, 2)], [(0, 0), (1, 2), (2, 0), (3, 1), (3, 3)], [(0, 0), (1, 3), (2, 0), (3, 1), (3, 2)], [(0, 0), (1, 3), (2, 3), (3, 0), (3, 2)], [(0, 0), (0, 1), (1, -1), (2, 1), (3, -1)], [(0, 0), (0, 1), (1, -1), (2, 2), (3, -1)], [(0, 0), (0, 1), (1, -1), (3, -1), (3, 1)], [(0, 0), (0, 1), (1, -1), (3, -1), (3, 2)], [(0, 0), (0, 1), (1, 2), (2, -1), (3, 2)], [(0, 0), (0, 1), (1, 2), (3, -1), (3, 2)], [(0, 0), (0, 2), (1, -1), (2, -1), (2, 1)], [(0, 0), (0, 2), (1, -1), (2, -1), (2, 2)], [(0, 0), (0, 2), (1, -1), (2, -1), (3, 1)], [(0, 0), (0, 2), (1, -1), (2, -1), (3, 2)], [(0, 0), (0, 2), (1, -1), (2, 1), (3, -1)], [(0, 0), (0, 2), (1, -1), (3, -1), (3, 2)], [(0, 0), (0, 2), (1, -1), (3, 1), (3, 2)], [(0, 0), (0, 2), (1, 2), (2, -1), (2, 1)], [(0, 0), (0, 2), (1, 2), (2, -1), (3, 0)], [(0, 0), (0, 2), (1, 2), (2, -1), (3, 1)], [(0, 0), (0, 2), (2, -1), (3, 1), (3, 2)], [(0, 0), (1, -1), (1, 2), (3, 1), (3, 2)], [(0, 0), (1, -1), (2, 2), (3, -1), (3, 2)], [(0, 0), (1, -1), (2, 2), (3, 0), (3, 2)], [(0, 0), (1, -1), (2, 2), (3, 1), (3, 2)], [(0, 0), 
(1, 2), (2, -1), (3, -1), (3, 1)], [(0, 0), (1, 2), (2, -1), (3, -1), (3, 2)], [(0, 0), (1, 2), (2, -1), (3, 1), (3, 2)], [(0, 0), (1, 2), (2, 2), (3, -1), (3, 1)], [(0, 0), (0, 1), (1, -2), (2, 1), (3, -1)], [(0, 0), (0, 1), (1, -2), (3, -1), (3, 1)], [(0, 0), (0, 1), (1, 1), (2, -2), (3, -1)], [(0, 0), (0, 1), (2, -2), (2, 1), (3, -1)], [(0, 0), (0, 1), (2, -2), (3, -1), (3, 1)], [(0, 0), (1, -2), (1, 1), (3, -2), (3, -1)], [(0, 0), (1, -2), (2, -2), (3, -1), (3, 1)], [(0, 0), (1, -2), (2, 0), (3, -2), (3, -1)], [(0, 0), (1, -2), (2, 1), (3, -2), (3, -1)], [(0, 0), (1, -2), (2, 1), (3, -2), (3, 1)], [(0, 0), (1, -2), (2, 1), (3, -1), (3, 1)], [(0, 0), (1, 1), (2, -2), (3, -2), (3, -1)], [(0, 0), (1, 1), (2, -2), (3, -2), (3, 0)], [(0, 0), (1, 1), (2, -2), (3, -2), (3, 1)], [(0, 0), (1, -3), (2, -3), (3, -2), (3, 0)], [(0, 0), 
(1, -3), (2, 0), (3, -2), (3, -1)], [(0, 0), (1, -2), (2, 0), (3, -3), (3, -1)]]



    """
    examplesss = [[(0,0), (0, 1), (1, 1)], [(0, 0), (1, 0), (1, 1)]]
    """
    for i in range(repetition):
        stuff = list(set((random.randint(min_x, max_x), random.randint(min_x, max_x)) for _ in range(num_of_points)))
        exterior_set, smallest_point = grahams_method(stuff, num_of_points,min_x, max_x, list_sorted=False)

        convex_set = np.array(stuff)
        point_in_set = np.random.randint(max_x+1, size=2)

        print(in_hull(convex_set, point_in_set))
        #visual.visualize(stuff, exterior_set, 2, maxVal=max_x, minVal=min_x, angles=True, min_point=smallest_point, other_point=True, point_considered=point_in_set)
    """
    max_x = 4
    number_of_points = 5

    min_x = 0
    max_x = 8
    num_of_points = 5

    examples = find_examples(min_x, max_x, number_of_points, pickle_name)
  
    filtered_exmaples = filter_same_shape2(examples, 0 , 10)
    print(filtered_exmaples)
    #play_with_pickle(current_dir, min_x, max_x)

      
if __name__ == "__main__":
    main()
