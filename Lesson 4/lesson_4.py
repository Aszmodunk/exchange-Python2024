def years(year):
    if (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0): #Uses logic function to make clenaer code (for me)
     return 1
    else:
        return 0


def main():
    year = input("Input year in Gregorian calendar: ")
    result = years(int(year)) #Here we must declare that year variable will be passed as int, or it will be passed as string

    if result == 1:
        print(f"{year} is a leap year")

    else:
        print(f"{year} is not a leap year")


main() #Uses one main function, something I took from C
