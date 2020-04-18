import matplotlib.pyplot as plt
import numpy as np
import random
import itertools

def visualize(points, convex_border, dimensions, maxVal=None, minVal=None, linestyles=["r.","b-", "rx"], ticks=[5, 1], angles=False, min_point = [0,0]):
    if maxVal == None: maxVal = max(max(points, key = lambda a: a[0]), max(points, key = lambda a: a[1]))
    if minVal == None: minVal = min(min(points, key = lambda a: a[0]), min(points, key = lambda a: a[1]))
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
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
    plt.show()


def main():
    #for points in [itertools.product]:
    #    pass
    pass

if __name__ == "__main__":
    main()
