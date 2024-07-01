import time
def selection_sort(my_list):
    n = len(my_list)
    for i in range(n):
        max_I = 0
        for j in range(1, n - i):
            if my_list[j] > my_list[max_I]:
                max_I = j
        my_list[max_I], my_list[n - i - 1] = my_list[n - i - 1], my_list[max_I]
    return my_list
input_list = [int(x) for x in input("Enter numbers separated by space: ").split()]
print("Original list:", input_list)

start_time = time.time()
sorted_list = selection_sort(input_list)
end_time = time.time()

print("Sorted list:", sorted_list)
print("Time taken:", end_time - start_time, "seconds")