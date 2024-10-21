### __Python lesson 2__
- Student name: __Jiří David__
- Student number: __X1131401__


```python
type("Hello")
```




    str




```python
type(11.3)
```




    float




```python
type(11)
```




    int




```python
type("c")
```




    str




```python
float("2.0")
```




    2.0




```python
x = 10
float(x) #This is refered as type casting, where we transfer the variable to the specific type
x = float(x)
x
```




    10.0




```python
int(1.1)
```




    1



# __Data Types__ 
Basic datatypes in python are __int__, __float__, __string__ and __bool__
to make it easeier lets reference to the __string__ as __*char__ from C language

Let's write some examples:
- int = `1`;
- float = `10.3`;
- string = `"String"`;
- bool = `True`;
- bool = `1`;

__Booleans have first letter always upper case! True/ False__ and can be also represtented by __0 for False__ or __1 for True__

When we declare variable let's say `x = 10` we can manipilate it by declaring `x = 11` __this will override original value__, same cane be done with data types. If we currently execute `type(x)` we recieve `int`. We can do `x = float(x)` and we recieve `x = 11.0` __remeber we changed the value from `10` to the `11`__. If now do `type(x)` we will recieve float. This is easy way how to switch between datatypes of variable.



```python
#For the coment above
x = 10
print(f"first iteration of x is: {x}\n")
x = 11
print(f"After changing x to 11 we get: {x}\n")
print(f"Now we get the type of x: {type(x)}\n")
x = float(x)
print(f"Now after changing data type we get that x is: {type(x)}\n")
```

    first iteration of x is: 10
    
    After changing x to 11 we get: 11
    
    Now we get the type of x: <class 'int'>
    
    Now after changing data type we get that x is: <class 'float'>
    
    


```python
#int("A")
#Int to string doesn't work with the alphabet
int("2")
#However works with numbers
#string(5.5) works too boviously
```




    2




```python
#Booleans are handled by the True/False statments. It is IMPORTANT to use upper case T/F
type(True) #type(False) has same result 

```




    bool




```python
int(True) #True is considered logical value of 1
```




    1




```python
float(False) #False is considered as the logical value of 0
```




    0.0




```python
bool(1)
```




    True




```python
bool(0) #As explained above
```




    False




```python
#Arithmetic operations examples
100+132+111+33
#Each segment - + are called operators
#The 100 132 111 33 are Operands
```




    376




```python
100 - 2000
# We can go to the negative values too
```




    -1900




```python
25/6
```




    4.166666666666667




```python
100*3
```




    300



### We can do basic algebraic operations as is `+ - / *` we can also use `//` that will force the output to be integer


```python
25 // 5
```




    5




```python
25//6
```




    4




```python
#Double slash // double division forces the integer - Integer division
```


```python
100*100+5
```




    10005




```python
5+100*100
```




    10005




```python
#The Python respects rules of algebra, () First then * / and lastly + -
(100+5)*100
```




    10500




```python
#Variables
x = 10
y= "String"
type(y)
```




    str




```python
#Rewriting of variables is possible too, we can perform following tasks:
x = 10
print(f"x original value is: {x}\n")
x = x+1
print(f"Variation x = x + 1 : {x}\n")
x = x / 2
print(f"Variation x = x / 2: {x}\n")
```

    x original value is: 10
    
    Variation x = x + 1 : 11
    
    Variation x = x / 2: 5.5
    
    

## __There is excercise for today's lesson__

We can use `#` to write a coment, and `//` or `/* */` equivalent in __C__

Compiler gives us really nice idea when we make a mistake.
For example: `drint("Hello")`
"NameError                                 Traceback (most recent call last)
Cell In[147], line 1
----> 1 drint("Hello")

NameError: name 'drint' is not defined"

Gives us good understanding on which __line__ error occured, what is wrong and how we might correct it. In this case we have typo in declaration, so just slight corrction gets rid of error. So changing `drint("Hello")` to `print("Hello")` gets job done.


If we have multiple lines of code like at [179](#179) we can see `drint("Hello")` is __commented out__. As you can see in the coment, the `print("Pea")` __will be executed but the next lines will be ignored.__ Upon reaching an erro python procrsses __Break__ (C function) and ends the program.


We can later see when we execute `type(6/2)` we get a `float`. To enforce type `int` we need to use `type(6//2)` as can be seen below [233](#232)



```python
# EXCERCISE BELOW
import sys

def pyVersionControl():
    print(f"{sys.version}\n\n") #To ensure we use python 3.0 +

def showcaseNum():
    a = [1, 2, 3.13, 7.12, "Dog", "Ice cream", 11, "Python", True, False]
    for i in range(0, len(a), 1):
        print(f" {a[i]} has type: {type(a[i])}")

def main():
    pyVersionControl()
    showcaseNum()

main()
    
```

    3.12.4 | packaged by Anaconda, Inc. | (main, Jun 18 2024, 15:03:56) [MSC v.1929 64 bit (AMD64)]
    
    
     1 has type: <class 'int'>
     2 has type: <class 'int'>
     3.13 has type: <class 'float'>
     7.12 has type: <class 'float'>
     Dog has type: <class 'str'>
     Ice cream has type: <class 'str'>
     11 has type: <class 'int'>
     Python has type: <class 'str'>
     True has type: <class 'bool'>
     False has type: <class 'bool'>
    


```python
print("Pea")
#drint("Hello")# <- This is the error line, code won't execute fruther, but the print("Pea") will be executed
print("Hello")
```

    Pea
    Hello
    


```python
print(type(6/2))
print(type(6//2))
```

    <class 'float'>
    <class 'int'>
    


```python

```
