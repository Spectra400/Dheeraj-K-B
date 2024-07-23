# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Main function to take user input and display the result
def main():
    try:
        # Take input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Call the add_numbers function
        result = add_numbers(num1, num2)
        
        # Display the result
        print(f"The sum of {num1} and {num2} is {result}")
        
    except ValueError:
        print("Invalid input! Please enter numerical values.")

# Run the main function
if __name__ == "__main__":
    main()
