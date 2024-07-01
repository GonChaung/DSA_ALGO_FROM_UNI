def print_numbers(n):
    for i in range(1,n+1):
        print(i)

n = int(input("How many integers do you want to input : "))
#print_numbers(n)

# Insertion sort
# for i in range(1, len(a)):
#     j = i
#     while j > 0 and a[j - 1] > a[j]:
#         # Swap
#         a[j], a[j - 1] = a[j - 1], a[j]
#         j -= 1

n = 9 // 2
print(n)

# def mergesort(A, p, r):
#     if p < r:
#         q = (p + r) // 2
#         mergesort(A, p, q)
#         mergesort(A, q + 1, r)
#         merge(A, p, q, r)