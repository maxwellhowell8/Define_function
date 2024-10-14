# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract_numbers(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply_numbers(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide_numbers(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero is not allowed"

# Main program to take input from the user and perform calculations
def main():
    # Taking input from the user
    try:
        num1 = float(input("Enter the first number (num1): "))
        num2 = float(input("Enter the second number (num2): "))
        
        # Performing addition
        addition_result = add_numbers(num1, num2)
        
        # Performing subtraction
        subtraction_result = subtract_numbers(num1, num2)
        
        # Performing multiplication
        multiplication_result = multiply_numbers(num1, num2)
        
        # Performing division
        division_result = divide_numbers(num1, num2)
        
        # Displaying results
        print(f"The addition of {num1} and {num2} is: {addition_result}")
        print(f"The subtraction of {num1} and {num2} is: {subtraction_result}")
        print(f"The multiplication of {num1} and {num2} is: {multiplication_result}")
        print(f"The division of {num1} and {num2} is: {division_result}")
    
    except ValueError:
        print("Invalid input. Please enter numerical values.")

# Calling the main function
if __name__ == "__main__":
    main()
