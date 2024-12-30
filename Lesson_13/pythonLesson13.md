```python
def copareStrings(x,y):
    if x==y:
        return 1

myString1 = "Sample text"
myString2 = "Sample text"

check = copareStrings(myString1,myString2)

if check == 1:
    print("\n Strings are mathing")
else:
    print("\n Strings are not mathing")
```

    
     Strings are mathing
    




```python
inputString = input("Insert sentence here:\n")
stringList = inputString.split()
print(len(stringList))
#My take
```

    3
    


```python
frog = "⠄⠄⢀⣠⣤⣶⣶⣶⣤⣄⠄⠄⢀⣠⣤⣤⣤⣤⣀⠄⠄⠄⠄⠄⠄\n⢠⣾⣿⣿⣿⣿⠿⠿⢿⣿⣿⡆⣿⣿⣿⣿⣿⣿⣿⣷⡄⠄⠄⠄⠄\n⣿⣿⡟⣩⣵⣶⣾⣿⣷⣶⣮⣅⢛⣫⣭⣭⣭⣭⣭⣭⣛⣂⠄⠄⠄\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣭⠛⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀\n⣿⣿⣿⣿⣿⠿⢟⣛⣫⣭⠉⠍⠉⣛⠿⡘⣿⠿⢟⣛⡛⠉⠙⠻⢿\n⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣭⣍⠄⣡⣬⣭⣭⣅⣈⣀⣉⣁\n⣿⣿⣿⣿⣶⣭⣛⡻⠿⠿⢿⣿⡿⢛⣥⣾⣿⣿⣿⣿⣿⣿⣿⠿⠋\n⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣩⣵⣾⣿⣿⣯⣙⠟⣋⣉⣩⣍⡁⠄⠄\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣷⡄⠄\n⣿⣿⡿⢟⣛⣛⣛⣛⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⡀\n⣿⡟⢼⣿⣯⣭⣛⣛⣛⡻⠷⠶⢶⣬⣭⣭⣭⡭⠭⢉⡄⠶⠾⠟⠁\n⣟⠻⣦⣤⣭⣭⣭⣭⣛⣛⡻⠿⠷⠶⢶⣶⠞⣼⡟⡸⣸⡸⠿⠄⠄\n⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠷⡆⣾⠟⡴⣱⢏⡜⠆⠄⠄"
```




```python
#Teachers take
def freq(string):
    words = []
    words = string.split()
    
    dict = {}
    for word in words:
        dict[word]=words.count(word)
    print(dict)

tongue_twister = ("Betty Botter bought a bit of butter, "
                  "\"But,\" she said, \"this butter's bitter. "
                  "If I put it in my batter, "
                  "It will make my batter bitter. "
                  "But a bit of better butter "
                  "Will make my batter better.\" "
                  "So Betty Botter bought a bit of better butter, "
                  "And it made her batter better. "
                  "So 'twas better Betty Botter "
                  "Bought a bit of better butter.")
freq(tongue_twister)
```

    {'Betty': 3, 'Botter': 3, 'bought': 2, 'a': 4, 'bit': 4, 'of': 4, 'butter,': 2, '"But,"': 1, 'she': 1, 'said,': 1, '"this': 1, "butter's": 1, 'bitter.': 2, 'If': 1, 'I': 1, 'put': 1, 'it': 2, 'in': 1, 'my': 3, 'batter,': 1, 'It': 1, 'will': 1, 'make': 2, 'batter': 3, 'But': 1, 'better': 4, 'butter': 1, 'Will': 1, 'better."': 1, 'So': 2, 'And': 1, 'made': 1, 'her': 1, 'better.': 1, "'twas": 1, 'Bought': 1, 'butter.': 1}
    


```python
def freq(string):
    words = string.split()
    secondWords = []
    for i in words:
        secondWords.append(i.lower())
    print(secondWords)
    word_freq = {} 

    for word in secondWords:
        clean_word = word.strip(".,\"'").lower()
        if clean_word not in word_freq:  
            word_freq[clean_word] = secondWords.count(clean_word)

    print(word_freq)

tongue_twister = ("Betty Botter bought a bit of butter, "
                  "\"But,\" she said, \"this butter's bitter. "
                  "If I put it in my batter, "
                  "It will make my batter bitter. "
                  "But a bit of better butter "
                  "Will make my batter better.\" "
                  "So Betty Botter bought a bit of better butter, "
                  "And it made her batter better. "
                  "So 'twas better Betty Botter "
                  "Bought a bit of better butter.")
freq(tongue_twister)

```

    ['betty', 'botter', 'bought', 'a', 'bit', 'of', 'butter,', '"but,"', 'she', 'said,', '"this', "butter's", 'bitter.', 'if', 'i', 'put', 'it', 'in', 'my', 'batter,', 'it', 'will', 'make', 'my', 'batter', 'bitter.', 'but', 'a', 'bit', 'of', 'better', 'butter', 'will', 'make', 'my', 'batter', 'better."', 'so', 'betty', 'botter', 'bought', 'a', 'bit', 'of', 'better', 'butter,', 'and', 'it', 'made', 'her', 'batter', 'better.', 'so', "'twas", 'better', 'betty', 'botter', 'bought', 'a', 'bit', 'of', 'better', 'butter.']
    {'betty': 3, 'botter': 3, 'bought': 3, 'a': 4, 'bit': 4, 'of': 4, 'butter': 1, 'but': 1, 'she': 1, 'said': 0, 'this': 0, "butter's": 1, 'bitter': 0, 'if': 1, 'i': 1, 'put': 1, 'it': 3, 'in': 1, 'my': 3, 'batter': 3, 'will': 2, 'make': 2, 'better': 4, 'so': 2, 'and': 1, 'made': 1, 'her': 1, 'twas': 0}
    


```python
def getAra(width, height=12):
    return width*height
ret1 = getAra(3,3)
ret2 = getAra(4)
print(ret1, ret2)
```

    9 48
    


```python
def goodRating(rating =4):
    if rating < 7:
        print("Not good rating:", rating)
    else:
        print("Good rating:", rating)
    
goodRating()
goodRating(11)
```

    Not good rating: 4
    Good rating: 11
    


```python
#Local vs global variable

def scope():
    var1 = 1 # local
    #var2 = 2 # local
    print(var1, var2)

var1 = 4 #global
var2 = 5 #global 
scope()
print(var1, var2)
```

    1 5
    4 5
    


```python
#Local vs global variable

def scope():
    var1 = 1 # local
    var2 = 2 # local
    print(var1, var2)

var1 = 4 #global
var2 = 5 #global 
scope()
print(var1, var2)
```

    1 2
    4 5
    


```python
def printer1(artist):
    internal_car1 = artist
    print(artist, "Is an artist")
artist = "Michael Jackson"
printer1(artist)
#printer1(internal_car1)  #Won't work since we call local variable within the function
```

    Michael Jackson Is an artist
    


```python
def printer1(artist):
    global internal_car1
    internal_car1 = artist
    print(artist, "Is an artist")
artist = "Michael Jackson"
printer1(artist)
printer1(internal_car1)  

```


```python
myFavBand = "AC/DC"

def getBandRating(band):
    if band == myFavBand:
        return 10.0
    else:
        return 0.0

print("AC/DC rating:", getBandRating(myFavBand))
print("Sabaton rating",getBandRating("Sabaton"))
print("My fav band is", myFavBand)
```

    AC/DC rating: 10.0
    Sabaton rating 0.0
    My fav band is AC/DC
    


```python
#myFavBand = "AC/DC"
#del myFavBand
def getBandRating(band):
    myFavBand = "AC/DC"
    if band == myFavBand:
        return 10.0
    else:
        return 0.0

print("AC/DC rating:", getBandRating("AC/DC"))
print("Sabaton rating",getBandRating("Sabaton"))
print("My fav band is", "AC/DC")
```

    AC/DC rating: 10.0
    Sabaton rating 0.0
    My fav band is AC/DC
    


```python
myFavBand = "AC/DC"
#del myFavBand
def getBandRating(band):
    myFavBand = "Sabaton"
    if band == myFavBand:
        return 10.0
    else:
        return 0.0

print("AC/DC rating:", getBandRating("AC/DC"))
print("Sabaton rating",getBandRating("Sabaton"))
print("My fav band is", "AC/DC")
```

    AC/DC rating: 0.0
    Sabaton rating 10.0
    My fav band is AC/DC
    


```python
def printall(*args): 
    print(f"Number of arugments: {len(args)}")
    for arg in args:
        print(arg)

printall("Adidas","Nike","Pepe the frog")

```

    Number of arugments: 3
    Adidas
    Nike
    Pepe the frog
    


```python
performace = input("Performace of sales:")
performace = int(performace)
salary = 40000
def checkBonus(sales):
    if sales < 500000:
        return "No bonus"
    else:
        return ((sales-500000)/100)


print("Expected salary this month isis: ",checkBonus(performace) + salary)    
print("Bonus in the salary is: ",checkBonus(performace))

```

    Expected salary this month isis:  41000.0
    Bonus in the salary is:  1000.0
    


```python
weight = float(input("Please enter your weight in [kg]: \n"))
height = float(input("Please enter your height in [cm]: \n"))
def BMI(weight,height):
    height = height/100
    BMI = weight/(height**2)
    
    if BMI < 18.5:
        return "Your BMI is underweight", BMI
    elif BMI > 24:
        return "Your BMI is overweight", BMI
    elif 24 <= BMI <27:
        return "Your BMI is within healthy limits", BMI
    else:
        return "Obese", BMI

checkBMI = BMI(weight,height)
print(checkBMI)
```

    ('Your BMI is overweight', 26.583175803402646)
    


```python
#Quiz 1
in1 = int(input("Number: "))
in2 = int(input("Number: "))
def dividor(one,two):
    return one / two
print(dividor(in1,in2))
```

    5.5
    


```python
#Quiz 2

def con(a,b):
    return a+b

#Q: Cane we use this function to add numbers or strings?
#A: Both.

print(con("dog","dawg"))
print(con(1,2))

#Q: Can it be used to concatenate lists or touples?
#A: Yes, both.

print(con([2,3,1,1],[8,1,15,6]))
```

    dogdawg
    3
    [2, 3, 1, 1, 8, 1, 15, 6]
    


```python
#Write function for total count of the words of the betty

tongue_twister = ("Betty Botter bought a bit of butter, "
                  "\"But,\" she said, \"this butter's bitter. "
                  "If I put it in my batter, "
                  "It will make my batter bitter. "
                  "But a bit of better butter "
                  "Will make my batter better.\" "
                  "So Betty Botter bought a bit of better butter, "
                  "And it made her batter better. "
                  "So 'twas better Betty Botter "
                  "Bought a bit of better butter.")

def myCounter(input,search):
    myList2 = input.split()
    b = 0
    for i in myList2:
        i = i.strip(".,\"'").lower()
        if i == search.lower():
            b = b+1
    print(b)
myCounter(tongue_twister,"betty")
```

    3
    
