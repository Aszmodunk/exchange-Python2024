# String Operations

# Example 1: Basic string declaration
name = "Michael Jackson"
print(name)  # Output: Michael Jackson

# Example 2: String indexing
print(name[0])  # Output: M (first character)
print(name[-1])  # Output: n (last character)

# Example 3: Slicing strings
print(name[0:7])  # Output: Michael (first 7 characters)
print(name[::2])  # Output: McalJcsn (every second character)

# Example 4: String length
print(len(name))  # Output: 15

# Example 5: Combining strings
statement = name + " is a great artist."
print(statement)  # Output: Michael Jackson is a great artist.

# String Manipulation

# Example 1: Upper and lower case conversion
A = "Hello World"
B = A.upper()
print(B)  # Output: HELLO WORLD

C = B.lower()
print(C)  # Output: hello world

# Example 2: Replacing part of a string
text = "I love coding."
new_text = text.replace("coding", "Python")
print(new_text)  # Output: I love Python.

# Example 3: Finding a substring
D = "Python is amazing!"
print(D.find("amazing"))  # Output: 10 (index of the first letter of "amazing")

# Example 4: String concatenation with multiplication
statement = "Python is fun!\n"
print(3 * statement)  # Output: The string printed three times

# Example 5: Stripping whitespace
text_with_spaces = "   Hello Python!   "
print(text_with_spaces.strip())  # Output: "Hello Python!"

# User Interaction with input()

# Example 1: Simple input interaction
name = input("What is your name?\n")
print(f"Nice to meet you, {name}!")

# Example 2: Input with integer manipulation
number = int(input("Enter a number: "))
print(f"{number} + 1 is {number + 1}")

# Example 3: Input with string concatenation
hobby = input("What is your hobby?\n")
print(f"Your hobby is {hobby}. That's awesome!")

# Example 4: Multiplying input strings
repeat_text = input("Enter something to repeat:\n")
print(repeat_text * 3)  # Output: The input repeated 3 times

# Example 5: Calculating square of a number
number = int(input("Enter a number to square: "))
print(f"The square of {number} is {number ** 2}")

# String Methods

# Example 1: split() method
sentence = "Learning Python is fun"
words = sentence.split()
print(words)  # Output: ['Learning', 'Python', 'is', 'fun']

# Example 2: Checking if string starts/ends with a certain substring
print(sentence.startswith("Learning"))  # Output: True
print(sentence.endswith("fun"))  # Output: True

# Example 3: Counting occurrences of a substring
print(sentence.count("i"))  # Output: 2 (number of occurrences of "i")

# Example 4: Joining a list of strings
words_list = ['Python', 'is', 'cool']
sentence = ' '.join(words_list)
print(sentence)  # Output: Python is cool

# Example 5: Capitalizing the first letter of each word
title_text = "python is amazing"
print(title_text.title())  # Output: Python Is Amazing

# String Escaping & Special Characters

# Example 1: Using newline \n
text = "Hello\nWorld"
print(text)  # Output: "Hello" on one line and "World" on the next

# Example 2: Using tab \t
text = "Name:\tJohn"
print(text)  # Output: Name:	John

# Example 3: Escaping quotes
quote = "He said, \"Python is awesome!\""
print(quote)  # Output: He said, "Python is awesome!"

# Example 4: Escaping backslashes
path = "C:\\Users\\JohnDoe\\Documents"
print(path)  # Output: C:\Users\JohnDoe\Documents

# Example 5: Using carriage return \r
text = "Hello World\rPython"
print(text)  # Output: Pythonld (Python overwrites part of Hello World)
