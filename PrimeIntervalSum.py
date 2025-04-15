# Function to check whether a number is prime
def isPrime(n):
    # 2 and 3 are prime numbers
    if n == 2 or n == 3:
        return True
    elif n > 3:
        # Check divisibility from 2 up to the square root of n
        for i in range(2, 1 + int(n**0.5)):
            if n % i == 0:
                return False
    # Return True if no divisors found (i.e., it's prime)
    return True

# Initialize an empty list to store prime numbers
list = []

# m and n define the starting index and number of primes to sum respectively
m = 6
n = 2

# Counter for how many prime numbers have been found
count = 0

# Start checking from the first prime number
p = 2

# Loop until we collect (m + n) primes
while count <= m + n:
    if isPrime(p):
        list.append(p)
        count += 1
    p += 1

# Initialize sum
sum = 0

# Sum the n prime numbers starting from the (m-1)th index
for i in range(m - 1, m + n):
    sum = sum + list[i]

# Output the list of prime numbers and the calculated sum
print(list)
print(sum)
