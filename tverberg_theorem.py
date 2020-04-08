from itertools import combinations, product

def set_of_points(min_num, max_num, dimensions, num_of_points):
    return combinations(product(range(min_num, max_num+1), repeat=dimensions), num_of_points)

def check_tverberg(list_of_points, num_of_points):
    for index, list_b in enumerate(list_of_points):
        if index %10000 == 0:print("working on", index)
        if check_size1(list_b, num_of_points):
            yield list_b
    print(index)


def check_tverberg2(list_of_points, num_of_points):
    for index, list_b in enumerate(list_of_points):
        if index %100000 == 0:print("working on", index)
        if check_size2(list_b, num_of_points):
            yield list_b
    print(index)

def check_size1(list_of_points, size):
    check = True
    for i in range(size-1):
        if check:
            for j in range(i+1, size):
                point_a = list_of_points[i] 
                point_b = list_of_points[j]
                for a, b in zip(point_a, point_b):
                    if a == b: check = False
    return check


def check_size2(list_of_points, size):
    return len(set(list_of_points)) == size 

def main():
    max_num = 7
    min_num = 0
    dimensions = 2
    num_of_points = 5
    for a in check_tverberg(set_of_points(min_num, max_num, dimensions, num_of_points), num_of_points):
        pass
    print("finished")


import time

t1 = time.time()
nump = 5
for i, a in  enumerate(set_of_points(0, 10, 2, nump)):
    pass
print(i)
print(time.time() - t2)
"""
for a in check_tverberg(ls, nump):
    pass
t2 = time.time()
print(t2-t1)
ls = set_of_points(0, 10, 2, nump)
for a in check_tverberg2(ls, nump):
    pass
print(time.time()-t2)

#if __name__ == "__main__":
#    main()
"""