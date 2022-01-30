## 1 Array Slicing
Which of the following would extract all the rows of the first 3 columns in a given numpy 2D array ‘a’?
Result: a[:, :3]

## 2 Index of 100th element
Consider an (11,12) shape array. What is the index (x,y) of the 100th element?

Note: For counting the elements go row-wise. For example, the array,

    [[1, 5, 9],

    [3, 0, 2]]

the 5th element would be '0'.

Result: (8, 3)

## 3 NumPy eye() Function
What will the output of np.eye(2, dtype = int).reshape(4, 1).T be?
Result: [[1, 0, 0, 1]]

## 4 NumPy arange() Function
What will the output of the following code be?

    import numpy as np
    a = np.arange(10)
    f = np.vectorize(lambda x: x+1)
    f(a)

Result: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## 5 Array Creation Functions
What will the output of the following line of code be?

    np.full((2,2), 1) == np.ones((2,2))

Result:
    [[True, True],
    [True, True]]

## 6 Array Functions
What will the output of the following code be?

    import numpy as np
    a = np.array( [7, 10, 2, 4, 13, 16])
    med = np.percentile(a, 50)
    print(med)

Result: 8.5
