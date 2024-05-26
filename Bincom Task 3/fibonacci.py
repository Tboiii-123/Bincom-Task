
# Implementing a Fibonacci serires generator
def fibonacci(n):

  if n <= 1:
    return 1
    
  else:
    a, b = 1,1
    for i in range(2, n + 1):
      c = a + b
      a = b
      b = c
    return c

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = []
for i in range(num_terms):
  #Appending the result to the fibnonacci_sequence
  fibonacci_sequence.append(fibonacci(i))

# Print the Fibonacci sequence
print(fibonacci_sequence)


