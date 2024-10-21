### __Python lesson 3__

# __Today's topoc: String operations__

In python __stings__ are as _sequence of characters_. They are declared by the `" "` that also includes _spaces and special characters_.

Let's have an example:


```python
name = "Michael Jackson"
print(name)
```

    Michael Jackson
    

We declared string with python, as said above, string is set of characters. So we can use positions to print individual characters. We can use negative indexing too `name[-1]` is similar to the `name[0]` but is going from the opposite side if the string, since the 0 can't be negative, the `-1` is the first letter in this case.


```python
print(f"{name[0]}\n") # Print first character
print(f"{name[0:4]}\n") # Print character from 0 to 4
print(f"{name[::2]}\n") # Print every even character
#Negaitve index can be used too!
print(name[-1])
```

    M
    
    Mich
    
    McalJcsn
    
    n
    

Same with lists we can use `len()` function to get lenght of the string __with speciall characters and spaces!__


```python
len(name)
```




    15



We can combine strings. Just "as is"___*___ or via _variables_. Both cases are seen below.

___*___ _It is important to notice, that we need to add extra space before the combination of the strings, since the space is considered as an character!_


```python
statment = name + " is the best!"
print(statment)
```

    Michael Jackson is the best!
    


```python
print(f"{3*(statment+"\n")}") # math!
```

    Michael Jackson is the best!
    Michael Jackson is the best!
    Michael Jackson is the best!
    
    

# String manipmulation 
It is ___not possible___ to manipulate stings like `name[0]=J`, but we can create new strings like in the `statment` above.

We can use backshlash _(as we used several times above)_ to manipulate string behaviour, where __`"\n"`__ forces the text for the new line. It does not have to be at the end necesarly, it can be also in the middle _(or anywhere)_ in the string for example `"My mom is sweet\n caring\n and \n has big smile"`


```python
print("My mom is sweet\n caring\n and\n has big smile")
```

    My mom is sweet
     caring
     and
     has big smile
    

As can be seen above, it is important to remeber that space is considered character

The `\t` results in `   ` tab, who would have guessed!
If we need `\` in the text we can type  `\\`


```python
print("Look at it go! \\ Look at me go!")
```

    Look at it go! \ Look at me go!
    

We can  type `print(r"Michael jackson \ is the best")` results in the __raw string__ where all formating is ignored.


```python
print(r"This is \n an example \t of the raw \ string!/")
```

    This is \n an example \t of the raw \ string!/
    

## String sequence methods
When we apply methond to the stryng A we get string B. Can be achieved by method like `B = A.upper()` wich will result in B be identical to the _original stinrg_ A, but with `upper()` modification. There also exists function `lower()` where we take copy of the sting _(in our case B)_ and transfer it to the lower.


```python
A = "I am thrilled to be here and experience this wonderful event!"
print(A)

B = A.upper()
print(B)

C = B.lower()
print(C)
```

    I am thrilled to be here and experience this wonderful event!
    I AM THRILLED TO BE HERE AND EXPERIENCE THIS WONDERFUL EVENT!
    i am thrilled to be here and experience this wonderful event!
    

Another method of manipulation is `replace("What we look for", "What we want to replace it with")`


```python
D = C.replace("event", "food")
print(D)
```

    i am thrilled to be here and experience this wonderful food!
    

We can locate the specific positions of the characters with function `find()` let's have an example below.


```python
print(f"Position of the food! is: {D.find("food!")}\n")
print(f"The total lenght of the string is: {len(D)}\n")
print(f"If we try to search for something that doesn't exist like a dog we get: {D.find("dog!")}\n")
```

    Position of the food! is: 55
    
    The total lenght of the string is: 60
    
    If we try to search for something that doesn't exist like a dog we get: -1
    
    

### Interaction with the users
`print()` is basic function that can interact with the user, to some extent, of course we won't get any feedback. That is where the `input()` comes in. It can be used "as is" ___BUT!___ we need to have ability to store data from the user. That's why we usually associate it with a variable. Like `newName = input("My name is: \n")` as you can see, we can put some arguments inside the `input()` function too.

_Important note, all outputs are stings, unless we define otherwise!_


```python
print("Hello what is your name?\n")
newName = input("My name is: \n")
print(f"Nice to meet you {newName}! Excited to work with you!\n")
```

    Hello what is your name?: 
    
    

    My name is: 
     Jashuo
    

    Nice to meet you Jashuo! Excited to work with you!
    
    


```python
newNumber = input("Input new number: ")
print(int(newNumber) + 1)

anotherNumber = int(newNumber)
print(f"The power of two for {newNumber} is {anotherNumber **2}\n")
```

    Input new number:  55
    

    56
    The power of two for 55 is 3025
    
    

_As can be seen above, to manipulate with input to get number, can be bit tricky but not impossible. We can also make it always be in by `newNumber = int(input("text"))`_


We also gain new knowledge that __something to the power of two__ is achieved by `**2`

We learned about the another function of `split()` splits seperate words into the list.


```python

```
