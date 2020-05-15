# Discrete_math
 some stuff that's related to discrete math in Python



recurrence relation of generating integer points for programs that only cares about orientation

for the integer tvergberg tolerance problem there are 4 + 1 parameters (the additional one , ll, is required to contain the brute force search)

| symbol | meaning | relationships |
|--|--|--|
| d | dimension | affect the size of the point |
| n | number of points | proportional to computation and storage space |
| t | tolerance | parameter that detemine if the collection of points is an example or not |
| k | number of partitions | partition the points into k sets |
| ll | latice length | the length of one dimension of the grid, defines the search space in Z^d space, the grid made by this is of size (ll + 1) * (ll + 1)| 


there are few functions that we need to define:
1.) generate the points that is simple enough and minimizes the number of different orientations and doesnt include sets that are of a smaller case (brute force)
2.) make a boolean matrix that differentiate the exaples and non-examples, also the matrix have to be stored in an efficient way
3.) its required to build the base case before computing a matrix of a bigger magnitude (idea from DP)
4.) ***effiecient method of checking the tolerance given n points (currently brute force, maybe theres a better method)

since the main idea is to reduce the number of computation and storage, we will come up with this example

example:
7 x 7 grid ==> ll = 6
7 points ==> n = 7
t = 1
k = 2
d = 2

since t, k, d are constants in this iteration, we only need to care about the bigger cases

for some parameter ll, n and dimension 2, we can reduce the number of points to generate by fixing two points on the ll x ll grid: one point on the top row and the second on the first half of the bottom row.  After fixing 2 points, then we can generate all the combination of n-2 points on the grid.  then for each combinations of the two points

|    | (0, ll) | (1, ll) | (2, ll) | ... | (ll, ll)|
|----|---------|---------|---------|-----|---------|
| (0,0) |  |  |  |  |  |
| (1, 0)|  |  |  |  |  |
| (2, 0)|  |  |  |  |  |
|   .   |  |  |  |  |  |
|   .   |  |  |  |  |  |
|   .   |  |  |  |  |  |
|(ceil(ll/2), 0)|  |  |  |  |  |

since the search space is going to be the shape below, we will use two generators,
 one for the points in the square and one for the skewed trapezoidal shape
    
    6    __________________
    5   |                /
    4   |              /    
    3   |___________ /       
    2   |          |
    1   |          |
    0   |__________|
        0  1  2  3  4  5  6
    
the top row and bottom row will each have one fixed point and no point greater than it 

