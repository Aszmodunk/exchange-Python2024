## Operators
We can use operators as `==` *equals to* or `!=` *not equal to* `< or >` *higher or lower* ` <= or >=` *higher or equal to or lower or equal to*


```python
a = 10
A = 11
```


```python
a == A
```




    False




```python
a < A
```




    True




```python
A != a
```




    True




```python
"A" == "a"
```




    False




```python
"A" == "A"
```




    True




```python
"a" != " a"
```




    True




```python
"A" < "B"
```




    True



![asciifull.gif](pythonLesson05_files/10b94b1a-7404-42e3-a53e-d2d22388b65a.gif)

There is a table for reference. WHen we compare multiple `"strngs"` only first one is considered


```python
legal_limit = 21
age = input("enter your age: ")
age = int(age)

if int(age) > legal_limit:
    print("You are allowed to enter.")
elif int(age) == legal_limit:
    print("Maybe you should reconsider.")
else:
    print("You can not enter.")


print("Have a nice day.")
```

    enter your age:  25
    

    You are allowed to enter.
    Have a nice day.
    

<div class="alert alert-block alert-info">
It is important to keep in mind, that <b>input()</b> function returns the user input in the <b>str()</b> format. To use it as numerical we can use <b>var = <b>int(var)</b> or declare it as above <b>int(var)...</b>>
</div>

## Python code indentation. 
It is recommended to use tb or the 4 spaces

`def main():`

`    code #The tab showing it into the function.`

it's basically the `{ }` C/C++


```python
a = 3
if (a > 2):
    print(1)
if (a > 2):
    print(2)
if (a > 2 or a < 6):
    print(3)
if (a > 2 and not a < 6):
    print(4)

#Maybe python has switch cases?
```

    1
    2
    3
    


```python
score = int(input("Please enter your score: \n"))
msg = "You ahve failed the test."
if score > 60:
    msg = "You have passed the test"
print(msg)

#The goal was to use only one if statment to solve this. Solution, owerride the value of msg. It taught us to not overthink! Simplicity is the way!
```

    Please enter your score: 
     101
    

    You have passed the test
    


```python
id = "Agent007"
pswd = "0857"
tokens = 10 #I misunderstood teacher and made tokening system, comented out code is the implementation if said system

while (tokens != 0):
    checkId = input("Enter your id: \n")
    prompt = input(f"Enter your password for account {checkId}: ")
    if prompt == pswd and checkId == id:
        print("Hello, welcome!\n")
        break #This would be call for another function
    else:
        #print(f"Wrong password! {tokens} tries left!\n")
        tokens = tokens -1
        break
        #continue
```

    Enter your id: 
     Agent007
    Enter your password for account Agent007:  0857
    

    Hello, welcome!
    
    


```python
fare = 85 # first 5 km
extra = 10 # each km after 5
km = int(input("Set the distance: \n"))
price = 0

price = (km-5)*extra + fare

if km <= 5:
    price = fare
   

print(f"For the distance of {km} the price will be NT${price}!")
```

    Set the distance: 
     6
    

    For the distance of 6 the price will be NT$95!
    


```python
#Ambulance
#Nursing 700/hr, Doctor 1 500/hr
#We need to input km, if nursing staff or doctor is needed on board
#avg speed je 60km/hr
nurse = 700
doctor = 1500

km = int(input("Km?: \n"))
basicFee = 800 + (km*25)

print("What staff is required? \n1) Nursing\n2) Doctor\n3) Both")
staff = int(input())

staffFee = 0
if staff == 1:
    staffFee = nurse
elif staff == 2:
    staffFee = doctor
elif staff == 3:
    staffFee = nurse + doctor

finalCost = (km/60)*(staffFee+basicFee)

print(finalCost)
```

    What staff is required? 
    1) Nursing
    2) Doctor
    3) Both
    16875.0
    


```python

```
