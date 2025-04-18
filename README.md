# Binary-search-Tree

# Overview

This project implements various operations on binary trees, including:

1. Constructing a binary tree from a BFS (level-order) representation.

2. Performing in-order traversal (both recursive and iterative).

3. Generating different types of binary trees for analysis:

   1. Random permutation of unique numbers.
  
   2. Complete binary trees.
  
   3. Skewed binary trees (left or right heavy).

4. Comparing time and space complexity of recursive and iterative in-order traversal.

5. Validating if a binary tree is a Binary Search Tree (BST).

6. Printing the tree structure in a readable format (both ASCII and graphical representation).

# Installation and Requirements

<ins> Prerequisites </ins>

1. Python 3.6+

2. matplotlib

3. networkx

# Usage 

<ins> Constructing a Binary Tree </ins>

      homework3 = HomeWork3()
      input_str = "1,2,3,None,None,4"
      root = homework3.constructBinaryTree(input-str)

<ins> In-Order Traversal (Recursive & Iterative)</ins>

      recursive_output = homework3.inOrderTraversalRecursive(root)
      iterative_output = homework3.inOrderTraversalIterative(root)

<ins> Generating Trees for Complexity Analysis</ins>

      random_nums = homework3.generate_random_permutation(10)
      complete_tree = homework3.generate_complete_tree(random_nums)
      skewed_tree = homework3.generate_skewed_tree(random_nums, skew = 'left')

<ins> Validating BST </ins>

      is_bst = homework3.validateBST(root)
      print("Is the tree a valid BST?", is_bst)

<ins> Printing Tree Structure </ins>

For ASCII Format (for terminal output)

      print_tree_ascii(root)

Graphical Representation (using matplotlib & networkx)

      visualize_tree_hierarchical(root)

# Performance Analysis

The project compares the time and space complexity of in-order traversal (recursive vs iterative) on both complete and skewed binary trees.

<ins>Performance Testing</ins>

       sizes = [10, 100, 1000, 5000]
       trials = 100
       for N in sizes:
           nums = homework3.generate_random_permutation(N)
           complete_tree = homework3.generate_complete_tree(nums)
           skewed_tree = homework3.generate_skewed_tree(nums)

           analyze_performance(complete_tree, skewed_tree)

# Handling Common Issues</ins>

<ins> Encoding Error</ins>

The 'charmap' can't encode character. If we encounter this error while printing tree structures try :

1. Forcing UTF-8 encoding in Python:

         import sys
         sys.stdout.reconfigure(encoding='utf-8')

2. Using ASCII-only tree characters instead:

         print_tree_ascii(root, use_unicode=False)

<ins> Large Input Causing RecursionError</ins>

For large skewed trees, recursion may hit Python's depth limit. To avoid this :

1. Use the iterative traversal method instead.

2. Increase the recursion limit(use with coutin though):

          import sys
          sys.setrecursionlimit(10000)
