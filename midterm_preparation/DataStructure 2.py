#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Sorts a sequence in ascending order using the insertion sort alogorithm.
def insertionSort(theSeq):
    n=len(theSeq)
    #Starts with the first item as the only sorted entry.
    for i in range(1,n):
        value = theSeq[i]
        #Find the position where value fits in the ordered part of the list.
        pos = i
        while pos>0 and value<theSeq[pos-1]:
            #Shift the items to the right during the search.
            theSeq[pos] = theSeq[pos-1]
            pos-=1
        #Put the saved value into the open slot.
        theSeq[pos]=value
    return theSeq
print(insertionSort([23,78,45,8,32,56]))


# In[ ]:


#Insertion Sort
Big-O notation,O(n^2)
#Starts with 1st item->Find position where value fits->Shifts the items to the right during the search->Put the saved value in open slots


# In[9]:


def insertionSort(A,n): #cost time
    for i in range (1,n):
        key = A[i]
        j = i-1
        while j>=0 and A[j]>key:
            A[j+1] = A[j]
            j = j -1
        A[j+1] = key
    return A
 
print(insertionSort([23,78,45,8,32,56], 6))


# In[ ]:


Certainly! The provided Python code implements the Insertion Sort algorithm. Here's a condensed explanation:
 
1. **Initialize:**
   - Start with the second element (index 1) since the first is considered sorted.
 
2. **Compare and Insert:**
   - For each element, compare it with the elements on its left until a smaller element is found or the beginning of the array is reached.
   - Shift larger elements to the right.
   - Insert the element into the correct sorted position.
 
3. **Repeat:**
   - Repeat this process for each unsorted element.
 
4. **Result:**
   - The array becomes progressively sorted.
 
5. **Example:**
   - For the input `[23, 78, 45, 8, 32, 56]`:
     - After the first iteration: `[23, 45, 78, 8, 32, 56]`
     - After the second iteration: `[8, 23, 45, 78, 32, 56]`
     - After the third iteration: `[8, 23, 32, 45, 78, 56]`
     - Sorted Array: `[8, 23, 32, 45, 56, 78]`
 
The key idea is to build a sorted portion of the array gradually, inserting each element into its correct position.
has context menu


# In[ ]:


#Title: Running Time Analysis of Insertion Sort on Array A

Introduction: Insertion Sort is a simple algorithm that sequentially builds a sorted array by inserting one element at a time. While not as efficient for large lists as advanced algorithms, such as quicksort or mergesort, Insertion Sort is suitable for small datasets or partially sorted data. This analysis focuses on the running time of Insertion Sort applied to a specific array, denoted as A, with elements [1,2,3,4,5,6,7,8,9,10].

Insertion Sort Algorithm: The algorithm divides the input array into sorted and unsorted subarrays. It iterates through the unsorted subarray, selecting an element and inserting it into the correct position in the sorted subarray. This process continues until the entire array is sorted.

Running Time Analysis: The analysis includes best-case, average-case, and worst-case scenarios.

Best-case Scenario: When the input array is already sorted, Insertion Sort minimizes swaps, resulting in a best-case time complexity of O(n), where n is the number of elements.

Average-case Scenario: In random order, each element, on average, compares and swaps with approximately n/2 elements, leading to an average-case time complexity of O(n^2).

Worst-case Scenario: In reverse order, each element in the unsorted subarray compares and swaps with every element in the sorted subarray. The worst-case time complexity is O(n^2).

Conclusion: Insertion Sort's performance varies based on the initial order of elements. While it achieves linear time complexity in the best-case scenario, its average and worst-case time complexities are quadratic. This positions Insertion Sort as less efficient than other sorting algorithms, like quicksort or mergesort, for larger datasets or arrays with random or reverse-ordered elements.


# In[ ]:


a concise summary of insertion sort code:

- **Function Definition:**
  - `insertionSort(A, n)`: Sorts array `A` of size `n` using insertion sort.

- **For Loop:**
  - Iterates through the array from the second element.

- **Key Selection:**
  - Selects the current element as the key to be inserted.

- **Inner While Loop (Sorting):**
  - Shifts elements to the right until finding the correct position for the key.

- **Insertion:**
  - Inserts the key into its correct sorted position.

- **Return:**
  - Returns the sorted array.

- **Print Result:**
  - Calls `insertionSort` and prints the sorted array.

This algorithm efficiently sorts the input array in ascending order using insertion sort.


# In[ ]:


Certainly! Here are the arrays at each step of the insertion sort algorithm:

1. `[23, 78, 45, 8, 32, 56]`
2. `[23, 78, 45, 8, 32, 56]`
3. `[23, 45, 78, 8, 32, 56]`
4. `[8, 23, 45, 78, 32, 56]`
5. `[8, 32, 23, 45, 78, 56]`
6. `[8, 32, 23, 45, 56, 78]`

The final sorted array is `[8, 23, 32, 45, 56, 78]`.


# In[ ]:


...............................................................................................................................
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\................................................................................................................................


# In[ ]:


#Merge sort
def merge(A, p, q, r):
    B = []
    i = p
    j = q+1
    while i <= q and j <= r:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1
    A[p:r+1] = B + A[i:q+1] + A[j:r+1]

def mergesort(A, p, r):
    if p < r:
        q = (p+r)//2
        mergesort(A, p, q)
        mergesort(A, q+1, r)
        merge(A, p, q, r)
    



a = list(map(int, input().split()))

import time

st = time.process_time()

mergesort(a, 0, len(a)-1)

et = time.process_time()

print(a)
print(et-st)


# In[ ]:


#**Explanation of Merge Sort**
 
1. **Merge Function (`merge`):**
   - Merges two sorted subarrays `A[p:q+1]` and `A[q+1:r+1]` into a single sorted array.
   - Uses temporary array `B` to store the merged elements.
   - Elements from the subarrays are compared, and the smaller one is appended to `B`.
   - Merged array is then copied back to `A[p:r+1]`.
 
2. **Merge Sort Function (`mergesort`):**
   - Recursively divides the array into halves until each subarray has one element.
   - Calls the `merge` function to merge sorted subarrays.
   - Works with indices `p` (start) and `r` (end).
 
3. **User Input (`a`):**
   - Takes a list of integers as input from the user.
 
4. **Print Sorted Array:**
   - The final sorted array is printed after applying Merge Sort.
 
The code efficiently sorts the input array using the Merge Sort algorithm.


# In[ ]:


#**Merge Sort Time Complexity Summary:**

- **Time Complexity:** \(O(n \log n)\)
- **Best Case:** \(O(n \log n)\)
- **Worst Case:** \(O(n \log n)\)
- **Average Case:** \(O(n \log n)\)

- **Characteristics:**
  - Efficient for large datasets.
  - Consistent performance.
  - Stable sort.

Merge Sort is a reliable and efficient sorting algorithm with a consistent \(O(n \log n)\) time complexity across different scenarios.


# In[ ]:


...............................................................................................................................
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\................................................................................................................................


# In[11]:


#SelectionSort#
def selectionSort(theSeq):
    n = len(theSeq)
    for i in range(n-1):
        smallNdx = i
        for j in range(i+1,n):
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j
        if smallNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp
    return theSeq
 
print(selectionSort([10,51,2,18,4,31]))


# In[ ]:


#code explanation of selection sort
The outer loop (for i in range(n-1)) iterates through each element in the array, except the last one.

The inner loop (for j in range(i+1, n)) finds the index of the smallest element in the unsorted part of the array.

If a smaller element is found, it updates the index (smallNdx).

After the inner loop, if the index of the smallest element is different from the current index (i), a swap is performed to move the smallest element to its correct position.

This process is repeated for each element, resulting in a sorted array.

Example Usage: print(selectionSort([10, 51, 2, 18, 4, 31])) sorts the array [10, 51, 2, 18, 4, 31].

Step-by-Step Execution:

Initial: [10, 51, 2, 18, 4, 31]
Iteration 1: [2, 51, 10, 18, 4, 31] (Swapped 10 with the smallest element 2)
Iteration 2: [2, 4, 10, 18, 51, 31] (Swapped 51 with the smallest element 4)
Iteration 3: [2, 4, 10, 18, 51, 31] (No swap, 51 is in the correct position)
Iteration 4: [2, 4, 10, 18, 31, 51] (Swapped 51 with the smallest element 31)
Sorted Array: [2, 4, 10, 18, 31, 51]






# In[ ]:


#**Selection Sort Time Complexity Summary:**

- **Best-Case:** O(n^2) (No advantage for pre-sorted arrays)
- **Average-Case:** O(n^2) (Consistent performance regardless of initial order)
- **Worst-Case:** O(n^2) (Occurs when the array is in reverse order)
- **Space Complexity:** O(1) (In-place algorithm, uses constant extra space)
- **Stability:** Not stable (Relative order of equal elements may change)
- **Comparison:** Less efficient for larger datasets compared to advanced sorting algorithms.


# In[ ]:


a concise summary of selection sort code:

- **Function Definition:**
 - `selectionSort(theSeq)`: Sorts the sequence using selection sort.

- **Initialization:**
 - `n = len(theSeq)`: Gets the length of the sequence.

- **Outer Loop:**
 - Iterates through the sequence up to the second-to-last element.

- **Minimum Index Initialization:**
 - Assumes the current index is the minimum.

- **Inner Loop (Finding Minimum):**
 - Iterates through the remaining unsorted elements, updating the minimum index if a smaller element is found.

- **Swap if Necessary:**
 - Swaps elements to move the minimum to its correct position if the assumed minimum index is different from the current index.

- **Return Sorted Sequence:**
 - Returns the sorted sequence.

- **Print Result:**
 - Calls `selectionSort` and prints the sorted sequence.

This algorithm efficiently sorts the input sequence in ascending order using the selection sort technique.


# In[ ]:


Certainly! Here are the arrays at each step of the selection sort algorithm:

1. `[10, 51, 2, 18, 4, 31]`
2. `[2, 51, 10, 18, 4, 31]`
3. `[2, 4, 10, 18, 51, 31]`
4. `[2, 4, 10, 18, 51, 31]`
5. `[2, 4, 10, 18, 31, 51]`

The final sorted array is `[2, 4, 10, 18, 31, 51]`.


# In[ ]:


...............................................................................................................................
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\................................................................................................................................


# In[2]:


#Heap Sort#
def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
 
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child
 
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child
 
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
 
def heapSort(arr):
    n = len(arr)
 
    # Build a max heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # Extract elements from the heap one by one.
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)
 
# Example usage:
arr = [23, 78, 45, 8, 32, 56]
heapSort(arr)
print("Sorted array:", arr)


# In[ ]:


#Heap
To find the number of times the MAX-HEAPIFY procedure is called in the BUILD-MAX-HEAP operation for the given array A = [1,2,3,4,5,6,7,8,9,10], we need to understand how BUILD-MAX-HEAP works.
 
BUILD-MAX-HEAP(A) is an operation that transforms an array A into a max-heap, which is a binary tree where the value of each node is greater than or equal to the values of its children. It does this by calling MAX-HEAPIFY on each non-leaf node of the heap in a bottom-up manner.
 
MAX-HEAPIFY(A, i) is a procedure that corrects a single violation of the max-heap property in a subtree rooted at index i. It assumes that the binary trees rooted at LEFT(i) and RIGHT(i) are max-heaps, but A[i] might be smaller than its children, violating the max-heap property. MAX-HEAPIFY corrects this violation by recursively fixing the affected subtree.
 
Now, let's analyze the number of times MAX-HEAPIFY is called in BUILD-MAX-HEAP(A).
 
```plaintext
BUILD-MAX-HEAP(A):
1.  heap-size[A] = length[A]   // Initialize the heap size
2.  for i = floor(length[A]/2) downto 1:   // Iterate through non-leaf nodes in reverse order
3.      MAX-HEAPIFY(A, i)   // Call MAX-HEAPIFY on each non-leaf node
```
 
For the given array A = [1,2,3,4,5,6,7,8,9,10], the length of the array is 10. Therefore, in the loop starting at line 2 of BUILD-MAX-HEAP, we iterate from i = floor(10/2) = 5 down to 1.
 
Here's the breakdown:
 
- For i = 5, MAX-HEAPIFY is called once.
- For i = 4, MAX-HEAPIFY is called once.
- For i = 3, MAX-HEAPIFY is called once.
- For i = 2, MAX-HEAPIFY is called once.
- For i = 1, MAX-HEAPIFY is called once.
 
So, the total number of times MAX-HEAPIFY is called in BUILD-MAX-HEAP(A) is 5.
 
In summary, the number of times MAX-HEAPIFY is called in BUILD-MAX-HEAP(A) for the given array A is 5.


# In[ ]:


#Running time analysis of max-heap
The running time analysis of building a max-heap involves considering the best-case and worst-case scenarios. Let's analyze the BUILD-MAX-HEAP operation in both cases:
 
### Best-case Scenario:
 
The best-case scenario occurs when the input array is already a valid max-heap. In such a case, no adjustments are needed, and the BUILD-MAX-HEAP operation simply iterates through the non-leaf nodes once. The time complexity of the MAX-HEAPIFY operation in this case is \(O(1)\) for each node, as no swaps or recursive calls are required.
 
1. **BUILD-MAX-HEAP Procedure:**
   - Iterating through the non-leaf nodes once: \(O(n/2)\)
   - Time complexity of MAX-HEAPIFY in best case: \(O(1)\)
   - Total time complexity: \(O(n/2) \times O(1) = O(n)\)
 
So, in the best-case scenario, the time complexity of building a max-heap is linear, \(O(n)\), where \(n\) is the number of elements in the heap.
 
### Worst-case Scenario:
 
The worst-case scenario occurs when the input array is in reverse order, and every element needs to be moved to the root of the heap. Each MAX-HEAPIFY operation takes \(O(\log n)\) time, and there are \(n/2\) non-leaf nodes to consider.
 
1. **BUILD-MAX-HEAP Procedure:**
   - Iterating through the non-leaf nodes once: \(O(n/2)\)
   - Time complexity of MAX-HEAPIFY in worst case: \(O(\log n)\)
   - Total time complexity: \(O(n/2) \times O(\log n) = O(n \log n)\)
 
In the worst-case scenario, the time complexity of building a max-heap is \(O(n \log n)\).
 
In summary, the best-case time complexity of BUILD-MAX-HEAP is \(O(n)\), while the worst-case time complexity is \(O(n \log n)\). The best case occurs when the input array is already a max-heap, and the worst case occurs when the input array is in reverse order.


# In[ ]:


#Build a max heap

[23, 78, 45, 8, 32, 56]  # Original array

[78, 32, 56, 8, 23, 45]  # Max heap after the first iteration

#Extract elements from the heap one by one

[78, 32, 56, 8, 23, 45]  # Max heap

[56,32,45,8,23,78]  # Swap the maximum element (78) with the last element and heapify

[45,32,23,8,56,78]  # Swap the maximum element (78) with the second-to-last element and heapify

[45, 32, 23, 8, 56, 78]  # Swap the maximum element (56) with the third-to-last element and heapify

[32,8,23,45,56,78]  # Swap the maximum element (78) with the fourth-to-last element and heapify

[23,8,32,45,56,78]  # Swap the maximum element (78) with the last element and heapify

[8,23,32,45,56,78]  # Swap the maximum element (56) with the second-to-last element and heapify

[8,23,32,45,56,78]  # Swap the maximum element (78) with the third-to-last element and heapify

[8, 23, 32, 45, 56, 78]  # Sorted array
 
#delete heap operation -> root gone ->take last one to replace
#Functions needed -> Insert ->Delete(swap)->Build Heap


# In[ ]:


#Min Heap
class MinHeap:

    def __init__(self):

        self.heap = []
 
    def heapify_up(self, index):

        while index > 0:

            parent_index = (index - 1) // 2

            if self.heap[index] < self.heap[parent_index]:

                # Swap the elements if the current element is smaller than its parent

                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]

                index = parent_index

            else:

                break
 
    def insert(self, value):

        self.heap.append(value)

        index = len(self.heap) - 1

        self.heapify_up(index)
 
    def heapify_down(self, index):

        while True:

            left_child_index = 2 * index + 1

            right_child_index = 2 * index + 2

            smallest = index
 
            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:

                smallest = left_child_index
 
            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:

                smallest = right_child_index
 
            if smallest != index:

                # Swap the elements if the smallest child is smaller than the current element

                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]

                index = smallest

            else:

                break
 
    def extract_min(self):

        if not self.heap:

            return None
 
        min_value = self.heap[0]

        last_value = self.heap.pop()
 
        if self.heap:

            self.heap[0] = last_value

            self.heapify_down(0)
 
        return min_value
 
# Example usage:

min_heap = MinHeap()

elements = [4, 10, 3, 5, 1]

for element in elements:

    min_heap.insert(element)
 
print("Min Heap:", min_heap.heap)

print("Extract Min:", min_heap.extract_min())

print("Min Heap after extraction:", min_heap.heap)


# In[ ]:


#**Min-Heap Operations Time Complexity:**

- **Insertion (Heapify Up):** \(O(\log n)\)
- **Deletion (Extract Min/Heapify Down):** \(O(\log n)\)
- **Peek (Get Min):** \(O(1)\)
- **Building a Heap (Heapify):** \(O(n)\)
- **Heap Sort:** \(O(n \log n)\)

**Best Case:** All operations in \(O(1)\) when the heap properties are well-maintained.

**Worst Case:** All operations in \(O(\log n)\) when heap properties are violated, requiring complete restructuring.

Min-heap operations efficiently maintain the minimum element in dynamic collections, suitable for various applications, including priority queues and sorting algorithms.


# In[ ]:


...............................................................................................................................
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\................................................................................................................................


# In[7]:


#Quick Sort from chatGPT
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
 
    def is_empty(self):
        return self.front is None
 
    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
 
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            item = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return item
 
    def first(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.front.data
 
def quickSort(S):
    if S.is_empty() or S.front.next is None:
        return S
 
    p = S.first()
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()
 
    while not S.is_empty():
        if S.first() < p:
            L.enqueue(S.dequeue())
        elif S.first() > p:
            G.enqueue(S.dequeue())
        else:
            E.enqueue(S.dequeue())
 
    quickSort(L)
    quickSort(G)
 
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())
 
    return S
 
# Example usage:
linked_queue = LinkedQueue()
for item in [24,31,17,85,63,50,96]:
    linked_queue.enqueue(item)
 
sorted_list = quickSort(linked_queue)
result = []
while not sorted_list.is_empty():
    result.append(sorted_list.dequeue())
 
print(result)


# In[ ]:



import sys
sys.setrecursionlimit(10000)
counter = 0 
def quicksort(A, p, r):
     
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

def partition(A, p, r):
    global counter
    x = A[r]
    i = p - 1
    for j in range(p, r):
        counter+=1
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i + 1] = A[i + 1], A[r]
    return i + 1

# Scenario 1: The partition function splits the input into an empty list and "all except the minimum."
"""input_sequence_scenario1 = [2, 5, 7, 9, 4, 1]

# Scenario 2: The partition function splits the input into "all except the maximum" and an empty list.
input_sequence_scenario2 = [3, 6, 8, 2, 4, 9]

# Scenario 3: The partition function splits the input into about two halves.
input_sequence_scenario3 = [1, 2, 6, 4, 5, 3]

# Function to test partition scenarios
def test_partition_scenario(input_sequence):
    print("Input Sequence:", input_sequence)

    # Copy the original sequence to avoid modifying it
    test_sequence = input_sequence.copy()

    # Call partition to test the scenario
    q = partition(test_sequence, 0, len(test_sequence) - 1)

    # Print the result of the partition
    print("Partitioned Sequence:", test_sequence[:q], test_sequence[q], test_sequence[q + 1:])
    print()

# Test each scenario
test_partition_scenario(input_sequence_scenario1)
test_partition_scenario(input_sequence_scenario2)
test_partition_scenario(input_sequence_scenario3)"""

# Get input sequence from the user and convert to list of integers
input_sequence = [int(num_str) for num_str in input("Enter numbers separated by space: ").split()]

# Sort the input sequence using quicksort
quicksort(input_sequence, 0, len(input_sequence) - 1)

# Print the sorted sequence
print("Sorted Sequence:", input_sequence)
print("Running Time",counter)


# In[ ]:


#code explanation of quicksort
The code uses QuickSort to sort a user-input sequence, counting the comparisons made during the process. Key points:

1. **Recursion Limit and Counter:**
   - Sets recursion limit to prevent overflow.
   - Initializes a global counter (`counter`) to track comparisons.

2. **Quicksort Function:**
   - Recursively sorts the array using `partition`.
   - Takes array `A`, start index `p`, and end index `r`.
   - Finds pivot `q` with `partition` and applies recursion if needed.

3. **Partition Function:**
   - Chooses the last element as the pivot.
   - Increments the comparison counter for each comparison.
   - Places pivot correctly and returns its index.

4. **User Input and Sorting:**
   - Takes user input for a sequence of numbers.
   - Applies QuickSort to the input.
   - Prints the sorted sequence and the comparison count.

**Running the Code:**
1. User inputs numbers.
2. QuickSort is applied recursively.
3. Prints the sorted sequence and comparison count.

The code is concise, tracking comparisons for QuickSort analysis with different input sequences.


# In[ ]:


#**QuickSort Time Complexity:**

- **Average Case:** \(O(n \log n)\)
- **Best Case:** \(O(n \log n)\)
- **Worst Case:** \(O(n^2)\)

**Key Characteristics:**
- QuickSort is efficient on average and in practice.
- The worst case is rare but can be mitigated with randomized or carefully chosen pivots.
- In-place, non-stable sorting algorithm.
- Performance influenced by the choice of the pivot element.

**Note:** Pivot choice and input data significantly impact actual performance. Consider randomized QuickSort or selecting a median-of-three pivot for improved practical behavior.


# In[ ]:


[24, 31, 17, 85, 63, 50, 96]
smaller than 85 [24, 31, 17, 63, 50], 85, larger than 85 [96]
smaller than 17 [], 17, larger than 17 [24, 31, 63, 50], [85, 96]
[17], smaller than 17 [24], 31, larger than 31 [63, 50], [85, 96]
[17, 24, 31], smaller than 50 [], 50, larger than 50 [63], [85, 96]
[17, 24, 31, 50, 63, 85, 96]


# In[ ]:


...............................................................................................................................
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\................................................................................................................................


# In[ ]:


table_size = 17    # Set table size here
hash_table = [[] for _ in range(table_size)]
 
def show_hash_table():
    print('-------------------')
    for i, chain in enumerate(hash_table):
        print(f"{i}: {chain}")
    print('-------------------')
 
def hash_func(s):
    hash_val = sum(ord(char) for char in s) % table_size
    return hash_val
 
def insert(s, v):
    hash_key = hash_func(s)
    chain = hash_table[hash_key]
    for pair in chain:
        if pair[0] == s:
            return -1  
    chain.append((s, v))  
    show_hash_table()
    return 0
 
def search(s):
    hash_key = hash_func(s)
    chain = hash_table[hash_key]
    for pair in chain:
        if pair[0] == s:
            return pair[1]
    return -1
 
def delete(s):
    hash_key = hash_func(s)
    chain = hash_table[hash_key]
   
    for pair in chain:
        if pair[0] == s:
            chain = [item for item in chain if item != pair]  # Create a new list without the item to delete
            hash_table[hash_key] = chain  # Update the hash_table with the new list
            show_hash_table()
            return 0
 
    return -1
 
 
operations = [
    ["insert", "I", 1],
    ["insert", "IV", 4],
    ["insert", "XXV", 25],
    ["search", "IV"],
    ["insert", "XVI", 16],
    ["insert", "IX", 9],
    ["search", "I"],
    ["insert", "LXIV", 64],
    ["search", "XVI"],
    ["insert", "LXXXI", 81],
    ["insert", "XXXVI", 36],
    ["search", "XXV"],
    ["insert", "XLIX", 49],
    ["delete", "IV"],
    ["search", "IV"],
    ["delete", "LXXXI"],
    ["search", "LXXXI"]
]
 
# The main program to execute the sequence of operations
for op in operations:
    if op[0] == "insert":
        result = insert(op[1], op[2])
    elif op[0] == "search":
        result = search(op[1])
    elif op[0] == "delete":
        result = delete(op[1])
    print(result)


# In[ ]:


#BST
import sys
sys.setrecursionlimit(10001)

root = None
        

class node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.p = None
        self.left = None
        self.right = None


def Inorder_Tree_Walk(x):
    if x != None:
        Inorder_Tree_Walk(x.left)
        print(x.key)
        Inorder_Tree_Walk(x.right)
def Preorder_Tree_Walk(x):
    if x !=None:
        print(x.key)
        Preorder_Tree_Walk(x.left)
        Preorder_Tree_Walk(x.right)
        
def Postorder_Tree_Walk(x):
    if x !=None:
       
        Postorder_Tree_Walk(x.left)
        Postorder_Tree_Walk(x.right)
        print(x.key)

def Tree_Minimum(x):
    # Replace "pass" with your code
    while x.left != None:
        x=x.left
    print(x.key)
    

def Tree_Maximum(x):
    # Replace "pass" with your code
    while x.right != None:
        x=x.right
    print(x.key)

def Tree_Successor(x):
    # Replace "pass" with your code
    if x.right != None:
        return Tree_Minimum(x.right)
    y= x.p
    while y != None and x==y.right:
        x=y
        y= y.p
    print(y.key)


    

'''
Adding your own Tree_Predecessor(x) is recommended, but not required
'''
def Tree_Predecessor(x):
    if x.left != None:
        return Tree_Maximum(x.left)
    y= x.p
    while y != None and x == y.left:
        x=y
        y=y.p
    return y
def Transplant(T,u, v):
    # This function is required for supporting Tree_Delete
    # Replace "pass" with your code
    
    
    if u.p == None:
        T.root = v
    elif  u== u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v != None:
        v.p = u.p


def Tree_Delete(T,z):
    # Replace "pass" with your code
    if z.left == None:
        Transplant(T,z,z.right)
    elif z.right == None:
        Transplant(T,z,z.left)
    else:
        y = Tree_Minimum(z.right)
        if y.p !=z:
            Transplant(T,y,y.right) 
            y.right = z.right
            y.right.p = y
        Transplant(T,z,y)
        y.left = z.left
        y.left.p = y
   
def Tree_Search(x,k):
   

    # Replace "pass" with your code
    if x== None or k==x.key:
        return x
    if k<x.key:
        return Tree_Search(x.left,k)
    else:
        return Tree_Search(x.right,k)

def Tree_Insert(T,z):
    

    # Replace "pass" with your code
    y = None
    x= T.root
    while x!= None:
        y=x
        if z.key<x.key:
            x=x.left
        else:
            x = x.right
    z.p = y
    if y==None:
        T.root = z
    elif z.key <y.key:
        y.left = z
    else:
        y.right = z
    

# Function to print
def printCall ( node , indent , last ) :
    if node != None :
        print(indent, end=' ')
        if last :
            print ("R----",end= ' ')
            indent += "     "
        else :
            print("L----",end=' ')
            indent += "|    "

        print ( str ( node.key ) )
        printCall ( node.left , indent , False )
        printCall ( node.right , indent , True )

# Function to call print
def print_BSTree (root) :
    printCall( root , "" , True )


node56 = node(56,"Data of 56")
node26 = node(26,"Data of 26")
node200 = node(200,"Data of 200")
node56.left = node26
node56.right = node200
 



node18 = node(18,"Data of 18")
node28 = node(28,"Data of 28")
node26.left = node18
node26.right = node28



node190 = node(190,"Data of 190")
node213 = node(213,"Data of 213")
node200.left = node190
node200.right = node213


       

node12 = node(12,"Data of 12")
node24 = node(24,"Data of 24")
node18.left = node12
node18.right = node24

node27 = node(27,"Data of 27")
node28.left = node27

print_BSTree (node56)
Inorder_Tree_Walk(node56)
print("--------------------------------")
Preorder_Tree_Walk(node56)
print("--------------------------------")
Postorder_Tree_Walk(node56)
print("--------------------------------")
Tree_Minimum(node56)
Tree_Maximum(node56)
Tree_Successor(node56)
Tree_Predecessor(node56)
Tree_Delete(node56,node28)
print("After Deleting:")
print_BSTree(node56)
new_node = node(30,"Data of 30")
Tree_Insert(node56,new_node)
print ("After Insertion: ")
print_BSTree(node56)



# In[ ]:


#BSTshwan
import sys
sys.setrecursionlimit(10001)
 
root = None
 
class node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.p = None
        self.left = None
        self.right = None
 
 
def Inorder_Tree_Walk(x):
    if x != None:
        Inorder_Tree_Walk(x.left)
        print(x.key)
        Inorder_Tree_Walk(x.right)
 
def Preorder_Tree_Walk(x):
    if x != None:
        print(x.key)
        Preorder_Tree_Walk(x.left)
        Preorder_Tree_Walk(x.right)
 
def Postorder_Tree_Walk(x):
    if x != None:
        Postorder_Tree_Walk(x.left)
        Postorder_Tree_Walk(x.right)
        print(x.key)
 
 
def Tree_Minimum(x):
    while x.left != None:
        x = x.left
    return x
 
def Tree_Maximum(x):
    while x.right != None:
        x = x.right
    return x
 
def Tree_Successor(x):
    if x.right != None:
        return Tree_Minimum(x.right)
    y = x.p
    while y != None and x == y.right:
        x = y
        y = y.p
    return y
 
'''
Adding your own Tree_Predecessor(x) is recommended, but not required
'''
 
def Transplant(u, v):
    global root
    if u.p == None:
        root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v != None:
        v.p = u.p

 
def Tree_Delete(z):
    if z.left == None:
        Transplant(z,z.right)
    elif z.right == None:
        Transplant(z,z.left)
    else:
        y = Tree_Minimum(z.right)
        if y.p != z:
            Transplant(y,y.right)
            y.right = z.right
            y.right.p = y
        Transplant(z,y)
        y.left = z.left
        y.left.p = y
 
def Tree_Search(k):
    global root
    x = root
    while x != None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x
 
def Tree_Insert(z):
    global root
    y = None
    x = root
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == None:
        root = z 
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
 
# Function to print
def printCall ( node , indent , last ) :
    if node != None :
        print(indent, end=' ')
        if last :
            print ("R----",end= ' ')
            indent += "     "
        else :
            print("L----",end=' ')
            indent += "|    "
 
        print ( str ( node.key ) )
        printCall ( node.left , indent , False )
        printCall ( node.right , indent , True )
 
# Function to call print
def print_BSTree(root) :
    printCall( root , "" , True )
 
 
#create a new node
#level3 = 2^4 - 1 = 15
#node56 no parent
 
node56 = node(56,'Data of 56')
node26 = node(26, 'Data of 26')
node200 = node(200, 'Data of 200')
node56.left = node26
node56.right = node200
root = node56
 
node18 = node(18, 'Data of 18')
node28 = node(28, 'Data of 28')
node26.left = node18
node26.right = node28
 
#node18
node12 = node(12, 'Data of 12')
node24 = node(24, 'Data of 24')
node18.left = node12
node18.right = node24
 
#node28 one child only
node27 = node(27, 'Data of 28')
node28.left = node27
 
#node200
node190 = node(190, 'Data of 190')
node213 = node(213, 'Data of 213')
node200.left = node190
node200.right = node213
 
#print_BSTree(node56)
 
"""print('Preorder')
Preorder_Tree_Walk(node56)
print('Inorder')
Inorder_Tree_Walk(node56)
print('Postorder')
Postorder_Tree_Walk(node56)"""
 
"""Tree_Minimum(node56)
Tree_Maximum(node56)
"""
 
print_BSTree(root)
print("-------------####-------------------")
print("Searching node 20: ", Tree_Search(20))
print("Searching node 400: ", Tree_Search(400))
node20 = node(20, 'Node20')
node400 = node(400, 'Node400')
Tree_Insert(node20)
Tree_Insert(node400)
print("After inserting node 20 & 400: ")
print_BSTree(root)
print("-------------####-------------------")
Tree_Delete(node20)
print("After deleting node 20:")
print_BSTree(root)
 
#This is the Binary Search Tree because
#All nodes in the left subtree have values less than the node's value.
#All nodes in the right subtree have values greater than the node's value.
#Both left and right subtrees are also binary search trees.


# In[ ]:


#BST Ahjarn
import sys
sys.setrecursionlimit(10001)

class BST_Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.p = None
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None

    def Tree_Maximum(self, x):
        while x.right != None:
            x = x.right
        return x

    def Tree_Minimum(self, x):
        while x.left != None:
            x = x.left
        return x

    def Transplant(self, u, v):
        if u.p == None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v != None:
            v.p = u.p

    def Tree_Delete(self, z):
        if z.left == None:
            self.Transplant(z, z.right)
        elif z.right == None:
            self.Transplant(z, z.left)
        else:
            y = self.Tree_Minimum(z.right)
            if y.p != z:
                self.Transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.Transplant(z, y)
            y.left = z.left
            y.left.p = y

    def Tree_Insert(self, z):
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def Tree_Successor(self, x):
        if x.right != None:
            return self.Tree_Minimum(x.right)
        y = x.p
        while y != None and x == y.right:
            x = y
            y = y.p
        return y

    def Tree_Predecessor(self, x):
        if x.left != None:
            return self.Tree_Maximum(x.left)
        y = x.p
        while y != None and x == y.left:
            x = y
            y = y.p
        return y

    def Tree_Search(self, k):
        x = self.root
        while x != None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def Inorder_Tree_Walk(self, x):
        if x != None:
            self.Inorder_Tree_Walk(x.left)
            print(x.key)
            self.Inorder_Tree_Walk(x.right)

    # Function to print
    def __printCall ( self , node , indent , last ) :
        if node != None :
            print(indent, end=' ')
            if last :
                print ("R----",end= ' ')
                indent += "     "
            else :
                print("L----",end=' ')
                indent += "|    "

            print ( str ( node.key ) )
            self.__printCall ( node.left , indent , False )
            self.__printCall ( node.right , indent , True )

    # Function to call print
    def print_BSTree ( self ) :
        self.__printCall ( self.root , "" , True )




        


# In[ ]:


#RBTree
# Define Node
class RB_Node():
    def __init__(self,key, data=None):
        self.data = data
        self.key = key                                   # Key of Node
        self.p = None                                    # Parent of Node
        self.left = None                                 # Left Child of Node
        self.right = None                                # Right Child of Node
        self.color = 1                                   # Red Node as new node is always inserted as Red Node

# Define R-B Tree
class RBTree():
    def __init__(self):
        self.NULL = RB_Node ( 0 )
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL


    # Insert New Key
    def insert(self, key):
        node = RB_Node(key)
        node.p = None
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1                                   # Set root colour as Red
        self.RB_Insert(node)

    # Insert New Node
    def RB_Insert(self, node):
        node.p = None
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1                                   # Set root colour as Red
        
        y = None
        x = self.root

        while x != self.NULL :                           # Find position for new node
            y = x
            if node.key < x.key :
                x = x.left
            else :
                x = x.right

        node.p = y                                       # Set p of Node as y
        if y == None :                                   # If parent i.e, is none then it is root node
            self.root = node
        elif node.key < y.key :                          # Check if it is right Node or Left Node by checking the value
            y.left = node
        else :
            y.right = node

        if node.p == None :                              # Root node is always Black
            node.color = 0
            return

        if node.p.p == None :                            # If parent of node is Root Node
            return

        self.fixInsert ( node )                          # Else call for Fix Up


    def Tree_Minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node

    def Tree_Maximum(self, node):
        while node.right != self.NULL:
            node = node.right
        return node

    # Code for left rotate
    def LR ( self , x ) :
        y = x.right                                      # Y = Right child of x
        x.right = y.left                                 # Change right child of x to left child of y
        if y.left != self.NULL :
            y.left.p = x

        y.p = x.p                                        # Change parent of y as parent of x
        if x.p == None :                                 # If parent of x == None ie. root node
            self.root = y                                # Set y as root
        elif x == x.p.left :
            x.p.left = y
        else :
            x.p.right = y
        y.left = x
        x.p = y


    # Code for right rotate
    def RR ( self , x ) :
        y = x.left                                       # Y = Left child of x
        x.left = y.right                                 # Change left child of x to right child of y
        if y.right != self.NULL :
            y.right.p = x

        y.p = x.p                                        # Change parent of y as parent of x
        if x.p == None :                                 # If x is root node
            self.root = y                                # Set y as root
        elif x == x.p.right :
            x.p.right = y
        else :
            x.p.left = y
        y.right = x
        x.p = y


    # Fix Up Insertion
    def fixInsert(self, k):
        while k.p.color == 1:                            # While parent is red
            if k.p == k.p.p.right:                       # if parent is right child of its parent
                u = k.p.p.left                           # Left child of grandparent
                if u.color == 1:                         # if color of left child of grandparent i.e, uncle node is red
                    u.color = 0                          # Set both children of grandparent node as black
                    k.p.color = 0
                    k.p.p.color = 1                      # Set grandparent node as Red
                    k = k.p.p                            # Repeat the algo with Parent node to check conflicts
                else:
                    if k == k.p.left:                    # If k is left child of it's parent
                        k = k.p
                        self.RR(k)                       # Call for right rotation
                    k.p.color = 0
                    k.p.p.color = 1
                    self.LR(k.p.p)
            else:                                         # if parent is left child of its parent
                u = k.p.p.right                           # Right child of grandparent
                if u.color == 1:                          # if color of right child of grandparent i.e, uncle node is red
                    u.color = 0                           # Set color of childs as black
                    k.p.color = 0
                    k.p.p.color = 1                       # set color of grandparent as Red
                    k = k.p.p                             # Repeat algo on grandparent to remove conflicts
                else:
                    if k == k.p.right:                    # if k is right child of its parent
                        k = k.p
                        self.LR(k)                        # Call left rotate on parent of k
                    k.p.color = 0
                    k.p.p.color = 1
                    self.RR(k.p.p)                        # Call right rotate on grandparent
            if k == self.root:                            # If k reaches root then break
                break
        self.root.color = 0                               # Set color of root as black


    # Function to fix issues after deletion
    def fixDelete ( self , x ) :
        while x != self.root and x.color == 0 :           # Repeat until x reaches nodes and color of x is black
            if x == x.p.left :                            # If x is left child of its parent
                s = x.p.right                             # Sibling of x
                if s.color == 1 :                         # if sibling is red
                    s.color = 0                           # Set its color to black
                    x.p.color = 1                         # Make its parent red
                    self.LR ( x.p )                       # Call for left rotate on parent of x
                    s = x.p.right
                # If both the child are black
                if s.left.color == 0 and s.right.color == 0 :
                    s.color = 1                           # Set color of s as red
                    x = x.p
                else :
                    if s.right.color == 0 :               # If right child of s is black
                        s.left.color = 0                  # set left child of s as black
                        s.color = 1                       # set color of s as red
                        self.RR ( s )                     # call right rotation on x
                        s = x.p.right

                    s.color = x.p.color
                    x.p.color = 0                         # Set parent of x as black
                    s.right.color = 0
                    self.LR ( x.p )                       # call left rotation on parent of x
                    x = self.root
            else :                                        # If x is right child of its parent
                s = x.p.left                              # Sibling of x
                if s.color == 1 :                         # if sibling is red
                    s.color = 0                           # Set its color to black
                    x.p.color = 1                         # Make its parent red
                    self.RR ( x.p )                       # Call for right rotate on parent of x
                    s = x.p.left

                if s.right.color == 0 and s.right.color == 0 :
                    s.color = 1
                    x = x.p
                else :
                    if s.left.color == 0 :                # If left child of s is black
                        s.right.color = 0                 # set right child of s as black
                        s.color = 1
                        self.LR ( s )                     # call left rotation on x
                        s = x.p.left

                    s.color = x.p.color
                    x.p.color = 0
                    s.left.color = 0
                    self.RR ( x.p )
                    x = self.root
        x.color = 0


    # Function to transplant nodes
    def __rb_transplant ( self , u , v ) :
        if u.p == None :
            self.root = v
        elif u == u.p.left :
            u.p.left = v
        else :
            u.p.right = v
        v.p = u.p

    # Function to return node containing the given key
    def Tree_Search( self, k):
        x = self.root
        while x != self.NULL and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    # Function to return succesor of x
    def Tree_Successor(self, x):
        if x.right != self.NULL:
            return self.Tree_Minimum(x.right)
        y = x.p
        while y != self.NULL and x == y.right:
            x = y
            y = y.p
        return y

    # Function to return succesor of x
    def Tree_Predecessor(self, x):
        if x.left != self.NULL:
            return self.Tree_Maximum(x.left)
        y = x.p
        while y != self.NULL and x == y.left:
            x = y
            y = y.p
        return y

    # Function to handle deletion
    def delete_node_helper ( self , node , key ) :
        z = self.NULL
        while node != self.NULL :                          # Search for the node having that value/ key and store it in 'z'
            if node.key == key :
                z = node

            if node.key <= key :
                node = node.right
            else :
                node = node.left

        if z == self.NULL :                                # If Kwy is not present then deletion not possible so return
            print ( "Value not present in Tree !!" )
            return
        else:
            self.RB_Delete(z)

    def RB_Delete( self, z ):
        y = z
        y_original_color = y.color                          # Store the color of z- node
        if z.left == self.NULL :                            # If left child of z is NULL
            x = z.right                                     # Assign right child of z to x
            self.__rb_transplant ( z , z.right )            # Transplant Node to be deleted with x
        elif (z.right == self.NULL) :                       # If right child of z is NULL
            x = z.left                                      # Assign left child of z to x
            self.__rb_transplant ( z , z.left )             # Transplant Node to be deleted with x
        else :                                              # If z has both the child nodes
            y = self.Tree_Minimum ( z.right )                    # Find minimum of the right sub tree
            y_original_color = y.color                      # Store color of y
            x = y.right
            if y.p == z :                              # If y is child of z
                x.p = y                                # Set parent of x as y
            else :
                self.__rb_transplant ( y , y.right )
                y.right = z.right
                y.right.p = y

            self.__rb_transplant ( z , y )
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == 0 :                          # If color is black then fixing is needed
            self.fixDelete ( x )


    # Deletion of node
    def delete ( self , key ) :
        self.delete_node_helper ( self.root , key )         # Call for deletion


    # Function to print
    def __printCall ( self , node , indent , last ) :
        if node != self.NULL :
            print(indent, end=' ')
            if last :
                print ("R----",end= ' ')
                indent += "     "
            else :
                print("L----",end=' ')
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print ( str ( node.key ) + "(" + s_color + ")" )
            self.__printCall ( node.left , indent , False )
            self.__printCall ( node.right , indent , True )

    # Function to call print
    def print_RBTree ( self ) :
        self.__printCall ( self.root , "" , True )






# In[ ]:


#Advantages and Disadvantages 
**Insertion Sort:**
- **Advantages:**
  - Simple and easy to implement.
  - Efficient for small datasets.
  - Adaptive, performs well on partially sorted data.

- **Disadvantages:**
  - Inefficient for large datasets.
  - Quadratic time complexity (\(O(n^2)\)) in the worst case.

**Merge Sort:**
- **Advantages:**
  - Stable sort, preserves equal element order.
  - Efficient for large datasets.
  - Consistent performance, \(O(n \log n)\) time complexity.

- **Disadvantages:**
  - Additional memory space required for merging.
  - Slower constant factors compared to other algorithms.

**Selection Sort:**
- **Advantages:**
  - Simple and easy to implement.
  - In-place sorting algorithm.

- **Disadvantages:**
  - Quadratic time complexity (\(O(n^2)\)).
  - Not adaptive, inefficient for partially sorted data.

**Heap Sort:**
- **Advantages:**
  - In-place sorting.
  - Efficient for large datasets.
  - Guaranteed \(O(n \log n)\) time complexity.

- **Disadvantages:**
  - Not stable, may change equal element order.
  - Slower in practice compared to QuickSort for small datasets.

**Quick Sort:**
- **Advantages:**
  - Efficient for large datasets, average-case \(O(n \log n)\).
  - In-place sorting.
  - Adaptive and suitable for parallel processing.

- **Disadvantages:**
  - Worst-case time complexity (\(O(n^2)\)) for certain pivot choices.
  - Not stable, may change equal element order.

**Hash Table:**
- **Advantages:**
  - Fast data retrieval (average \(O(1)\) time complexity).
  - Efficient for search, insert, and delete operations.

- **Disadvantages:**
  - Limited range of hash functions.
  - Potential collisions, impacting performance.

**Binary Search Tree:**
- **Advantages:**
  - Efficient for searching operations (\(O(\log n)\)).
  - Easy to implement.

- **Disadvantages:**
  - May become unbalanced, leading to \(O(n)\) time complexity in the worst case.
  - Not suitable for large datasets with repeated elements.

**Red-Black Tree:**
- **Advantages:**
  - Balanced, ensuring \(O(\log n)\) time complexity.
  - Suitable for large datasets with efficient search, insert, and delete operations.

- **Disadvantages:**
  - More complex to implement compared to a Binary Search Tree.
  - Slightly higher overhead due to maintaining balance.

