## For loops 

'for (variable in a sequence)'


```python

from stringprep import in_table_b1

for i in range(0,10):
    print(i,")\t Hello")
```


```python
print(list(range(3)))
for i in range(3):
    print(i, end =" * ")
```


```python
a = input("ENTER POSITIVE NUMBER: ")
a = int(a)
if a > 0:
    for i in range(1,a+1):
        print(i, end=" ")
else:
     print("Please provide positive number")
        
    
    
```


```python
for i in range(2,8):
    print("1) The value of i is ",i)

    for c in range(2,8,3):
        print("2) The value of c is ",c)
```


```python
#Pracitce 2
a = input("ENTER POSITIVE NUMBER: ")
a = int(a)
if a > 0:
    for i in range(a):
        print(i+1, end=" ")
    print("||")
    for i in range(1,a+1):
        print(i, end=" ")
    print("||")    
    if a > 0:
        for i in range(1,a+1,1):
            print(i, end=" ")
    print("||")
    
    
else:
    print("Please provide positive number")

        
```


```python
for x in range (0,10):
    print(x,end=" ")
print("||")    
for x in range(0,10,2):
    print(x,end=" ")
print("||")
for x in range(10,0,-1):
    print(x,end=" ")
print("||")    
```


```python
abc = input("ENTER POSITIVE NUMBER: ")
abc = int(abc)
if abc > 0:
    for i in range(1,abc,2):
        print(i+1, end=" ")
    print("\n")
    
    for i in range(2,abc,2):
        print(i, end=" ")
    print("\n")
    
    for i in range(1,abc,2):
        if i%2==0:
            print(i, end=" ")
else:
    print("Please provide positive number")
    

```


```python
first_number = input("ENTER POSITIVE NUMBER: ")
second_number = input("ENTER POSITIVE NUMBER: ")
increment_number = input("enter increment number: ")

first_number = int(first_number)
second_number = int(second_number)
increment_number = int(increment_number)

a = 0
if first_number > 0 and increment_number >0: 
    for i in range(first_number,second_number+1,increment_number):
        print(i, end=" ")
        a += i
    print("\nSum of nubmers is: ",a)
else:
    print("Numbers must be positive.))")
```

    
    Sum of nubmers is:  0
    


```python
m = 0
for i in range(1,11):
    print("LVL 1 ",i)
    for j in range(1,11):
        print("LVL 2 ",j)
        m += 1
        
print(m)
```

    LVL 1  1
    LVL 2  1
    LVL 2  2
    LVL 2  3
    LVL 2  4
    LVL 2  5
    LVL 2  6
    LVL 2  7
    LVL 2  8
    LVL 2  9
    LVL 2  10
    LVL 1  2
    LVL 2  1
    LVL 2  2
    LVL 2  3
    LVL 2  4
    LVL 2  5
    LVL 2  6
    LVL 2  7
    LVL 2  8
    LVL 2  9
    LVL 2  10
    LVL 1  3
    LVL 2  1
    LVL 2  2
    LVL 2  3
    LVL 2  4
    LVL 2  5
    LVL 2  6
    LVL 2  7
    LVL 2  8
    LVL 2  9
    LVL 2  10
    LVL 1  4
    LVL 2  1
    LVL 2  2
    LVL 2  3
    LVL 2  4
    LVL 2  5
    LVL 2  6
    LVL 2  7
    LVL 2  8
    LVL 2  9
    LVL 2  10
    LVL 1  5
    LVL 2  1
    LVL 2  2
    LVL 2  3
    LVL 2  4
    LVL 2  5
    LVL 2  6
    LVL 2  7
    LVL 2  8
    LVL 2  9
    LVL 2  10
    LVL 1  6
    LVL 2  1
    LVL 2  2
    LVL 2  3
    LVL 2  4
    LVL 2  5
    LVL 2  6
    LVL 2  7
    LVL 2  8
    LVL 2  9
    LVL 2  10
    LVL 1  7
    LVL 2  1
    LVL 2  2
    LVL 2  3
    LVL 2  4
    LVL 2  5
    LVL 2  6
    LVL 2  7
    LVL 2  8
    LVL 2  9
    LVL 2  10
    LVL 1  8
    LVL 2  1
    LVL 2  2
    LVL 2  3
    LVL 2  4
    LVL 2  5
    LVL 2  6
    LVL 2  7
    LVL 2  8
    LVL 2  9
    LVL 2  10
    LVL 1  9
    LVL 2  1
    LVL 2  2
    LVL 2  3
    LVL 2  4
    LVL 2  5
    LVL 2  6
    LVL 2  7
    LVL 2  8
    LVL 2  9
    LVL 2  10
    LVL 1  10
    LVL 2  1
    LVL 2  2
    LVL 2  3
    LVL 2  4
    LVL 2  5
    LVL 2  6
    LVL 2  7
    LVL 2  8
    LVL 2  9
    LVL 2  10
    100
    


```python
m = 0
i = 0

for i in range(5):
    m += 1
    print(f"[lvl1]This is {i+1} iteration\n")
    n = 0
    for j in range(i):
        n = n+1
        print(f"[lvl2] This is the {j+1} iteration \n")
```

    [lvl1]This is 1 iteration
    
    [lvl1]This is 2 iteration
    
    [lvl2] This is the 1 iteration 
    
    [lvl1]This is 3 iteration
    
    [lvl2] This is the 1 iteration 
    
    [lvl2] This is the 2 iteration 
    
    [lvl1]This is 4 iteration
    
    [lvl2] This is the 1 iteration 
    
    [lvl2] This is the 2 iteration 
    
    [lvl2] This is the 3 iteration 
    
    [lvl1]This is 5 iteration
    
    [lvl2] This is the 1 iteration 
    
    [lvl2] This is the 2 iteration 
    
    [lvl2] This is the 3 iteration 
    
    [lvl2] This is the 4 iteration 
    
    


```python
mytext = "####"
for i in range(10):
    print(mytext)
print("ENDO OF MY TEXT1\n")

mychar = "#"
for i in range(10):
    print("")
    for a in range(4):
        print(mychar, end="")
```

    ####
    ####
    ####
    ####
    ####
    ####
    ####
    ####
    ####
    ####
    ENDO OF MY TEXT1
    
    
    ####
    ####
    ####
    ####
    ####
    ####
    ####
    ####
    ####
    ####


```python
rng=input("ENTER RANGE: ")
rng=int(rng)
x = 0
for i in range(rng):
    print(i*"#")

for j in range(rng,0,-1):
    print(j*"#")

```

    
    #
    ##
    ###
    ####
    #####
    ######
    #######
    ########
    #########
    ##########
    #########
    ########
    #######
    ######
    #####
    ####
    ###
    ##
    #
    

# Lesson 8


```python
#Lesson 8 here

rng=input("ENTER RANGE: ")
rng=int(rng)
x = 0
for i in range(rng):
    print("")
    for j in range(i+1):
        print(j+1,end="")


```

    
    1
    12
    123
    1234
    12345
    123456
    1234567
    12345678
    123456789
    12345678910
    1234567891011
    123456789101112
    12345678910111213
    1234567891011121314
    123456789101112131415


```python

for j in range(10,0,-1):
    print(j*"#")
    
for j1 in range(10,0,-1):
    for j2 in range(0,j2,1):
        print(j2*"#")
```

    ##########
    #########
    ########
    #######
    ######
    #####
    ####
    ###
    ##
    #
    
    


```python
rng=input("ENTER RANGE: ")
rng=int(rng)

for i in range(rng,0,-1):
    print("")
    for j in range(i):
        print(j+1,end="")


for i2 in range(rng,0,-1):
    print(i)
```

    
    123456789101112
    1234567891011
    12345678910
    123456789
    12345678
    1234567
    123456
    12345
    1234
    123
    12
    112
    11
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
    


```python
for a3 in range(1,10):
    for a4 in range(2,10):
        c = a3 * a4
        print(f"{a3}*{a4}={c}", end= "\t")
        if a4 == 9:
            print("\n")
        
```

    1*2=2	1*3=3	1*4=4	1*5=5	1*6=6	1*7=7	1*8=8	1*9=9	
    
    2*2=4	2*3=6	2*4=8	2*5=10	2*6=12	2*7=14	2*8=16	2*9=18	
    
    3*2=6	3*3=9	3*4=12	3*5=15	3*6=18	3*7=21	3*8=24	3*9=27	
    
    4*2=8	4*3=12	4*4=16	4*5=20	4*6=24	4*7=28	4*8=32	4*9=36	
    
    5*2=10	5*3=15	5*4=20	5*5=25	5*6=30	5*7=35	5*8=40	5*9=45	
    
    6*2=12	6*3=18	6*4=24	6*5=30	6*6=36	6*7=42	6*8=48	6*9=54	
    
    7*2=14	7*3=21	7*4=28	7*5=35	7*6=42	7*7=49	7*8=56	7*9=63	
    
    8*2=16	8*3=24	8*4=32	8*5=40	8*6=48	8*7=56	8*8=64	8*9=72	
    
    9*2=18	9*3=27	9*4=36	9*5=45	9*6=54	9*7=63	9*8=72	9*9=81	
    
    


```python
rng=input("ENTER RANGE: ")
rng=int(rng)
x = 0
for i in range(rng):
    print(i*"#")

for j in range(rng,0,-1):
    print(j*"#")
```

    
    #
    ##
    ###
    ####
    #####
    ######
    #######
    ########
    #########
    ##########
    #########
    ########
    #######
    ######
    #####
    ####
    ###
    ##
    #
    


```python
for i in range(rng):
    if i != rng-1:
        print(i*"#")
    else:
        for a in range(i,0,-1):
            print(a*"#")
    
```

    
    #
    ##
    ###
    ####
    #####
    ######
    #######
    ########
    #########
    ########
    #######
    ######
    #####
    ####
    ###
    ##
    #
    


```python
for a3 in range(1, 10):
    for a4 in range(2, 10):
        c = a3 * a4
        print(f"{a3}*{a4}={c}", end="\t\n")
        if a4 == 9:
            print("")
```

    1*2=2	
    1*3=3	
    1*4=4	
    1*5=5	
    1*6=6	
    1*7=7	
    1*8=8	
    1*9=9	
    
    2*2=4	
    2*3=6	
    2*4=8	
    2*5=10	
    2*6=12	
    2*7=14	
    2*8=16	
    2*9=18	
    
    3*2=6	
    3*3=9	
    3*4=12	
    3*5=15	
    3*6=18	
    3*7=21	
    3*8=24	
    3*9=27	
    
    4*2=8	
    4*3=12	
    4*4=16	
    4*5=20	
    4*6=24	
    4*7=28	
    4*8=32	
    4*9=36	
    
    5*2=10	
    5*3=15	
    5*4=20	
    5*5=25	
    5*6=30	
    5*7=35	
    5*8=40	
    5*9=45	
    
    6*2=12	
    6*3=18	
    6*4=24	
    6*5=30	
    6*6=36	
    6*7=42	
    6*8=48	
    6*9=54	
    
    7*2=14	
    7*3=21	
    7*4=28	
    7*5=35	
    7*6=42	
    7*7=49	
    7*8=56	
    7*9=63	
    
    8*2=16	
    8*3=24	
    8*4=32	
    8*5=40	
    8*6=48	
    8*7=56	
    8*8=64	
    8*9=72	
    
    9*2=18	
    9*3=27	
    9*4=36	
    9*5=45	
    9*6=54	
    9*7=63	
    9*8=72	
    9*9=81	
    
    


```python
for a3 in range(1, 10):
    for a4 in range(2, 6):
        c = a3 * a4
        print(f"{a4}*{a3}={c:2d}", end="\t")
        if a4 == 5:
            print("")
print("\n")
for a3 in range(1, 10):
    for a4 in range(6, 10):
        c = a3 * a4
        print(f"{a4}*{a3}={c:2d}", end="\t")
        if a4 == 9:
            print("")
```

    2*1= 2	3*1= 3	4*1= 4	5*1= 5	
    2*2= 4	3*2= 6	4*2= 8	5*2=10	
    2*3= 6	3*3= 9	4*3=12	5*3=15	
    2*4= 8	3*4=12	4*4=16	5*4=20	
    2*5=10	3*5=15	4*5=20	5*5=25	
    2*6=12	3*6=18	4*6=24	5*6=30	
    2*7=14	3*7=21	4*7=28	5*7=35	
    2*8=16	3*8=24	4*8=32	5*8=40	
    2*9=18	3*9=27	4*9=36	5*9=45	
    
    
    6*1= 6	7*1= 7	8*1= 8	9*1= 9	
    6*2=12	7*2=14	8*2=16	9*2=18	
    6*3=18	7*3=21	8*3=24	9*3=27	
    6*4=24	7*4=28	8*4=32	9*4=36	
    6*5=30	7*5=35	8*5=40	9*5=45	
    6*6=36	7*6=42	8*6=48	9*6=54	
    6*7=42	7*7=49	8*7=56	9*7=63	
    6*8=48	7*8=56	8*8=64	9*8=72	
    6*9=54	7*9=63	8*9=72	9*9=81	
    


```python
days = 30
dollars = 0

for i in range(days):
    dollars = dollars + 2**i
    print(dollars)
```

    1
    3
    7
    15
    31
    63
    127
    255
    511
    1023
    2047
    4095
    8191
    16383
    32767
    65535
    131071
    262143
    524287
    1048575
    2097151
    4194303
    8388607
    16777215
    33554431
    67108863
    134217727
    268435455
    536870911
    1073741823
    

# While loop
while something true do:



```python
total = 0
n = 1
while(n<11):
    total +=n
    n+=1
print(total)
```

    55
    


```python
i = 3
sum = 0
for i in range(3,13,3):
    sum = sum + i
print(sum)

sum=0
i = 3
print("")

while i<13:
    sum = sum + i
    i = i + 3
print(sum)
```

    30
    
    30
    


```python
total = 0
i = 1
while(i<=10):
    total = total + i
    i = i + 1
print(total)

totalB = 0
ib = 0

for ib in range(1,11):
    totalB = totalB + ib
print(totalB)


a
```

    55
    55
    


```python
abcde  = 0
while abcde < 10:
    print(f"{abcde} this is A block\n{abcde} this is B block")
    abcde = abcde + 1
```

    0 this is A block
    0 this is B block
    1 this is A block
    1 this is B block
    2 this is A block
    2 this is B block
    3 this is A block
    3 this is B block
    4 this is A block
    4 this is B block
    5 this is A block
    5 this is B block
    6 this is A block
    6 this is B block
    7 this is A block
    7 this is B block
    8 this is A block
    8 this is B block
    9 this is A block
    9 this is B block
    


```python

```


```python

user_input = input("Enter positive number: ")
user_input = int(user_input)
midvar = 0
while midvar < user_input+1:
    print(midvar, end=" ")
    midvar = midvar + 1
```

    0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 


```python

```


```python
ndinput = input("Enter positive number: ")
ndinput = int(ndinput)
calculator = 0
id = 0
while id < ndinput+1=:
    calculator = calculator + id
    id = id + 1
print(calculator)    
```


```python
oddinput = input("Enter positive number: ")
oddinput = int(oddinput)
i = 0
while i < oddinput+1:
    if i%2 == 0:
        print(i, end=" ")
        i = i + 1
    else:
        i = i + 1
```

    0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 


```python
oddinput = input("Enter positive number: ")
oddinput = int(oddinput)
i = 0
while i < oddinput+1:
    if i%2 != 0:
        print(i, end=" ")
        i = i + 1
    else:
        i = i + 1
```

    1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 


```python
a = "#"
b = 10
bb = 0
c = 0


while bb < b:
    print(a*bb)
    bb = bb + 1
c =bb
while c != 0:
    print(c*a)
    c = c - 1
    
        
```

    
    #
    ##
    ###
    ####
    #####
    ######
    #######
    ########
    #########
    ##########
    #########
    ########
    #######
    ######
    #####
    ####
    ###
    ##
    #
    


```python
# for a3 in range(1, 10):
#     for a4 in range(2, 10):
#         c = a3 * a4
#         print(f"{a3}*{a4}={c}", end="\t")
#         if a4 == 9:
#             print("\n")

a = 0
b = 0

while a != 9:
    a = a + 1
    b = 0
    while b !=9:
        b = b +1
        print(f"{b}*{a} = {a*b:2d}", end="\t")
        if b == 9:
            print("\n")
```

    1*1 =  1	2*1 =  2	3*1 =  3	4*1 =  4	5*1 =  5	6*1 =  6	7*1 =  7	8*1 =  8	9*1 =  9	
    
    1*2 =  2	2*2 =  4	3*2 =  6	4*2 =  8	5*2 = 10	6*2 = 12	7*2 = 14	8*2 = 16	9*2 = 18	
    
    1*3 =  3	2*3 =  6	3*3 =  9	4*3 = 12	5*3 = 15	6*3 = 18	7*3 = 21	8*3 = 24	9*3 = 27	
    
    1*4 =  4	2*4 =  8	3*4 = 12	4*4 = 16	5*4 = 20	6*4 = 24	7*4 = 28	8*4 = 32	9*4 = 36	
    
    1*5 =  5	2*5 = 10	3*5 = 15	4*5 = 20	5*5 = 25	6*5 = 30	7*5 = 35	8*5 = 40	9*5 = 45	
    
    1*6 =  6	2*6 = 12	3*6 = 18	4*6 = 24	5*6 = 30	6*6 = 36	7*6 = 42	8*6 = 48	9*6 = 54	
    
    1*7 =  7	2*7 = 14	3*7 = 21	4*7 = 28	5*7 = 35	6*7 = 42	7*7 = 49	8*7 = 56	9*7 = 63	
    
    1*8 =  8	2*8 = 16	3*8 = 24	4*8 = 32	5*8 = 40	6*8 = 48	7*8 = 56	8*8 = 64	9*8 = 72	
    
    1*9 =  9	2*9 = 18	3*9 = 27	4*9 = 36	5*9 = 45	6*9 = 54	7*9 = 63	8*9 = 72	9*9 = 81	
    
    
