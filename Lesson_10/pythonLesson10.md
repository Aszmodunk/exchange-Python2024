```python
from webencodings import lookup

i = 1
while i <10:
    print(i)
    i += 1
else:
    print("i>10")
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
    i>10
    


```python
i = 1
while i <10:
    print(i)
    i += 1
    if i == 5:
        break
else:
    print("This line will never be executed :(")
```

    1
    2
    3
    4
    


```python
for a in range(10):
    print(a)
    if a == 5:
        break
    a = i+1
print("This line will be executed :)")
```

    0
    1
    2
    3
    4
    5
    This line will be executed :)
    


```python
b = 111
for b in range(1,1): #It might look like this should execute, but we need to realise the second argument uses 1 = 0 so we have first argument larger than second one
    print(b)
else:
    print("else ", b )
```

    else  111
    


```python
#0857
#Login screen
import time as t
studentId = "0X1"
pswd = "0857"
numberOfAttempts = 0



while True:
    print("/---------------------\\")
    print("Enter your student ID: \n")
    idInput= input("Enter your student ID: \n")
      
    print("Enter your password: \n")
    pwdInput= input("Enter your password: \n")
    print("\\---------------------/")
    
    
    if idInput == studentId and pwdInput == pswd:
        print("Welcome the magnificent one")
        break
    else:
        print("Wrong identification!\n")
        numberOfAttempts += 1
        if numberOfAttempts == 3:
            print("System locked for 10 minutes")
            for time in range(10):
                print("Locked for:", time-10)
                t.sleep(1)
        continue
    
```

    /---------------------\
    Enter your student ID: 
    
    Enter your password: 
    
    \---------------------/
    Wrong identification!
    
    /---------------------\
    Enter your student ID: 
    
    Enter your password: 
    
    \---------------------/
    Wrong identification!
    
    /---------------------\
    Enter your student ID: 
    
    Enter your password: 
    
    \---------------------/
    Wrong identification!
    
    System locked for 10 minutes
    


```python

```

Touple\\
dictionary
set


```python
toupleIs = (1,2,"12","car")
print(type(toupleIs))

listBeLike = [1,2,3,4,5,"11"]
print(type(listBeLike))

for item in listBeLike:
    print(f"In this {type(listBeLike)} we have {item} with {type(item)}")
    
print(listBeLike[1:5:2]) #Onwards
print(listBeLike[-1::-1]) #And backwards


dictionaryBeLike = {10,11,12,13}
print(type(dictionaryBeLike))

print(dictionaryBeLike, listBeLike, toupleIs)


```

    <class 'tuple'>
    <class 'list'>
    In this <class 'list'> we have 1 with <class 'int'>
    In this <class 'list'> we have 2 with <class 'int'>
    In this <class 'list'> we have 3 with <class 'int'>
    In this <class 'list'> we have 4 with <class 'int'>
    In this <class 'list'> we have 5 with <class 'int'>
    In this <class 'list'> we have 11 with <class 'str'>
    [2, 4]
    ['11', 5, 4, 3, 2, 1]
    <class 'set'>
    {10, 11, 12, 13} [1, 2, 3, 4, 5, '11'] (1, 2, '12', 'car')
    


```python
touple1 = (10,11,12,13,13,15,88,54,14,23,11)
touple2 = (11,12,13,1,5,4,8,9,10,11,8,13,2)
touple3 = touple1 + touple2
print(touple3)
print("3 TO 5",touple3[3:5])

print(sorted(touple3))


#Nested touplest

touple4 = (1,2,touple1, 13, "123", touple2)
print(touple4)


nested = (1,2,("A","B","C"),(3,4),("disco",("1","3")))
for i in range(len(nested)):
    print("The index",i ,"in list nested has value,",nested[i])
    
print("\n\n\n\n\n")


print("Value of nested in position 2 0 is ",nested[2][0] )
print("Value of nested in position 2 1 is ",nested[2][1] )
print("Value of nested in position 2 2 is ",nested[2][2] )
print("etc.")
print("\n\n\n\n\n")
print("Last letter of disco is",nested[4][0][-1])

print(nested[4][1][0])



#QUIZ IS HERE
#QUIZ IS HERE
#QUIZ IS HERE
#QUIZ IS HERE
#QUIZ IS HERE
#QUIZ IS HERE
#QUIZ IS HERE
#QUIZ IS HERE
#QUIZ IS HERE
#QUIZ IS HERE
#QUIZ IS HERE
#QUIZ IS HERE
#QUIZ IS HERE
#QUIZ IS HERE
#QUIZ IS HERE
#QUIZ IS HERE
#QUIZ IS HERE
for i in range(10):
    print("PRACTICE\n")
genres_tuple =("pop","rock","metal","techno","etc","martian music", "Disco","another genre", "I need long enough list", "Powermetal")
print("lenght of the tuple is",len(genres_tuple)) #Lenght of the touple


lenghtofIt = 0
for i in genres_tuple:
    lenghtofIt = lenghtofIt + 1
print(lenghtofIt)

for i in range(lenghtofIt):
    print(genres_tuple[i])
    
print(genres_tuple[3])
print("How to access index 3,4,5")
print(genres_tuple[3:6])
print("First two elements")
print(genres_tuple[:2])
position = 0
for i in genres_tuple:
    recon = i.lower()
    if recon == "disco":
        print(position)
    position = position + 1
genres_tuple.index("Disco")

print("generate sorted list:")
C_tuple=(-5,1,-3)
print(sorted(C_tuple))
```

    (10, 11, 12, 13, 13, 15, 88, 54, 14, 23, 11, 11, 12, 13, 1, 5, 4, 8, 9, 10, 11, 8, 13, 2)
    3 TO 5 (13, 13)
    [1, 2, 4, 5, 8, 8, 9, 10, 10, 11, 11, 11, 11, 12, 12, 13, 13, 13, 13, 14, 15, 23, 54, 88]
    (1, 2, (10, 11, 12, 13, 13, 15, 88, 54, 14, 23, 11), 13, '123', (11, 12, 13, 1, 5, 4, 8, 9, 10, 11, 8, 13, 2))
    The index 0 in list nested has value, 1
    The index 1 in list nested has value, 2
    The index 2 in list nested has value, ('A', 'B', 'C')
    The index 3 in list nested has value, (3, 4)
    The index 4 in list nested has value, ('disco', ('1', '3'))
    
    
    
    
    
    
    Value of nested in position 2 0 is  A
    Value of nested in position 2 1 is  B
    Value of nested in position 2 2 is  C
    etc.
    
    
    
    
    
    
    Last letter of disco is o
    1
    PRACTICE
    
    PRACTICE
    
    PRACTICE
    
    PRACTICE
    
    PRACTICE
    
    PRACTICE
    
    PRACTICE
    
    PRACTICE
    
    PRACTICE
    
    PRACTICE
    
    lenght of the tuple is 10
    10
    pop
    rock
    metal
    techno
    etc
    martian music
    Disco
    another genre
    I need long enough list
    Powermetal
    techno
    How to access index 3,4,5
    ('techno', 'etc', 'martian music')
    First two elements
    ('pop', 'rock')
    6
    generate sorted list:
    [-5, -3, 1]
    


```python
tuple1 = (1,2,3,4,5,6)
list1 = list(touple1)
list1.append(7)
list1[0] = 99
print(list1)

list2 = list1
tuple2 = tuple(list1)
#tuple2[0]=1 As we all know this doesn't work
#tuple2.append() Neither does this


```

    [99, 11, 12, 13, 13, 15, 88, 54, 14, 23, 11, 7]
    

### Lists


```python
mylist = ["Hello","I","There","Have","Ah","The","General","Highghround"]
mylist.append("Kenobi")
print(mylist)
print(mylist[::2])
print(mylist[1::2])

for i in range(len(mylist)):
    print("For index",i, "We get", mylist[i],"And for index",i*-1,"We get", mylist[i*-1])
    
nestedList = mylist
#Lists are referenced between one and other, they are identical, one change to the first one is change for the other one too.
#We can prevent to that by adding [:]
nestedList.append(("Wookies", "Jungle"))
nestedList.append(["Han solo","Chubaka"])
print(nestedList)

#Fruther list manipulation
mylist.extend(["Mandalorians","Big Dakka."])
print(mylist)

#list.append() Discussed above
#Reminder - Append takes values as literars, so if we append [Things,like,this] a whole list will be appended, not like in extend function!

mylist[10][0] = "Frozen Han Solo"
print(mylist)
print(len(mylist))
del(mylist[12])
print(mylist)
"Anakin! is Darth Wader".split("!")
```

    ['Hello', 'I', 'There', 'Have', 'Ah', 'The', 'General', 'Highghround', 'Kenobi']
    ['Hello', 'There', 'Ah', 'General', 'Kenobi']
    ['I', 'Have', 'The', 'Highghround']
    For index 0 We get Hello And for index 0 We get Hello
    For index 1 We get I And for index -1 We get Kenobi
    For index 2 We get There And for index -2 We get Highghround
    For index 3 We get Have And for index -3 We get General
    For index 4 We get Ah And for index -4 We get The
    For index 5 We get The And for index -5 We get Ah
    For index 6 We get General And for index -6 We get Have
    For index 7 We get Highghround And for index -7 We get There
    For index 8 We get Kenobi And for index -8 We get I
    ['Hello', 'I', 'There', 'Have', 'Ah', 'The', 'General', 'Highghround', 'Kenobi', ('Wookies', 'Jungle'), ['Han solo', 'Chubaka']]
    ['Hello', 'I', 'There', 'Have', 'Ah', 'The', 'General', 'Highghround', 'Kenobi', ('Wookies', 'Jungle'), ['Han solo', 'Chubaka'], 'Mandalorians', 'Big Dakka.']
    ['Hello', 'I', 'There', 'Have', 'Ah', 'The', 'General', 'Highghround', 'Kenobi', ('Wookies', 'Jungle'), ['Frozen Han Solo', 'Chubaka'], 'Mandalorians', 'Big Dakka.']
    13
    ['Hello', 'I', 'There', 'Have', 'Ah', 'The', 'General', 'Highghround', 'Kenobi', ('Wookies', 'Jungle'), ['Frozen Han Solo', 'Chubaka'], 'Mandalorians']
    




    ['Anakin', ' is Darth Wader']



### QUIZ


```python
a_list = [1,"hello",[1,2,3],True]
a_list
```




    [1, 'hello', [1, 2, 3], True]




```python
a_list[1]
```




    'hello'




```python
a_list[1:40]
```




    ['hello', [1, 2, 3], True]




```python
A = [1,"A"]
B = [2,1,"d"]
C = A + B
C
```




    [1, 'A', 2, 1, 'd']




```python

```

## PRacitce


```python
scores = [85, 79, 93]
subjects = ["Chinese", "Math", "English"]
for i in range(len(scores)):
    print("Student achieved",scores[i], "in subject",subjects[i])
```

    Student achieved 85 in subject Chinese
    Student achieved 79 in subject Math
    Student achieved 93 in subject English
    
