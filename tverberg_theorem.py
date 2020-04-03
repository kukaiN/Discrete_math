import itertools


def check_tverberg(list_of_points):
    list_to_check = []
    point_in_list = 11
    for index, list_b in enumerate(itertools.combinations(list_of_points, point_in_list)):
        if index %10000 == 0:print("working on", index)
        check = True
        for i in range(point_in_list-1):
            if check:
                for j in range(i+1, point_in_list):
                    point_a = list_b[i] 
                    point_b = list_b[j]
                    for a, b in zip(point_a, point_b):
                        if a == b: check = False
        if check:
            yield list_b
    print(index)
    print(len(list_to_check))

max_num = 7
small_num = 4
list_of_points = itertools.product(range(small_num), range(small_num), range(max_num)) 
for a in check_tverberg(list_of_points):
    pass
print("finished")
