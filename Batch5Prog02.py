#Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.
#Example:
#Input: 143
#Output: 000143

#Ask user for a number between 0 and 1000
#Convert number to a 6-digit format with leading zeros
#Print the result

number = int(input("Enter a number (0-1000): "))
print(f"{number:06}")
