## 1 List Comprehension | split function
What will be the output of the following code?

    input_string = "I love Python"
    k = [(i.upper(), len(i)) for i in input_string.split(' ')]
    print(k)

Result: [(‘I’,1),(‘LOVE’,4),(‘PYTHON’,6)]

## 2 List Comprehension
What will be the output of the following code snippet?

    var = [i**2 for i in range(5)]
    print(var)

Result: [0,1,4,9,16]

## 3 Nested iteration in list comprehension
What will be the output of the following code?

    l1=[1,2,3,7]
    l2=[4,5,6,9]
    [x+y for x in l1 for y in l2]

Result: [5,6,7,10,6,7,8,11,7,8,9,12,11,12,13,16]

## 4 Functions in Python
What will be the output of the following?

    def function(n):
        n=n+1
    
    n=2
    print(function(2))

Result: No output

## 5 Functions in Python
What will be the output of the below code?

    x=10
    def func(x):
        x=20
    print(x)
    print(x)

Result:
10
10

## 6 Default parameter in Python Functions
What will be the output of the following?

    def samplefunc(msg,i=3):
        print(msg*i)
    
    samplefunc('python',4)
    samplefunc('program')

Result:
pythonpythonpythonpython
programprogramprogram

## 7 Lambda Function
What will be the output of the following program?

    f=lambda x:bool(x%2)
    print(f(100)* f(101))

Result: 0

## 8 Map Function
What will be the answer printed when the following code is executed?

    l=(1, -2, -3, 4, 5)
    def f1(x):
        return x//2
    m1=map(f1, l)
    print(list(m1))

Result: [0, -1, -2, 2, 2]

## 9 Reduce Function
What will be the output of the code below?

    from functools import reduce
    numbers = [-1, 2, -5, 3, 8,-2, 1,-4,-2]
    sum = reduce(lambda x, y: x + y, numbers)
    print(sum)

Result: 0

## 10 Assigning Map Function to a Variable
What will be the output of the following code?

    sample=[-4,2,5,-3]
    ans=map(lambda x: x*2, sample)
    print(ans)

Result: Address of ans

## 11 Typecasting to list
What will be the output of the following code snippet?

    from functools import reduce
    print(list(reduce(lambda x,y:x+y,range(5,15))))

Result: Compilation error

## 12 Logic Building
Is the output of the following two code snippets the same? Are they logically the same for any values in ‘lis’?

    import functools
    lis=[1, 2, 3, 4, 5]
    m=functools.reduce(lambda x, y:x if x<y else y, lis)
    print(m)
    lis=[1, 2, 3, 4, 5]
    c=lis[0]
    for i in range(len(lis)-1):
        if lis[i]<c:
            c=lis[i]
    print(c)

Result: Y, N

## 13 Appending to set elements
What will be the output of the following code?

    letters = ('d','i','a','s')
    ans = list(map(lambda word: f"{word}x", letters))
    print(ans)

Result: [‘dx’, ‘ix’, ‘ax’, ’sx’]

## 14 Filter Function
Read the following code. Select from the given options the length of the list printed. (Do not run it on the notebook. Try solving manually.)

    def sf(a):
        return a%4==0 and a%8!=0
    m=filter(sf, range(10, 31))
    print(list(m))

Result: 3
