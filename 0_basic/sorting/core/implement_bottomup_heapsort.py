
def heapify(arr, n, i):
    """
    This function ensures the heap property for the subtree rooted at index i.
    It's also known as "sift-down"

    Parameters:
    arr (list): The list (heap)
    n (int): The size of the heap (can be smaller than len(arr) during sorting)
    i (int): The index of the root node of the subtree to heapify
    
    Root is at index 0.
    Left child of node i -> 2*i + 1.
    Right child of node i -> 2*i + 2.
    Parent of node i -> (i-1)/2.
    Last non-leaf node -> parent of last node -> (n/2) - 1
    the division is integer division.
    
    why ? because heap is a complete binary tree. 
    All levels are completely filled, except possibly the last level.
    Nodes in the last level are filled from left to right
    last element is guranteed to be a leaf node.
    parent of the last element is the last non-leaf node.
    apply parent index formula on last element index (n-1) 
    we get (n-2)/2 = (n/2) - 1

    Find the largest among root, left child, and right child
    in case left or right child is larger than root (current subtree root we are checking is not the largest)
    swap current root with the largest child in array
    recurse on the child subtree at index "largest"
    """
    largest = i       # Initialize largest as root
    left = 2 * i + 1    # Left child index
    right = 2 * i + 2   # Right child index
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    """
    Implements the in-place Heapsort algorithm.
    Phase 1: Bottom-up Build Max Heap: call heapify from last non-leaf node and iterate backward 
    Phase 2: Extract elements one by one to sort the array
    We iterate from the end of the array (n-1) down to the second element (1).
      1. Swap the current root (the max element) with the last element
          in the unsorted portion (arr[i]).
      2. The max element is now "sorted" and "locked" at the end.
          The heap size is reduced to 'i'.
      3. heapify the subheap of size i at root index 0
    """
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr
