## 1 Lists
What is the output of the following?

    s = 'a$b@c@d'
    print(s.split('@','$'))

Result: Compilation error

## 2 Lists
What is the code to print the element ‘banana’?

    fruits = ['apple', 'mango', ['grapes', 'papaya'], ('banana', 'pomegranate')]

Result: fruits[3][0]

## 3 Lists
Find the output of the following code.

    list_1 = ['red' , 'orange', 'blue', 'green', 'black', 'white']
    print(list_1.sort())

Result: None

## 4 Lists
What will the output of the following code be?

    num_1=[9,4,2,7]
    num_2=[8,3,6,1]
    print(sorted(num_1))
    print(num_1)
    print(num_2.sort())
    print(num_2)

Result:
[2,4,7,9]
[9,4,2,7]
None
[1,3,6,8]

## 5 Tuples
Find the output of the following code.

    l = ['paris','india','china','london']
    print(tuple(l+['sri lanka']))

Result: ('paris','india','china','london','sri lanka')

## 6 Tuples
What is the output of the following code?

    var=(5)
    print(type(var))

Result: int

## 7 Tuples
What is the output of the code given below?

    tup=([1,3,5],"abcd",(2,4),6)
    tup[0][2]=7
    print(tup)

Result: ([1,3,7], "abcd", (2,4), 6)

## 8 Sets
What will the output of the following code be?

    a= {1,2,4,5}
    b= {5,6,7,8}
    print(a-b)

Result: {1,2,4}

## 9 Sets
What will the output of the following code be?

    s= {3,4,5}
    s*2

Result: Error in operand type

## 10 Sets
What is the output of the following code?

    numbers= {1,0,6,1,4,0,7}
    print(len(numbers))

Result: 5

## 11 Dictionaries
What will the output of the following Python code be?

    dict= {'ab':12,'cd':34,'ef':56}
    print(dict[1])

Result: error

## 12 Dictionaries
What will the output of the following code be?  

    marks= {'John':45,'Alex':60}
    print(marks.keys())

Result: dict_keys(['John', 'Alex'])

## 13 Dictionaries
What is the output of the following code?

    d = {"Python":40, "R":45}
    "Python" in d

Result: True

## 14 Looping through data structures
What will the output of the following code be?

    input_dict= {1:"one",2:"two",3:"three"}
    for i in input_dict:
      print(i)

Result:
1
2
3

## 15 Looping through data structures
Find the output of the following code snippet.

    input_str="I love programming in python"
    count=0
    l=['a','e','i','o','u']
    for i in input_str.lower():
      if i in l:
      	count=count+1
    print(count)

Result: 8