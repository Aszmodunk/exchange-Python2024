# Today's topic: 

review for the midterm test
`important!`


```python
a = 3
b = 2 
if a > 5 or b < 7:
    print(a)
```


```python
if (a > 2):
    print(1)
if a > 2:
    print(2)
if (a > 2 or a <6):
    print(3)
if a > 2 and not a <6:
    print(4)
```


```python
#Ambulance
#Nursing 700/hr, Doctor 1 500/hr
#We need to input km, if nursing staff or doctor is needed on board
#avg speed je 60km/hr


nurse = 700
doctor = 1500

km = int(input("Km?: \n"))
basicFee = 800 + (km*25)

print("What staff is required? \n1) Nursing\n2) Doctor\n3) Both\n")
staff = int(input())

hrs = km//60 #Defined Hrs

if km%60 != 0: # If there is some 0.123123123 it will take a hrs and add extra hour
    hrs = hrs +1
    

staffFee = 0
if staff == 1:
    staffFee = nurse
elif staff == 2:
    staffFee = doctor
elif staff == 3:
    staffFee = nurse + doctor

finalCost = hrs*staffFee + basicFee #For 20 km both should be 3500
print(f"{basicFee} - BasicFee")

print(finalCost)
```

## Two way condition
Tell code what to do if the `if` is not *true* handled by the condition `else`



```python
def ins(val):
    if val >= 0:
        return "The input value is greater or equal to 0"
    else:
        return "The input value is less than 0"
    
def trials():
    for i in range(-11,11):
        print(ins(i))

trials()
# if int(input()) >= 0:
#     print("The input value is greater or equal to 0")
# else:
#     print("The input value is less than 0")
```


```python
import random as rn
a = rn.randint(1,20)
b = 6
c = 8
if a >10:
    print(a)
else:
    print(b)
print(c)
```


```python
#PRactice
#Allow user to input integer, and determine if its odd or even
a = int(input("Enter a number: "))
if a%2 == 0:
    print(f"{a} is an even number")
else:
    print(f"{a} is an odd number")
```


```python
grade = int(input("Enter a grade: "))
if grade>=60:
    print("You passed good job!")
else:
    print("You didn't pass, try again")
```


```python
id = "X1000001"
pswd = "0857"
login = input("Enter your login name: ")
guess = input("password: \n")
if guess != pswd or login != id:
    print("Wrong 1")
else:
    print("Welcome 1")

if guess == pswd and login == id:
    print("Welcome 2")
else:
    print("Wrong 2")
```

Elif function


```python
a = -5
if a>10:
    print("A")
elif(a>5):
    print("B")
elif(a>0):
    print("c")
else:
    print("d")
```


```python
# input 0-100
# 90+ A, 80+ B, 70+ C 60 D <F

grade = int(input("Enter a grade: "))

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D") 
else:
    print("F")
```


```python
#BMI
weight = int(input("Enter a weight [kg]: "))
height = int(input("Enter a height [cm]: "))
height = height / 100
bmi = weight / (height * height)
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
else:
    print("Overweight")
    
print(bmi)
```

    Normal
    21.64412070759625
    


```python
for i in range(0,100):
    print(f"I want to be rich {i+1} times!")
```

    I want to be rich 1 times!
    I want to be rich 2 times!
    I want to be rich 3 times!
    I want to be rich 4 times!
    I want to be rich 5 times!
    I want to be rich 6 times!
    I want to be rich 7 times!
    I want to be rich 8 times!
    I want to be rich 9 times!
    I want to be rich 10 times!
    I want to be rich 11 times!
    I want to be rich 12 times!
    I want to be rich 13 times!
    I want to be rich 14 times!
    I want to be rich 15 times!
    I want to be rich 16 times!
    I want to be rich 17 times!
    I want to be rich 18 times!
    I want to be rich 19 times!
    I want to be rich 20 times!
    I want to be rich 21 times!
    I want to be rich 22 times!
    I want to be rich 23 times!
    I want to be rich 24 times!
    I want to be rich 25 times!
    I want to be rich 26 times!
    I want to be rich 27 times!
    I want to be rich 28 times!
    I want to be rich 29 times!
    I want to be rich 30 times!
    I want to be rich 31 times!
    I want to be rich 32 times!
    I want to be rich 33 times!
    I want to be rich 34 times!
    I want to be rich 35 times!
    I want to be rich 36 times!
    I want to be rich 37 times!
    I want to be rich 38 times!
    I want to be rich 39 times!
    I want to be rich 40 times!
    I want to be rich 41 times!
    I want to be rich 42 times!
    I want to be rich 43 times!
    I want to be rich 44 times!
    I want to be rich 45 times!
    I want to be rich 46 times!
    I want to be rich 47 times!
    I want to be rich 48 times!
    I want to be rich 49 times!
    I want to be rich 50 times!
    I want to be rich 51 times!
    I want to be rich 52 times!
    I want to be rich 53 times!
    I want to be rich 54 times!
    I want to be rich 55 times!
    I want to be rich 56 times!
    I want to be rich 57 times!
    I want to be rich 58 times!
    I want to be rich 59 times!
    I want to be rich 60 times!
    I want to be rich 61 times!
    I want to be rich 62 times!
    I want to be rich 63 times!
    I want to be rich 64 times!
    I want to be rich 65 times!
    I want to be rich 66 times!
    I want to be rich 67 times!
    I want to be rich 68 times!
    I want to be rich 69 times!
    I want to be rich 70 times!
    I want to be rich 71 times!
    I want to be rich 72 times!
    I want to be rich 73 times!
    I want to be rich 74 times!
    I want to be rich 75 times!
    I want to be rich 76 times!
    I want to be rich 77 times!
    I want to be rich 78 times!
    I want to be rich 79 times!
    I want to be rich 80 times!
    I want to be rich 81 times!
    I want to be rich 82 times!
    I want to be rich 83 times!
    I want to be rich 84 times!
    I want to be rich 85 times!
    I want to be rich 86 times!
    I want to be rich 87 times!
    I want to be rich 88 times!
    I want to be rich 89 times!
    I want to be rich 90 times!
    I want to be rich 91 times!
    I want to be rich 92 times!
    I want to be rich 93 times!
    I want to be rich 94 times!
    I want to be rich 95 times!
    I want to be rich 96 times!
    I want to be rich 97 times!
    I want to be rich 98 times!
    I want to be rich 99 times!
    I want to be rich 100 times!
    

The main porpouse of range() function is to generate continous sequence of integers.


```python
list1 = range(3,8)
print(list(list1))
print(type(list1))

list_2 = range(-11,11+1)
print(list(list_2))

list_3 = range(2,-4)
print(list(list_3))
```

    [3, 4, 5, 6, 7]
    <class 'range'>
    [-11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    []
    


```python
range_variable = range(1,5,2) #Third argument is step!
print(list(range_variable))
```

    [1, 3]
    


```python
for i in range(2,10,2):
    print(i)
```

    2
    4
    6
    8
    


```python
list_4 = range(3,8,1)
print(list(list_4))

list_5=range(3,8,2)
print(list(list_5))

list_6=range(3,10,-2)
print(list(list_6))
```

    [3, 4, 5, 6, 7]
    [3, 5, 7]
    []
    
