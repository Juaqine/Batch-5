#Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.
#Example:
#Input: Juan Dela Cruz
#Output: Juan Dela Cruz

#Ask user for full name input
#Remove leading spaces
#Print the result

fullname = input("Enter your full name: ")
print(fullname.lstrip())
