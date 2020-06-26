from itertools import product, combinations

def doignonTheorem():
    pass



def sample_points(LL = 5, n = 7):
    # ll is the grid size, this function makes generators that returns n points sampled on a LL by LL grid that is suitable for tolerance
    # we only care about generating points to make all orientation ignoring simple transformation on the integer lattice (rotation, reflection, and the combination of them)
    # hence we ignore some of the sampling, this decreases the number of sets of test points
    # half_x = int((ll+1)/2)
    # 
    # one point is on top_row
    # one point is on the bottom_row

    top_row = [(i, LL) for i in range(LL+1)]
    top_point = (0, LL) # this will be incremented

    sample_space = [(i, j) for i in range(LL+1) for j in range(LL)] # a square that doesnt include the top row

    generator_added = combination(search_space, n-2)
# this file uses cupy and uses the GPU to calculate tolerance problems




def tolerance_cuda(n = 7, ll = 4, t = 1, k = 2, d = 2):
    # make use of a bound (one loop)
    # use itertools to generate the points, stored in memory (second loop)
    # itetools to make all the samples of n points from the possible points
    # 
    # pass the possible points into a generator called partitioner() (third loop)
    #
    # this would make all the possible partition, 
    # set_a and set_b passed to andrew's monotone chain

    # use the max and min to find the boundaries, if the x max < x min or y max < y min then there's no intersection
    # if there's a possible intersection, we know the bottom left corner and the x and y bounds, so we can generate all the points in a small grid that could be in the intersection
    # then check if the partition is broken or not
    
    



def main():
    tolerance_cuda()




if __name__ == "__main__":
    main()