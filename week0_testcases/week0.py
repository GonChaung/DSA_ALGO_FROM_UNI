def print_numbers(n):
    for i in range(1,n+1):
        print(i)

# n = int(input("How many integers do you want to input : "))
# print_numbers(n)

def read_numbers():
    numbers = list(map(int, input("Enter a sequence of integers separated by spaces: ").split()))
    return numbers

def print_oddNumbers():
    print("Odd numbers in the list:")
    for num in numbers:
        if num % 2 != 0:
            print(num)

numbers = read_numbers()
print_oddNumbers(numbers)