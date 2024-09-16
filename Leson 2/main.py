import sys

def versioncheck():
    print(f"{sys.version} \n \n") #To ensure we use python version 3.0+

def datatypes():
    myData = [True, False, 10, 11, 12, 13.0, 0, 0.0,"string", "1", "11"]
    for i in range(0,len(myData),1):
        print(f"{myData[i]} has data type {type(myData[i])}\n ")
    x = 10
    print(f"The x value is {x} and type {type(x)}\n ")
    x = 11
    print(f"The x value is now {x} and type {type(x)}\n ")
    x = float(x)
    print(f"The x value is now {x} and type can be changed to {type(x)}\n ")
    #Don't forget for comments so you know what you are doing!
    #This is a comment ;
    print("The int is still int, no matter if he is positive or negative. Same is for float!\n ")
    for a in range(-10,10,1):
        print(f"{a} has data type of {type(a)}\n")


def main():
    print("This is summary of t he lecture 1 nad lecture 2\n")
    versioncheck()
    datatypes()

main()