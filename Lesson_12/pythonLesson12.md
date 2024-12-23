```python
#Functions
#[Are optional]
#(are reqired)

import time
def timerz(param):
    print("Loading please wait.\n")
    for i in range(param):
        print(f"{param - i}\n", end="...")
        time.sleep(1)
    return 0
timerz(10)

```

    Loading please wait.
    
    10
    ...9
    ...8
    ...7
    ...6
    ...5
    ...4
    ...3
    ...2
    ...1
    ...




    0




```python
def min(a,b):
    if a>b:
        return b
    else:
        return a
x = min(10,12)
print(x)


```

    10
    


```python
a = int(input("Enter a size of a: "))
b = int(input("Enter a size of b: "))

def area(a,b):
    return a*b
area(a,b)
```




    400




```python
def add(a):
    """Documentation
    This function adds two numbers together.
    Parameters:
    a
    """
    
    b = a + 1
    print(b)
    return b
for i in range(10):
    add(i)
    
```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    


```python
help(add)
```

    Help on function add in module __main__:
    
    add(a)
        Documentation
        This function adds two numbers together.
        Parameters:
        a
    
    


```python
def multiply(a,b):
    c = a * b
    return c
    #print("This won't be printed")
result = multiply(10,"Joe \n")
print(result)
```

    Joe 
    Joe 
    Joe 
    Joe 
    Joe 
    Joe 
    Joe 
    Joe 
    Joe 
    Joe 
    
    


```python
import math
pi = math.pi
def circle(radius):
    area = pi * radius**2
    lenght = pi * radius*2
    return area, lenght
print(circle(5))
```

    (78.53981633974483, 31.41592653589793)
    


```python
def square(a):
    """Documentation
    this just square roots input and adds one
    not much to it
    """
    b = 1
    c = a*a+b
    print(a, " if you square + 1 ", c)
    return c

square(5)
help(square)
```

    5  if you square + 1  26
    Help on function square in module __main__:
    
    square(a)
        Documentation
        this just square roots input and adds one
        not much to it
    
    


```python
def MJ():
    print("Michael jackson")
    
def MJ2():
    print("Michael jackson")
    return None

MJ()
MJ2()
```

    Michael jackson
    Michael jackson
    


```python
album_ratings = [100, 98, 12, 30,50,60,70,76,74,33]
sum(album_ratings)
len(album_ratings)
average = sum(album_ratings)/len(album_ratings)
print(average)
print(len(album_ratings))
print(sum(album_ratings))
```

    60.3
    10
    603
    


```python
def type_of_almbum(artist, almbum, year_released):
    print(artist, almbum, year_released)
    if int(year_released) > 1980:
        return "Modern"
    else:
        return "Older"

x =type_of_almbum("Michael Jacskon", "Thriller", "1980")
print(x)
```

    Michael Jacskon Thriller 1980
    Older
    


```python
string_1 = "Michael Jackson is the best"

def checkstring(text):
    if text in string_1:
        return "Matching"
    else:
        "Mismatch"
        
checkstring("is the best")
```




    'Matching'




```python
def compare_strings(x,y):
    if x == y:
        return 1
    
string_2 = string_1

check = compare_strings(string_1,string_2)
if check == 1:
    print("\n Matching strings")
else:
    print("\n Mismatch")
    
```

    
     Matching strings
    
