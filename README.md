# Discrete_math
 some stuff that's related to discrete math in Python



recurrence relation of generating integer points for programs that only cares about orientation

for the integer tvergberg tolerance problem there are 4 + 1 parameters (the additional one , LL, is required to contain the brute force search)

| symbol | meaning | relationships |
|--|--|--|
| d | dimension | affect the size of the point |
| n | number of points | proportional to computation and storage space |
| t | tolerance | parameter that detemine if the collection of points is an example or not |
| k | number of partitions | partition the points into k sets |
| LL | latice length | the length of one dimension of the grid, defines the search space in Z^d space, the grid made by this is of size (LL + 1) * (LL + 1)| 


there are few functions that we need to define:
1. ) generate the points that is simple enough and minimizes the number of different orientations and doesnt include sets that are of a smaller case (brute force)
2. ) make a boolean matrix that differentiate the exaples and non-examples, also the matrix have to be stored in an efficient way
3. ) its required to build the base case before computing a matrix of a bigger magnitude (idea from DP)
4. ) ***effiecient method of checking the tolerance given n points (currently brute force, maybe theres a better method)



## Storing values and ideas

since the main idea is to reduce the number of computation and storage, we will come up with this example

| Example |  Value |
|--|--|
|LL | 6 ==> 7 x 7 grid |
| n | 7 |
|t | 1 |
| k | 2|
|d | 2 |

since t, k, d are constants in this iteration, we only need to care about the bigger cases

for some parameter LL, n and dimension 2, we can reduce the number of points to generate by fixing two points on the LL x LL grid: one point on the top row and the second on the first half of the bottom row.  After fixing 2 points, then we can generate all the combination of n-2 points on the grid.  Then make a LL by LL/2 grid where the column and rows represent the two fixed points and a cell of the d dimensional table represent the bool for the tolerance question by fixing two points.


Example of the LL* LL/2 grid: ( entries will be a matrix that points to a smaller case)

|    | (0, LL) | (1, LL) | (2, LL) | ... | (LL-1, LL) | (LL, LL)|
|----|---------|---------|---------|-----|---------|---------|
| (0,0) |  |  |  |  |  | |
| (1, 0) |  |  |  |  |  | |
| (2, 0) |  |  |  |  |  | |
| (3, 0) |  |  |  |  |  | |
|   ...   |  |  |  |  |  | |
|(ceil(LL/2) - 1, 0) |  |  |  |  |  | |
|(ceil(LL/2), 0)|  |  |  |  |  |


## search space
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

## other ideas


everything below will be the smallest case that we need to check for the integer tolerance (dimension = 2, tolerance level = 1, point = 7)

fix 2 points, then find all the combinations of 5 points in the restricted search space of the LL x LL grid.

then the growth factor of the original problem (2^n)  * (LL^2 choose n-2) * (1/2 * n^2)  *  ( O(n * log n) * LL^1.5 (log n))


2^7 = 128
| LL size | grid size | number of points removed with the trapezoid/square method | # of test cases | # number of operations (# of test cases * 128) | % of points saved by trapezoid/square method | 
|---------|----------|-----------------|----------|----------|-----|
| 4         | 25 | 5 | 52,414 | 6,708,992 | 5/25 = 20% |
| 5         | 36 | 9 | 546,017 | 69,890,176 | 9/36 = 25% |
| 6         | 49 | 11 | 4,645,396 | 594,610,688 | 22% |
| 7         | 64 | 17 | 22,694,492 | 2,904,894,976 | 27% |
| 8         | 81 | 20 | 109,544,061 | 14,021,639,808 | 24% |
| 9         | 100 | 28 | ... | ... | 28% | 