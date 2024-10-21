### __Python lesson 3 homework__



## Assigment
BMI value calculation formula: BMI = weight (kg) / height**2

For example: a 52 kg person with a height of 155 cm would have a BMI of:
52(kg)/(1.55*1.55) = 21.6
The normal range of weight is BMI=18.5~24

[1] Please ask the user to enter their height and weight.

[2] Calculate the BMI value and output it on the screen.


```python
weight = float(input("Please enter your weight in [kg]: \n"))
height = float(input("Please enter your height in [cm]: \n"))
height = height/100
BMI = weight/(height**2)

if BMI < 18.5:
    print(f"Your BMI ({BMI}) is underweight")
elif BMI > 24:
    print(f"Your BMI ({BMI}) is overweight")
else:
    print(f"Your BMI ({BMI}) is within healthy limits")
```

    Please enter your weight in [kg]: 
     52
    Please enter your height in [cm]: 
     155
    

    Your BMI (21.64412070759625) is within healthy limits
    


```python

```
