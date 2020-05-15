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

This method will be abbreviated as the t/s method, standing for trapezoid/square method for saving computation

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
| LL size | grid size | # of points removed with the t/s method | # of test cases | # number of operations (# of test cases * 128) ** 2^7 = 128| % of points saved by t/s method | 
|---------|----------|-----------------|----------|----------|-----|
| 4         | 25 | 5 | 52,414 | 6,708,992 | 5/25 = 20% |
| 5         | 36 | 9 | 546,017 | 69,890,176 | 9/36 = 25% |
| 6         | 49 | 11 | 4,645,396 | 594,610,688 | 22% |
| 7         | 64 | 17 | 22,694,492 | 2,904,894,976 | 27% |
| 8         | 81 | 20 | 109,544,061 | 14,021,639,808 | 24% |
| 9         | 100 | 28 | ... | ... | 28% | 

the 128 exist to represent the number of 2 partitions possible, we dont care about cases with 1 point and 6 point being a partitions (reasoning somewhere), but we keep 128 as an upperbound of the calculation

- for each opperations above we need to do find the border of the partitioned convex set, which is O(logn * n) using Andrew's monotone chain algorithm
- then we use the algorithm (1) designed below that takes O(log n) to check if a point p is in the convex set or not
- Let A and B be the two partitioned set, We can reduce the number of points to check by finding the boundary of a smaller grid where the intersection would be if it exist (min( max Ax, max Bx) , min( max Ay, max By) , max( min Ax, min Bx) , max( min Ay, min By))
- then iterate the grid and check membership with set A, keep the integer points in set A, call it Set_A
- then iterate Set_A and check membership with B to check tolerance

calculation 
-  there are 128 ways to partition 7 points 
- (LL^2)/2 ways of choosing two fixed point on the bounded LL x LL grid 
- (LL^2 choose 5) ways of getting 5 points from the LL x LL grid
- for each partition, takes O(n * log n) to find the set's boundary
- O(log n) to check membership of a point
- multiply by a small consant factor for the grid made by searching for the intersection

after multiplying all of the above, we get  (2^n)  * (LL^2 choose n-2) * (1/2 * n^2)  *  ( O(n * log n) * LL^1.5 (log n))



## Algorithm explanation:

### Andrew's monotone chain
sort points by the coordinate, then find the top part of the hull, then find the bottom border of the hull, then join the border

similar to graham's scan, but since we dont have to calculate the angle, this is faster.

the runtime of O(n * log n) comes from the sorting, if the points are sorted, then it is easy to find the next point that makes the top or bottom border

### algorithm (1) , I dont know the name for this
draw a line from one point on the convex hull to the point, p, that we want to check membership. 

** the cross product's sign tells us if the second vector is on the left or the right of the vector

we use the fact above to do a divide and conquer algorithm to find the 3 points on the set, that makes a triangle, then check if the point in question is on the same direction for all 3 sides

the divide and conquer decreases the number of test cases by 2 at each step so the runtime is O(log n)


