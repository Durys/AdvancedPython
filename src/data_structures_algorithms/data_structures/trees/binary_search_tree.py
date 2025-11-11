"""
Binary SEARCH trees are a specific type of trees where the nodes
on the right are always larger than the nodes on the left,
and it has to be correct for all parent nodes as well.
Meaning - no child node of the left parent node
can be greater than the right parent node.
"""

""" A binary tree - NOT a binary search tree
      __6__
     /      \
    4       8
   / \     / \
  3   8   7  22

Why - the leaf node 8 is larger than the main root node (6).

A Binary SEARCH tree
      __6__
     /      \
    4       8
   / \     / \
  3   5   7  22
"""