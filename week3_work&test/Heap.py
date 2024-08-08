'''
Python 3
A explicit comparing function is required for custom priority definition
The compare function takes two items:
  - returns True if the first item has higher priority than the second
  - returns False otherwise
The function is to be passed to the heap instantiation
'''

class heap:
    def compare(x, y):  # a default compare function for min heap
        return x < y

    def empty(self):
        if self.heapsize == 0:
            return True
        else:
            return False

    def heapify(self, i):
        l = i*2+1
        r = (i+1)*2
        if l < self.heapsize and self.cmp(self.a[l],self.a[i]):
            largest = l
        else:
            largest = i
        if r < self.heapsize and self.cmp(self.a[r],self.a[largest]):
            largest = r
        if largest != i:
            self.a[i],self.a[largest] = self.a[largest],self.a[i]
            self.heapify(largest)

    def insert(self, x):
        self.heapsize += 1
        if len(self.a) < self.heapsize:
            self.a.append(x)
        else:
            self.a[self.heapsize-1] = x
        i = self.heapsize-1
        j = (i-1)//2
        while i > 0 and self.cmp(self.a[i],self.a[j]):
            self.a[i],self.a[j] = self.a[j],self.a[i]
            i = j
            j = (i-1)//2

    def extract(self):
        x = self.a[0]
        last = self.heapsize-1
        self.a[0],self.a[last] = self.a[last],self.a[0]
        self.heapsize -= 1
        self.heapify(0)
        return x

    def buildHeap(self):
        for i in range((self.heapsize-1)//2, -1, -1):
            self.heapify(i)

    def __init__(self, items=[], cmp=compare):
        self.a = items
        self.cmp = cmp
        self.heapsize = len(self.a)
        if len(self.a) > 0:
            self.buildHeap()

'''
# Example class definition for heap's element and test code

def myCompare(x, y):   # max heap
    return x.key > y.key

class myClass:
    def __init__(self, k):
        self.key = k


testList = [i+100 for i in range(10)]

pq1 = heap(items=testList)   # default as min heap for a list of numbers
pq2 = heap(cmp=myCompare)  # custom class item with custom compare function

for v in testList:
    pq2.insert(myClass(v))

while not pq1.empty():
    print(pq1.extract(), end=' ')
print()

while not pq2.empty():
    print(pq2.extract().key, end=' ')

'''
'''
                        17
                        /\
                       15 10
                       /\   /
                      6  10 7
   Given a Max-heap tree in following diagram, complete the representation of this tree by the ocntent of an array. Explain stey by step and show the content of the array during performing heapify() while apply heapsort to the given Max-heap.
   Element ->
   Index   -> 0 1 2 3 4 5
'''
'''

heapify() 

1. Start by comparing the values of the root node (at index 0) and its
left child node (at index 1). If the value of the root node is greater
than or equal to the value of its left child, stop. Otherwise, swap their
positions in the array and continue with the next step.
2. Compare the values of the root node and its right child node (at index
2). If the value of the root node is greater than or equal to the value of
its right child, stop. Otherwise, swap their positions in the array and
continue with the next step.
3. If both children are larger than the root node, we need to perform a
more extensive search to find the largest element among all three nodes.
Compare the values of the left child's right child (at index 3) and the
right child's left child (at index 4). If either of these values is
greater than or equal to the value of the root node, stop. Otherwise, swap
their positions in the array and continue with the next step.
4. Repeat steps 1-3 for each level of the tree, starting from the root
node and working downward to the bottom level.
5. Once we have reached the bottom level, we are done! The entire tree has
been sorted in ascending order using heapsort.

Max-heap tree:
```
[17, 15, 10, 6, 10, 7]

Step 1: Compare the values of the root node (at index 0) and its left
child node (at index 1). They are both greater than or equal to each
other, so we don't need to swap anything.
Step 2: Compare the values of the root node and its right child node (at
index 2). The value of the root node is greater than the value of its
right child, so we don't need to swap anything.
Step 3: Since both children are larger than the root node, we need to
perform a more extensive search. Compare the values of the left child's
right child (at index 3) and the right child's left child (at index 4).
The value of the left child's right child is greater than or equal to the
value of the root node, so we don't need to swap anything.
Step 4: We have reached the bottom level of the tree, so we are done! The
entire tree has been sorted in ascending order using heapsort.
```
In this example, the sorted array would look like this:
```
[6, 7, 10, 15, 17]
```
'''