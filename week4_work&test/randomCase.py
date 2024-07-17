import sys
import random

if len(sys.argv) < 2:
    print("Usage: python randomCase.py <n>")
    sys.exit(1)

n = int(sys.argv[1])

# Generate random numbers
random_numbers = []
for _ in range(n):
    num = random.randint(-2 * n, 4 * n - 1)
    random_numbers.append(num)

print(' '.join(map(str, random_numbers)))
