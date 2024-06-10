def read_numbers():
    numbers = list(map(int, input("Enter a sequence of integers separated by spaces: ").split()))
    return numbers
def print_oddNumbers(numbers):
    print("Odd numbers in the list:")
    for num in numbers:
        if num % 2 != 0:
            print(num)
def print_largest_even(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    if even_numbers:
        largest_even = max(even_numbers)
        print("Largest even number:", largest_even)
    else:
        print("No even numbers in the list")
def print_even_numbers_reverse(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    print("Even numbers in reverse order:")
    for num in range(len(even_numbers)-1, -1, -1):
        print(even_numbers[num])

numbers = read_numbers()
print_oddNumbers(numbers)
print_largest_even(numbers)
print_even_numbers_reverse(numbers)