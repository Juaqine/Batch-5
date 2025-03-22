#Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
#Example:
#Input: jUAn DEla CrUZ
#Output: juan_dela_cruz

#Ask user for full name input
#Convert all characters to lowercase
#Join words with underscores
#Print the result

fullname = input("Enter your full name: ")
print('_'.join(word.lower() for word in fullname.split()))
