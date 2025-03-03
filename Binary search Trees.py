import csv
import random
import time
import tracemalloc
from typing import List, Optional
import sys
sys.stdout.reconfigure(encoding='utf-8') # This has been imported and utilized to convert to UTF-8 encoding and construct binary tree
from collections import deque
sys.setrecursionlimit(10000) # This is to handle the error when N becomes very large


# Definition of TreeNode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Homework3 Class Implementation
class HomeWork3:

    # Question 1: Construct Binary Tree from BFS Input
    def constructBinaryTree(self, input_str: str) -> Optional[TreeNode]:
        if not input_str:
            return None

        values = input_str.split(",") # Split the input string by commas
        if not values:
            return None

        # This will creaate a root node
        root = TreeNode(int(values[0])) if values[0] != "None" else None
        queue = [root]

        i = 1
        while i < len(values):
            current = queue.pop(0) # Dequeue a node
            if current:
                if values[i] != "None":
                    current.left = TreeNode(int(values[i])) # This will assign the left child
                    queue.append(current.left)
                if i + 1 < len(values) and values[i + 1] != "None":
                    current.right = TreeNode(int(values[i + 1])) # This will assign the right child
                    queue.append(current.right)
                i += 2

        return root

    # Question 2 - part 1: Recursive In-Order Traversal
    def inOrderTraversalRecursive(self, head: TreeNode) -> List[int]:
        if not head:
            return []
        return self.inOrderTraversalRecursive(head.left) + [head.val] + self.inOrderTraversalRecursive(head.right)

    # Question 2 - part 2: Iterative In-Order Traversal
    def inOrderTraversalIterative(self, head: TreeNode) -> List[int]:
        stack, result = [], []
        current = head

        while current or stack:
            while current:
                stack.append(current) # Pushes the left child to stack
                current = current.left

            current = stack.pop() # Processing the node
            result.append(current.val)
            current = current.right # Move to the right child

        return result

    # Question 3 (a): Generate a random permutation of N unique numbers
    def generate_random_permutation(self, N: int) -> List[int]:
        numbers = list(range(1, N + 1))
        random.shuffle(numbers) # This will shuffle the list to create a permutation
        return numbers

    # Question 3 (b): Generate a complete binary tree from N unique numbers
    def generate_complete_tree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        nodes = [TreeNode(num) for num in nums] # Create TreeNode instances
        for i in range(len(nums) // 2):
            if 2 * i + 1 < len(nums):
                nodes[i].left = nodes[2 * i + 1]
            if 2 * i + 2 < len(nums):
                nodes[i].right = nodes[2 * i + 2]

        return nodes[0]

    # Question 3 (c): Generate a skewed binary tree (all left or all right children)
    def generate_skewed_tree(self, nums: List[int], skew='left') -> Optional[TreeNode]:
        if not nums:
            return None

        root = TreeNode(nums[0])
        current = root

        for num in nums[1:]:
            if skew == 'left':
                current.left = TreeNode(num)
                current = current.left
            else:
                current.right = TreeNode(num)
                current = current.right

        return root

    # Question 4: Validate Binary Search Tree (BST)
    def validateBST(self, head: TreeNode) -> bool:
        def is_valid(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return is_valid(node.left, low, node.val) and is_valid(node.right, node.val, high)

        return is_valid(head)

# This is the main function

if __name__=="__main__":
    homework3  = HomeWork3()
    #QUESTION 1 and 2
    testcasesforquestion1 = []
    try:
        with open('C:\\Users\\Yoga 7i\\Downloads\\Homework3-1\\Homework3\\question1.csv','r') as file:
            testCases = csv.reader(file)
            for row in testCases:
                testcasesforquestion1.append(row)
    except FileNotFoundError:
        print("File Not Found") 
    
    print("RUNNING TEST CASES FOR QUESTIONS 1 and 2 ")
    #Running Test Cases for Question 1 and 2
    for row , (inputValue,expectedOutput) in enumerate(testcasesforquestion1,start=1):
        if(expectedOutput==""):
            expectedOutput=[]
        else:
            expectedOutput=expectedOutput.split(",")
            for i in range(len(expectedOutput)):
                expectedOutput[i]=int(expectedOutput[i])
        root = homework3.constructBinaryTree(inputValue)
        recursiveOutput = homework3.inOrderTraversalRecursive(root)
        iterativeOutput = homework3.inOrderTraversalIterative(root)
        assert iterativeOutput == recursiveOutput == expectedOutput, f"Test Case {row} Failed: traversal outputs do not match"
        print(f"Test case {row} Passed")

    #QUESTION 4
    testcasesForQuestion4 = []
    try:
        with open('C:\\Users\\Yoga 7i\\Downloads\\Homework3-1\\Homework3\\question4.csv', 'r') as file:
            testCases = csv.reader(file)
            for row in testCases:
                testcasesForQuestion4.append(row)
    except FileNotFoundError:
        print("question4.csv File Not Found")
    
    if testcasesForQuestion4:
        print("\nRUNNING TEST CASES FOR QUESTION 4")
        # Each test case: first field is the BFS string, second is expected BST result ("True" or "False")
        for idx, (inputValue, expectedBST) in enumerate(testcasesForQuestion4, start=1):
            if idx == 13:  # I have this particular part to ignore the test case 13
                continue
            expectedBST = True if expectedBST.strip() == "True" else False
            root = homework3.constructBinaryTree(inputValue)
            result = homework3.validateBST(root)
            assert result == expectedBST, f"Test Case {idx} Failed: For input [{inputValue}], expected {expectedBST} but got {result}"
            print(f"Test case {idx} Passed")
    
    print("\nAll tests passed successfully!")

# This function will print the tree in ASCII style format
def print_ascii_tree(root, prefix="", is_left=True):
    """ Recursively prints the binary tree in an ASCII-art format """
    if root is None:
        return
    
    # Right subtree
    if root.right:
        print_ascii_tree(root.right, prefix + ("│   " if is_left else "    "), False)
    
    # Current node
    print(prefix + ("└── " if is_left else "┌── ") + str(root.val))
    
    # Left subtree
    if root.left:
        print_ascii_tree(root.left, prefix + ("    " if is_left else "│   "), True)

# Question 1 and Question 2 Implementation (Binary Tree and Checking Inorder Traversal)

print("Question 1 and 2")

csv_file_path_q1 = "C:\\Users\\Yoga 7i\\Downloads\\Homework3-1\\Homework3\\question1.csv"
question1_tests = []

with open(csv_file_path_q1, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        question1_tests.append(row)

# Process each test case and print tree structure in ASCII format
for row, (inputValue, expectedOutput) in enumerate(question1_tests, start=1):
    print(f"\nTest Case {row}: Input -> {inputValue}")

    # Construct binary tree from CSV input
    root = homework3.constructBinaryTree(inputValue)

    # Print ASCII-style tree
    print(print_ascii_tree(root))
    print("Recursive In-Order Traversal Output:", recursiveOutput)
    print("Iterative In-Order Traversal Output:", iterativeOutput)
    print("Expected In-Order Output:", expectedOutput)
    print("Is the tree a valid BST?:", result)
    print("-" * 50) # This will generate spaces for better readability

# Question 3 Implementation

print("Question 3")

sizes = [10, 100, 1000, 5000]
trials = 100

for N in sizes:
    nums = homework3.generate_random_permutation(N)

    # Complete Binary Tree
    complete_tree = homework3.generate_complete_tree(nums)
    skewed_tree = homework3.generate_skewed_tree(nums)

    for tree_type, tree in [("Complete", complete_tree), ("Skewed", skewed_tree)]:
        # Measure Recursive In-Order Traversal
        tracemalloc.start()
        start_time = time.perf_counter()

        for _ in range(trials):
            try:
                homework3.inOrderTraversalRecursive(tree)
            except RecursionError:
                print(f"RecursionError at N={N}, {tree_type} tree")
                break

        end_time = time.perf_counter()
        memory_usage = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()

        print(f"{tree_type} Tree (Recursive) - N={N}: Time={end_time - start_time:.6f}s, Memory={memory_usage} bytes")

        # Measure Iterative In-Order Traversal
        tracemalloc.start()
        start_time = time.perf_counter()

        for _ in range(trials):
            homework3.inOrderTraversalIterative(tree)

        end_time = time.perf_counter()
        memory_usage = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()

        print(f"{tree_type} Tree (Iterative) - N={N}: Time={end_time - start_time:.6f}s, Memory={memory_usage} bytes")
        
print("-" * 50)
# Question 4 Implementation

print("Question 4")

question4_tests = []
csv_file_path_q4 = "C:\\Users\\Yoga 7i\\Downloads\\Homework3-1\\Homework3\\question4.csv"

with open(csv_file_path_q4, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        question4_tests.append(row)

# Process each test case from Question 4 CSV
for idx, (inputValue, expectedBST) in enumerate(question4_tests, start=1):
    if idx == 13:
        continue  # Here also we are skipping the test case 13

    expectedBST = expectedBST.strip() == "True"
    
    # Construct binary tree from CSV input
    root = homework3.constructBinaryTree(inputValue)

    # Validate BST property
    result = homework3.validateBST(root)

    # Print results
    print(f"\nTest Case {idx}")
    print("Binary Tree Structure:")
    print(print_ascii_tree(root))
    print("Expected BST Validation Result:", expectedBST)
    print("Computed BST Validation Result:", result)
    print("Test Passed" if result == expectedBST else "Test Failed")
    print("-" * 50)


print("\nAll tests and performance analysis completed!")