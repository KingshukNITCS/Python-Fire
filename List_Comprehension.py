squares = [x**2 for x in range(5)]
print(squares)


even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)


matrix = [[i * j for j in range(3)] for i in range(4)]
print(matrix)
#Output - [[0, 0, 0], [0, 1, 2], [0, 2, 4], [0, 3, 6]]


letters = ['a', 'b', 'c']
uppercase_letters = [letter.upper() for letter in letters]
print(uppercase_letters)


# Problem Statement - Write a program to print Prime numbers in a given range.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to generate a list of prime numbers in a range
def primes_in_range(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]

start_range = int(input("Enter the starting number of the range: "))
end_range = int(input("Enter the ending number of the range: "))

result = primes_in_range(start_range, end_range)
print(f"Prime numbers in the range ({start_range}, {end_range}): {result}")
      
