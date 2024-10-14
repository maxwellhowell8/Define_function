# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract_numbers(num1, num2):
    return num1 - num2

# Main program to take input from the user and perform the calculations
def main():
    # Taking input from the user
    try:
        num1 = float(input("Enter the first number (num1): "))
        num2 = float(input("Enter the second number (num2): "))
        
        # Performing addition
        addition_result = add_numbers(num1, num2)
        
        # Performing subtraction
        subtraction_result = subtract_numbers(num1, num2)
        
        # Displaying results
        print(f"The addition of {num1} and {num2} is: {addition_result}")
        print(f"The subtraction of {num1} and {num2} is: {subtraction_result}")
    
    except ValueError:
        print("Invalid input. Please enter numerical values.")

# Calling the main function
if __name__ == "__main__":
    main()
