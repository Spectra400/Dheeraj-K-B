def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage
num_terms = int(input("Enter the number of terms: "))
fib_sequence = fibonacci(num_terms)
print("Fibonacci sequence:")
print(fib_sequence)
