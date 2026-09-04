# Strings - sequence of characters
#enclosed in quotes
alpha = 'aaaaa'
name = 'aaaaa'
name= "NAME"

age = 20
salary = 20.366
active = True

# Features
# ordered
# indexing
# slicing
# Allows duplicates
# Immutable - cannot be changed

name = "   python   "
print(name[0])
# name[0] = 'J'
new_name = name + "Course"

print(name[1])

print(name.upper()) # change to uppercase
print(name.capitalize()) # change the first letter to capital
print(name.lower()) # change to lowercase

sentence = "my name is alice"
print(sentence.title())# coverts the first letter of each word to capital

str = "     alice    "
print(len(str.strip())) # removes spaces from beginning and end

print(sentence.replace("alice", "rupa")) # Replaces a word or character

text = "Apple Mango Orange grapes"
print(text.split()) # converts a string into a list

Names = "Rupa3Alice3Rahul3Ravi"
print(Names.split('3'))

fruits = ["Apple", "Orange"]
print(" ".join(fruits)) # convert to list elements into a string

print(Names.find("Yes"))
print(Names.find("R")) # Finds the index of a character

text1 = "bananananananananananananananananananana"
print(text1.count("n")) # counts occurences of a character

language = "python"
print(language.startswith("ja")) # checks if string starts with given value
print(language.endswith("on")) # Checks if string ends with given value


str1 = "Pythom123"
str2 = "Python"
print("Is Alphabet : ")
print(str1.isalpha())
print(str2.isalpha()) # check whether all characters are alphabets

print("IS Digit : ")
str3 = "122345"
str4 = "java123"
print(str3.isdigit())
print(str4.isdigit()) # check whether all characters are digits


print(str4.isalnum()) # check whether string characters only letters and numbers

str5 = "%@@@@@@@@@@$^&*)(@!"
print(str5.isalpha())










print(new_name)

# text = "aaaaaaa"
# print(text.upper())
#
# text1 = "AAAAAA"
# print(text.lower())
#
# print(text.capitalize())
#
# list = [1,2]
# list1 = [5,3,6]
# list.extend([3,4])
# list.extend([list1])
# print(list)
#
# print(list.index(2)) # return number
# print(len(list)) # return number
#
# print(list.extend([7,8])) # not return
#
# print(list)