int1=int(raw_input("Enter the first integer: "))
int2=int(raw_input("Enter the second integer: "))
print int1+int2

#Note that this program doesn't check if the inputted values are actually integer, it'll throw an error if not by default design of the int() function

# Alternative using input, rather than raw input:

int1 = input("Enter the First Integer: ")
int2 = input("Enter the Second Integer: ")
print int1 + int2