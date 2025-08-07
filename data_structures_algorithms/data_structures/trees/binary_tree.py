"""All trees are graphs. Binary trees are a specific type of trees where the nodes on the right are always larger
than the nodes on the left."""

root = "The upper node of the tree, that has no parents (nodes above)"
leaf = "Any node of the tree which has no children"


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


""" A binary tree - NOT a binary search tree
      __6__
     /      \
    4       8
   / \     / \
  3   8   7  22

Why - the leaf node 8 is larger than the root node.

A Binary SEARCH tree
      __6__
     /      \
    4       8
   / \     / \
  3   5   7  22
"""

# IN ORDER, PRE ORDER AND POS ORDER TRANSVERSAL

# In-Order Traversal
# In-order traversal means to "visit" the left branch, then the current node, and finally, the right branch.


def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print(node)
        in_order_traversal(node.right)


# When performed on a binary search tree, it visits the nodes in ascending order (hence the name "in-order").


# Pre-Order Traversal
# Pre-order traversal visits the current node before its child nodes (hence the name "pre-order").


def pre_order_tranversal(node):
    if node is not None:
        print(node)
        pre_order_tranversal(node.left)
        pre_order_tranversal(node.right)


# In a pre-order traversal, the root is always the first node visited.


# Post-Order Traversal
# Post-order traversal visits the current node after its child nodes (hence the name "post order").


def post_order_tranversal(node):
    if node is not None:
        post_order_tranversal(node.left)
        post_order_tranversal(node.right)
        print(node)

# In a post-order traversal, the root is always the last node visited.


# TRIES
"""A trie is a variant of an n-ary tree in which characters are stored at each node. Each path down the tree may
represent a word. The * nodes are used to indicate complete words. 

      __M__
     /     \
    A       L
   / \       \
  N   P       I
 /    |        \
Y     *         E 
|               |
*               *
"""


if __name__ == "__main__":
    ll = Node(4)
    l = Node(2, left=ll)
    r = Node(3)
    root = Node(1, left=l, right=r)

    print("In Order Traversal")
    in_order_traversal(root)
    print("\n")
    print("Pre Order Traversal")
    pre_order_tranversal(root)
    print("\n")
    print("Post Order Traversal")
    post_order_tranversal(root)
