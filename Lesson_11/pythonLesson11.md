```python
release_year_dict = {"Thriller": "1982", "Back in black":"1980", "The dark side of the moon":"1973","Pepe the frog":"2003","Gladiator":"2005"}
release_year_dict
```




    {'Thriller': '1982',
     'Back in black': '1980',
     'The dark side of the moon': '1973',
     'Pepe the frog': '2003',
     'Gladiator': '2005'}




```python
release_year_dict["The dark side of the moon"]          

```




    '1973'



The first part "Thriller" is called key, which can be string, and the value, which can be any basic datatype int,str,float

we can retrieve value by calling the key



```python
release_year_dict.keys()
```




    dict_keys(['Thriller', 'Back in black', 'The dark side of the moon', 'Pepe the frog', 'Gladiator'])



We can recover all the keys by the dict.keys()


```python
release_year_dict.values()
```




    dict_values(['1982', '1980', '1973', '2003', '2005'])



We can do the same with values by calling dic.values()


```python
release_year_dict["Aszmobald"] = "1990"
release_year_dict
```




    {'Thriller': '1982',
     'Back in black': '1980',
     'The dark side of the moon': '1973',
     'Pepe the frog': '2003',
     'Gladiator': '2005',
     'Aszmobald': '1990'}



We can element by the dict["Key"] = "Value"


```python
del(release_year_dict["Aszmobald"])
release_year_dict
```




    {'Thriller': '1982',
     'Back in black': '1980',
     'The dark side of the moon': '1973',
     'Pepe the frog': '2003',
     'Gladiator': '2005'}



We can also remove the entry by del() function as show above

del(dict["key"])


```python
"Pepe the frog" in release_year_dict
```




    True



we can check if the value is in the dictionary by "Key" in dict

output is always gonna be true or false


```python
lang = {"Ahoj": "Hello", "Dobré ráno": "Good morning", "Jožka": "Joseph"}
print(lang)
lang.clear()
lang
```

    {'Ahoj': 'Hello', 'Dobré ráno': 'Good morning', 'Jožka': 'Joseph'}
    




    {}



We can clear the dictionary by the dict.clear()


```python
# We can convert list to the dictionary by calling dict(list1)
a = [["Ahoj", "Hello"], ["Mom", "Máma"]]
dict_1 = dict(a)
print(dict_1)

dict_2 = dict(a)
print(dict_2)

dict_3 = dict(a)
print(dict_3)

dict_4 = dict(a)
print(dict_4)

dict_1.clear()
dict_2.clear()
dict_3.clear()
dict_4.clear()
```

    {'Ahoj': 'Hello', 'Mom': 'Máma'}
    {'Ahoj': 'Hello', 'Mom': 'Máma'}
    {'Ahoj': 'Hello', 'Mom': 'Máma'}
    {'Ahoj': 'Hello', 'Mom': 'Máma'}
    


```python
# We can merge several dictionaries by the function update()
lang1 = {"Hallo":"Hello"}
lang2 = {"Ola": "Hello"}
print("Original list 1", lang1)
print("Original list 2", lang2)
lang1.update(lang2)
print("Updated list 1", lang1)

lang3 = {"Ola": "Hi"}
lang4 = {}
lang4.update(lang3)
print("List 4", lang4)
lang4.update(lang2)
print("Updated list 4", lang4)
# Here it's important that  value can be represented only once


#Copy function here
lang5 = lang4.copy()
lang5 
```

    Original list 1 {'Hallo': 'Hello'}
    Original list 2 {'Ola': 'Hello'}
    Updated list 1 {'Hallo': 'Hello', 'Ola': 'Hello'}
    List 4 {'Ola': 'Hi'}
    Updated list 4 {'Ola': 'Hello'}
    




    {'Ola': 'Hello'}




```python
dict1 = {"Banana":20, "Apple":34, "Orange":12}
print(dict1["Apple"])

dict2 = dict1.copy()
print(dict2["Banana"])
```

    34
    20
    


```python
# print(dict1[0])
# Doesn't work since the dictionary has no order
# If we want to  avoid interuption, we can use get() function
# dict.get(key[Value])
print(dict1.get("Apple"))
print(dict1.get("Banana", 55))
print(dict1.get("Pig", "Not in dictionary"))
print(dict1.get("Apple", 99))
print(dict1)
```

    34
    20
    Not in dictionary
    34
    {'Banana': 20, 'Apple': 34, 'Orange': 12}
    




```python
dict1 = {"Banana": 20, "Apple": 34, "Orange": 55}

print(dict1)

dict1["Bacon"] = 1
print(dict1)

del(dict1["Bacon"])
print(dict1)

dict1.clear()
print(dict1)
#del dict1

dict1 = {"Banana":20, "Apple":34, "Orange":12}
print(dict1["Apple"])

key1 = dict1.keys()
value1 = dict1.values()
print(key1, value1)

key2 = list(dict1.keys())
value2 = list(dict1.values())
print(key2, value2)
print(value2[0],key2[0])
print("Banana\n")

# ITems, we can obtain all keys: values
item1 = dict1.items()
print(item1)
item1_L = list(item1)
print(item1_L[1][1])
print(item1_L[1][0])
```

    {'Banana': 20, 'Apple': 34, 'Orange': 55}
    {'Banana': 20, 'Apple': 34, 'Orange': 55, 'Bacon': 1}
    {'Banana': 20, 'Apple': 34, 'Orange': 55}
    {}
    34
    dict_keys(['Banana', 'Apple', 'Orange']) dict_values([20, 34, 12])
    ['Banana', 'Apple', 'Orange'] [20, 34, 12]
    20 Banana
    Banana
    
    dict_items([('Banana', 20), ('Apple', 34), ('Orange', 12)])
    34
    Apple
    


```python
#We want ot allow uset to query different blood type personaliteis from the dictionary
# A = introverted / steeady
#  B Outgoing / Optimistic
# AB Inteligent / natural
bloodTypes = {"A": ["Introverted", "Steady"], "B":["Outgoing","Optimistic"], "AB":["Inteligent","natural"]}
userInput = input("Please select the blood type you are looking for")
if userInput in bloodTypes:
    print(f"{userInput} is a valid blood type")
    userInput2 = input("Please select property you are looking for")
    if userInput2 in bloodTypes[userInput]:
        print(f"the {userInput2} property found")
    else:
        print(f"{userInput2} property not found")
else:
    print(f"{userInput} is not a valid blood type")
```

    5 is not a valid blood type
    

### QUIZ



```python
 soundtrack_dict = {"The Bodyguard": "1992", "Saturday night fever": "1977"}
print(soundtrack_dict)
```

    {'The Bodyguard': '1992', 'Saturday night fever': '1977'}
    


```python
print(f"The key from the soundtrack_dict are {soundtrack_dict.keys()}")
```

    The key from the soundtrack_dict are dict_keys(['The Bodyguard', 'Saturday night fever'])
    


```python
print(f"Values from the soundtrack_dict are: {soundtrack_dict.values()}")
```

    Values from the soundtrack_dict are: dict_values(['1992', '1977'])
    

### This is end for the dictionaries

## Sets
sets is unique objects, that will automatically remove duplicates. Set is defined by the { }
Sets stores nonsequentional data. It uses UNION, INTERSECTION, DIFFERENCE operations.


```python
s = {1,2,3,4,5}
print(s)
s = set(("a",1,"b",2))
print(s)
print("SEPARATOR\n\n")
s = set(["Apple","Banana","Apple"])
print(s)
print("SEPARATOR\n\n")
s = set({"GOOD MORNING":"GOOD MORNING","HELLP":"HELLP"})
print(s)
print("SEPARATOR\n\n")
s = set("racecar")
print(s)
```

    {1, 2, 3, 4, 5}
    {1, 'b', 2, 'a'}
    SEPARATOR
    
    
    {'Apple', 'Banana'}
    SEPARATOR
    
    
    {'HELLP', 'GOOD MORNING'}
    SEPARATOR
    
    
    {'r', 'e', 'a', 'c'}
    


```python
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B","rock", "disco"}
set1
```




    {'R&B', 'disco', 'hard rock', 'pop', 'rock', 'soul'}




```python
album_list = ["Michael Jackson","Thriller", 1982, "00:42:19","Pop, Rock, R&B", 46.0, 65, None, 10.0]
album_set = set(album_list)
print(album_set)

A = set(["Thriller", "Back in black", "AC/DC"])
A.add("Pepe The Frog")
print(A)
A.add("Pepe The Frog")
print(A)
A.remove("Pepe The Frog")
print(A)
print("Pepe gone :(")

print("AC/DC" in A)

print("Pepe The Frog" in A)

print("No pepe :(")

A.add("Pepe The Frog")
print("Pepe The Frog" in A)
print("Pepe back :)")
print(A)
```

    {None, 65, 'Michael Jackson', '00:42:19', 10.0, 46.0, 'Thriller', 'Pop, Rock, R&B', 1982}
    {'Thriller', 'Back in black', 'Pepe The Frog', 'AC/DC'}
    {'Thriller', 'Back in black', 'Pepe The Frog', 'AC/DC'}
    {'Thriller', 'Back in black', 'AC/DC'}
    Pepe gone :(
    True
    False
    No pepe :(
    True
    Pepe back :)
    {'Thriller', 'Back in black', 'Pepe The Frog', 'AC/DC'}
    


```python
s2 = set("Schwerer Panzerspähwagen Sd. Kfz. 234/2")
print(s2)
s2.remove("/")
print(s2)
s2.add("b")
print(s2)
```

    {'3', 'z', 'r', '2', 'w', 'd', 'p', '.', 'ä', 'P', '4', 'n', ' ', 'e', 's', 'f', 'h', 'K', '/', 'a', 'S', 'c', 'g'}
    {'3', 'z', 'r', '2', 'w', 'd', 'p', '.', 'ä', 'P', '4', 'n', ' ', 'e', 's', 'f', 'h', 'K', 'a', 'S', 'c', 'g'}
    {'3', 'b', 'z', 'r', '2', 'w', 'd', 'p', '.', 'ä', 'P', '4', 'n', ' ', 'e', 's', 'f', 'h', 'K', 'a', 'S', 'c', 'g'}
    


```python
album_set1 = set(["Thriller","AC/DC","Back in black"])
album_set2 = set(["AC/DC","Back in black","The Dark Side Of The Moon"])
print(album_set1.intersection(album_set2))
print(album_set1.union(album_set2))

a = set("tiger")
b = set("bear")

print(f"The union of a and b elements are: {a|b}")

print(a&b)
intersection = album_set1 & album_set2
print("The intersection between albums are",intersection)

differencer = a-b
print("The difference a-b is", differencer)
print("h , u, b")

albumDifference = album_set1 - album_set2
print("The difference between albums are/is\n",albumDifference)

albumDifference2 = album_set2 - album_set1
print("The difference between albums are/is\n",albumDifference2)

intersecionOfAlbums = album_set1 & album_set2
print(f"intersection between albums is {intersecionOfAlbums}\n")

print(f"The difference by function is: {album_set2.difference(album_set1)}\n")

print(f"Union by function is {album_set2.union(album_set1)}\n")

print(f"Union by explicit is {album_set2 | album_set1}\n")

print(f"Subset by the function gets {album_set2.issubset(album_set1)}\n")
```

    {'AC/DC', 'Back in black'}
    {'The Dark Side Of The Moon', 'Thriller', 'AC/DC', 'Back in black'}
    The union of a and b elements are: {'g', 'r', 'i', 'b', 'a', 'e', 't'}
    {'r', 'e'}
    The intersection between albums are {'AC/DC', 'Back in black'}
    The difference a-b is {'i', 't', 'g'}
    h , u, b
    The difference between albums are/is
     {'Thriller'}
    The difference between albums are/is
     {'The Dark Side Of The Moon'}
    intersection between albums is {'AC/DC', 'Back in black'}
    
    The difference by function is: {'The Dark Side Of The Moon'}
    
    Union by function is {'The Dark Side Of The Moon', 'Thriller', 'AC/DC', 'Back in black'}
    
    Union by explicit is {'The Dark Side Of The Moon', 'Thriller', 'AC/DC', 'Back in black'}
    
    Subset by the function gets False
    
    


```python
#Subset test
AA = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"}
BB = {"a", "d", "f"}
print(f"Is the B subset of A? {BB.issubset(AA)}")

a = a
b = b

#print(a,b)
#TODO Find explanation for a^b
print(a^b)

#Is subset <=
print(f"Is B subset of A? explicit approach: {BB <= AA}")

#Proper subset >
#TODO find difference between subset and proper subset
print(f"Is B proper subset of A? {BB>AA}")

#Superset >= or issuperset() - Every element exists in both sets
print(f"Is AA superset of BB? {AA>=BB}")

#Super set
#Every element that exists in set B must also exist in set A, but at least one element of set A does not exist in set B, then True is returned
#Program here
```


      Cell In[30], line 25
        print(f"{}")
                 ^
    SyntaxError: f-string: valid expression required before '}'
    



```python
#Review Q1
listA = ["rap", "house", "EDM", "rap"]
setA = set(listA)
print(setA)


#Review Q2
#Prediction no
A = [1, 2,2, 1]
B = set([1,2,2,1])
sum(A) == sum(B)
#Because set will be {1,2}
print(B)

#Review Q3
album_set3 = album_set1.union(album_set2)
print(album_set3)

#Review Q3
print(f"Is almbum_set1 usbest of albumset3? : {album_set1.issuperset(album_set3)}")

#Review Q4
```

    {'rap', 'EDM', 'house'}
    {1, 2}
    {'The Dark Side Of The Moon', 'Thriller', 'AC/DC', 'Back in black'}
    Is almbum_set1 usbest of albumset3?: False
    
