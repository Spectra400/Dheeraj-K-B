def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
num = int(input("Enter a number: "))
fact = factorial_iterative(num)
print(f"Factorial of {num} is {fact}")
