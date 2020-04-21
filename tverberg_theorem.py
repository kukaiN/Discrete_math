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
    return combinations(product(range(min_num, max_num+1), repeat=dimensions), num_of_points)

def CCW_from_determinant(point1, point2, point3):
    return (point1[0]-point2[0])*(point3[1]-point2[1]) - (point1[1]-point2[1])*(point3[0]-point2[0])

def get_distance(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])

def make_angle_list(point_list, lowest_point):
    low_x, low_y = lowest_point
    # using atan2 because it takes the adjacient side and the opposite side separately
    # there's a division by zero for normal atan(y / x) if the point in consideration is directly above
    return [(math.atan2(point[1]-low_y, point[0]-low_x), point) for point in point_list]

def grahams_method(set_of_points, list_size, min_x = None, max_x = None, list_sorted=True):
    # getting the smallest element, O(n)
    smallest_point = set_of_points[0]
    for point in set_of_points:
        if smallest_point[1]+1>point[1] and smallest_point[0]+1 > point[0]:
            smallest_point = point

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

def main():
    current_dir = get_cd()
    num_of_points = 10
    min_x, max_x = 0 , 7
    dimensions = 2
    repetition = 10
    pickle_name = current_dir+"tverberg"
    pickle_type = ".pkl"
    """
    for i in range(repetition):
        stuff = list(set((random.randint(min_x, max_x), random.randint(min_x, max_x)) for _ in range(num_of_points)))
        exterior_set, smallest_point = grahams_method(stuff, num_of_points,min_x, max_x, list_sorted=False)
 
        #convex_set = np.random.rand(num_of_points, 2)
        #point_in_set = np.random.rand(dimensions)
        convex_set = np.array(stuff)
        point_in_set = np.random.randint(max_x+1, size=2)

        print(in_hull(convex_set, point_in_set))
        #visual.visualize(stuff, exterior_set, 2, maxVal=max_x, minVal=min_x, angles=False, min_point=smallest_point, other_point=True, point_considered=point_in_set)
    """
    max_x = 8
    number_of_points = 4
    t1 = time.time()
    points_Z2 = {(i, j) for i in range(max_x+1) for j in range(max_x+1)} 
    data_points = []
    #print(list(set_of_points(min_x, max_x, 2, number_of_points)))
    for i in (set_of_points(min_x, max_x, 2,  number_of_points)):
        if not ((0, 0) in i):
            candidate_set = [(0, 0)] + list(i)  
            break_bool = True
            for point in points_Z2 - set(candidate_set):
                if in_hull(np.array(candidate_set), np.array(point)):
                    break_bool = False
                    break
            if break_bool:
                data_points.append(candidate_set)
    if data_points != []:
        df = pd.DataFrame(data_points, columns=["p1", "p2", "p3", "p4", "p5"])
        save_pickle(pickle_name+".pkl", df)
    time_took = t1-time.time() 
    print(time_took)
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
