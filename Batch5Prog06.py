#Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.
#Example:
#Input: jUAn DEla CrUZ
#Output: JuaN deLA cRuz

#Ask user for full name input
#Swap uppercase to lowercase and vice versa
#Print the result

fullname = input("Enter your full name: ")
print(fullname.swapcase())
