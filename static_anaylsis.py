# Define a function named 'add' that takes two arguments, 'number1' and 'number2'.
def add(number1, number2):
    # The function returns the sum of 'number1' and 'number2'.
    return number1 + number2

num1 = 4
num2 = 5

# Call the 'add' function with 'num1' and 'num2' as arguments and store the result in 'total'.
total = add(num1, num2)

# Print the result of adding 'num1' and 'num2' using the 'format' method to insert the values into the string.
print("The sum of {} and {} is {}".format(num1, num2, total))


'''
Run pylint from the command line:
Open the command prompt or terminal and directly run the command:
pylint static_anaylsis.py 

'''