"""All trees are graphs. Binary trees are a specific type of trees where the nodes on the right are always larger
than the nodes on the left. Binary SEARCH trees on the other hand, follow the same rule, but it has to be correct for
all parent nodes as well. Meaning - no child node of the left parent node can be greater than the right parent node. """

root = "The upper node of the tree, that has no parents (nodes above)"
leaf = "Any node of the tree which has no children"

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

IN ORDER, PRE ORDER AND POS ORDER TRANSVERSAL

In-order traversal means to "visit" (often, print) the left branch, then the current node, and finally, the right
branch.
1 void inOrderTraversal(TreeNode node) {
2 if (node!= null) {
3 inOrderTraversal(node.left);
4 visit(node);
5 inOrderTraversal(node.right);
6 }
7 }
When performed on a binary search tree, it visits the nodes in ascending order (hence the name "in-order").

Pre-Order Traversal
Pre-order traversal visits the current node before its child nodes (hence the name "pre-order").
1 void preOrderTraversal(TreeNode node) {
2 if (node!= null) {
3 visit(node);
4 preOrderTraversal(node.left);
5 preOrderTraversal(node.right);
6 }
7 }
In a pre-order traversal, the root is always the first node visited.

Post-Order Traversal
Post-order traversal visits the current node after its child nodes (hence the name "post order").
1 void postOrderTraversal(TreeNode node) {
2 if (node!= null) {
3 postOrderTraversal(node.left);
4 postOrderTraversal(node.right);
5 visit(node);
6 }
7 }
In a post-order traversal, the root is always the last node visited.

TRIES
A trie is a variant of an n-ary tree in which characters are stored at each node. Each path down the tree may
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
