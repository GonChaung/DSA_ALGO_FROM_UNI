#name - Thant Si Thu Naing
#ID - 611720
#section - 541
from BinarySearchTree import *
import random

#Q1
bst = BSTree()
a = [4, 5, 12, -5, -87, 9, 1026,2]
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
print("____________")
print()