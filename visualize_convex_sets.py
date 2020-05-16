import matplotlib.pyplot as plt
import numpy as np
import random
import itertools

def Max_Min_of_tuple(points):
    max_value = points[0][0]
    min_value = points[0][0]
    for point in points:
        for coordinate_value in point:
            if coordinate_value > max_value:
                max_value = coordinate_value
            if coordinate_value < min_value:
                min_value = coordinate_value
    return (max_value, min_value)

def visualize(points, convex_border, dimensions,
            maxVal=None, minVal=None, linestyles=["rx","b-", "bx"], ticks=[5, 1], angles=False, min_point = [0,0], other_point=False, point_considered=[0,0], save_plt=False, filename="default.png"):
    if maxVal == None: maxVal = Max_Min_of_tuple(points)[0]
    if minVal == None: minVal =  Max_Min_of_tuple(points)[1]
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    if other_point:
        minVal = min(minVal, min(point_considered))
        maxVal= max(maxVal+1, max(point_considered))
    print(minVal, maxVal)
    major_ticks = np.arange(minVal, maxVal+1, ticks[0])
    minor_ticks = np.arange(minVal, maxVal+1, ticks[1])
    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)
    ax.grid(which="both")

    x_points, y_points = [a[0] for a in points], [a[1] for a in points]
    conv_x_points, conv_y_points = [a[0] for a in convex_border], [a[1] for a in convex_border]
    plt.plot(x_points, y_points, linestyles[0])
    plt.plot(conv_x_points, conv_y_points, linestyles[1])
    plt.plot(conv_x_points, conv_y_points, linestyles[2])
    if angles:
        for x, y in zip(x_points, y_points):
            x_list = [min_point[0], x]
            y_list = [min_point[1], y]
            plt.plot(x_list, y_list, "--r")
    if other_point:
        plt.plot(point_considered[0], point_considered[1], "yx")
    if save_plt:
        plt.savefig(filename)
    else:
        plt.show()

def save_examples(examples):
    """
    examplesss = [[(0, 0), (0, 1), (1, 0), (2, 3), (3, 2)], [(0, 0), (0, 1), (1, 2), (2, 0), (3, 2)], [(0, 0), (0, 1), (1, 2), (3, 0), (3, 2)], 
    [(0, 0), (0, 1), (1, 3), (2, 0), (3, 2)], [(0, 0), (0, 1), (1, 3), (3, 0), (3, 2)], [(0, 0), (0, 1), (2, 0), (2, 3), (3, 2)], [(0, 0), (0, 1), (2, 3), (3, 0), (3, 2)], 
    [(0, 0), (0, 2), (1, 0), (2, 1), (2, 3)], [(0, 0), (0, 2), (1, 0), (2, 3), (3, 1)], [(0, 0), (0, 2), (1, 0), (2, 3), (3, 2)], [(0, 0), (0, 2), (1, 3), (2, 0), (2, 3)],
    [(0, 0), (0, 2), (1, 3), (2, 1), (2, 3)], [(0, 0), (0, 2), (1, 3), (2, 1), (3, 3)], [(0, 0), (0, 2), (1, 3), (2, 3), (3, 0)], [(0, 0), (0, 2), (1, 3), (2, 3), (3, 1)], 
    [(0, 0), (0, 2), (1, 3), (3, 0), (3, 1)], [(0, 0), (0, 2), (1, 3), (3, 0), (3, 3)], [(0, 0), (0, 2), (2, 0), (3, 1), (3, 2)], [(0, 0), (0, 2), (2, 2), (3, 0), (3, 1)], 
    [(0, 0), (0, 2), (2, 3), (3, 0), (3, 1)], [(0, 0), (0, 3), (1, 0), (2, 1), (2, 3)], [(0, 0), (0, 3), (1, 0), (2, 3), (3, 1)], [(0, 0), (0, 3), (1, 0), (2, 3), (3, 2)], 
    [(0, 0), (0, 3), (1, 3), (2, 0), (2, 2)], [(0, 0), (0, 3), (1, 3), (2, 0), (3, 1)], [(0, 0), (0, 3), (1, 3), (2, 0), (3, 2)], [(0, 0), (0, 3), (2, 0), (3, 1), (3, 2)], 
    [(0, 0), (0, 3), (2, 0), (3, 1), (3, 3)], [(0, 0), (0, 3), (2, 3), (3, 0), (3, 2)], [(0, 0), (0, 3), (2, 3), (3, 1), (3, 2)], [(0, 0), (1, 2), (2, 0), (3, 1), (3, 2)], 
    [(0, 0), (1, 2), (2, 0), (3, 1), (3, 3)], [(0, 0), (1, 3), (2, 0), (3, 1), (3, 2)], [(0, 0), (1, 3), (2, 3), (3, 0), (3, 2)], [(0, 0), (0, 1), (1, -1), (2, 1), (3, -1)], 
    [(0, 0), (0, 1), (1, -1), (2, 2), (3, -1)], [(0, 0), (0, 1), (1, -1), (3, -1), (3, 1)], [(0, 0), (0, 1), (1, -1), (3, -1), (3, 2)], [(0, 0), (0, 1), (1, 2), (2, -1), (3, 2)],
    [(0, 0), (0, 1), (1, 2), (3, -1), (3, 2)], [(0, 0), (0, 2), (1, -1), (2, -1), (2, 1)], [(0, 0), (0, 2), (1, -1), (2, -1), (2, 2)], [(0, 0), (0, 2), (1, -1), (2, -1), (3, 1)],
    [(0, 0), (0, 2), (1, -1), (2, -1), (3, 2)], [(0, 0), (0, 2), (1, -1), (2, 1), (3, -1)], [(0, 0), (0, 2), (1, -1), (3, -1), (3, 2)], [(0, 0), (0, 2), (1, -1), (3, 1), (3, 2)], 
    [(0, 0), (0, 2), (1, 2), (2, -1), (2, 1)], [(0, 0), (0, 2), (1, 2), (2, -1), (3, 0)], [(0, 0), (0, 2), (1, 2), (2, -1), (3, 1)], [(0, 0), (0, 2), (2, -1), (3, 1), (3, 2)], 
    [(0, 0), (1, -1), (1, 2), (3, 1), (3, 2)], [(0, 0), (1, -1), (2, 2), (3, -1), (3, 2)], [(0, 0), (1, -1), (2, 2), (3, 0), (3, 2)], [(0, 0), (1, -1), (2, 2), (3, 1), (3, 2)],
    [(0, 0), (1, 2), (2, -1), (3, -1), (3, 1)], [(0, 0), (1, 2), (2, -1), (3, -1), (3, 2)], [(0, 0), (1, 2), (2, -1), (3, 1), (3, 2)], [(0, 0), (1, 2), (2, 2), (3, -1), (3, 1)],
    [(0, 0), (0, 1), (1, -2), (2, 1), (3, -1)], [(0, 0), (0, 1), (1, -2), (3, -1), (3, 1)], [(0, 0), (0, 1), (1, 1), (2, -2), (3, -1)], [(0, 0), (0, 1), (2, -2), (2, 1), (3, -1)], 
    [(0, 0), (0, 1), (2, -2), (3, -1), (3, 1)], [(0, 0), (1, -2), (1, 1), (3, -2), (3, -1)], [(0, 0), (1, -2), (2, -2), (3, -1), (3, 1)], [(0, 0), (1, -2), (2, 0), (3, -2), (3, -1)],
    [(0, 0), (1, -2), (2, 1), (3, -2), (3, -1)], [(0, 0), (1, -2), (2, 1), (3, -2), (3, 1)], [(0, 0), (1, -2), (2, 1), (3, -1), (3, 1)], [(0, 0), (1, 1), (2, -2), (3, -2), (3, -1)], 
    [(0, 0), (1, 1), (2, -2), (3, -2), (3, 0)], [(0, 0), (1, 1), (2, -2), (3, -2), (3, 1)], [(0, 0), (1, -3), (2, -3), (3, -2), (3, 0)], [(0, 0), (1, -3), (2, 0), (3, -2), (3, -1)],
    [(0, 0), (1, -2), (2, 0), (3, -3), (3, -1)]]
    """
    return
    base_name = "set_with_5_points_"
    foldername = "collection_of_examples\\"
    for counter, sets in enumerate(examplesss):
        name = foldername + base_name + str(counter) + ".png"
        visualize(sets, sets, 2, save_plt=True, filename=name) 

def main():
    #for points in [itertools.product]:
    pass

    
     
if __name__ == "__main__":
    main()
