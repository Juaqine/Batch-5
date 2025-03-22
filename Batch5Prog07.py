#Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.
#Example:
#Input: We will weather the weather whatever the weather whether we like it or not
#Output: 14

#Ask user for a complete statement
#Count the words in the statement
#Print the word count

statement = input("Enter a complete statement: ")
print(len(statement.split()))
