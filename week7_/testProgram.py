# name - Thant Si Thu Naing
# ID - 611720
# section - 541
import time

from BinarySearchTree import *
import random

from week7_.RedBlackTree import RBTree

# Q1
'''
bst = BSTree()
a = [4, 5, 12, -5, -87, 9, 1026, 2]
random.shuffle(a)
for i in a:
    x = BST_Node(i)
    bst.Tree_Insert(x)
print(" Binary Search Tree : ",)
bst.print_BSTree()
print("Minimum: ", bst.Tree_Minimum(bst.root).key)
print("Maximum: ", bst.Tree_Maximum(bst.root).key)
print("Successor of root: ", bst.Tree_Successor(bst.root).key)
print("Predecessor of root: ", bst.Tree_Predecessor(bst.root).key)
x = bst.Tree_Search(4)
print("Search 4: ", x.key)
print("In-order traversal of tree: ")
bst.Inorder_Tree_Walk(bst.root)
print("Tree after deletion:")
bst.print_BSTree()
print("____________________________________________________________________________________________________")
print()


# Q2

list_random = []
bst = BSTree()
for i in range(16):
    list_random.append(int(random.random()*100))
random.shuffle(list_random)
for i in list_random:
    x = BST_Node(i)
    bst.Tree_Insert(x)
print("random list =", list_random)
print("Binary Search Tree For Question2 : ",)
bst.print_BSTree()
print("____________________________________________________________________________________________________")
print()

#Q3
bst3 = BSTree()
n = int(input("Enter the number :"))
for i in range(n):
    x=BST_Node(i)
    bst3.Tree_Insert(x)
bst3.print_BSTree()
print("____________________________________________________________________________________________________")
print()

#Q4
bst4 = BSTree()
counter = 0
n = int(input())
k = 2*n
for i in range(n):
    x = BST_Node(i)
    bst4.Tree_Insert(x)
st = time.process_time()
for i in range(n):
    v = random.randint(0, k)
    x = bst4.Tree_Search(v)
    if x != None:
        counter += 1
et = time.process_time()
print("counter: ", counter)
print("time: ", et-st)

#Q5
The upperbound on the running time of each search is O(n).

#Q6
rbt = RBTree()
a = [12,5,3,11,15,7,10,13,14,6,4,17,8]
random.shuffle(a)
for k in a:
    rbt.insert(k)
print("Tree:")
rbt.print_RBTree()
print("Minimum:", rbt.Tree_Minimum(rbt.root).key)
print("Maximum:", rbt.Tree_Maximum(rbt.root).key)
print("Successor of root:", rbt.Tree_Successor(rbt.root).key)
print("Predecessor of root:", rbt.Tree_Predecessor(rbt.root).key)
x = rbt.Tree_Search(7)
print("Search 7:", x.key)
rbt.delete(7)
print("Tree after deletion:")
rbt.print_RBTree()

#Q7
rbt1 = RBTree()
counter = 0
n = int(input())
k = 2*n
for i in range(n):
    rbt1.insert(i)
rbt1.print_RBTree()
'''

# Q8
rbt2 = RBTree()
counter = 0
n = int(input())
k = 2 * n
for i in range(n):
    rbt2.insert(i)
st = time.process_time()
for i in range(n):
    v = random.randint(0, k)
    x = rbt2.Tree_Search(v)
    if x != rbt2.NULL:
        counter += 1
et = time.process_time()
print("counter: ", counter)
print("time: ", et - st)