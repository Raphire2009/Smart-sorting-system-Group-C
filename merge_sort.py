def merge_sort(arr):
    if len(arr) > 1:
        M = len(arr) // 2
        L = arr[:M]
        R = arr[M:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

list_to_sort = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(list_to_sort)
print("Sorted array is:", sorted_list)


"""
Recursive Splitting (Divide Phase)

Merge Sort repeatedly splits the list into halves until each sublist has one element.

Recursive Call Tree
                        [38, 27, 43, 3, 9, 82, 10]
                         /                     \
            [38, 27, 43]                       [3, 9, 82, 10]
              /        \                       /           \
        [38, 27]      [43]                [3, 9]         [82, 10]
         /     \                           /    \           /    \
      [38]   [27]                       [3]    [9]       [82]   [10]


At this point, all sublists have size 1 → stop splitting.

Merging sublists (Conquer phase)

The merging process combines the sublists back together in sorted order.

Merge call tree
                           [3, 9, 10, 27, 38, 43, 82]
                           /                      \
             [27, 38, 43]                          [3, 9, 10, 82]
             /         \                          /           \
       [27, 38]        [43]                  [3, 9]        [10, 82]
        /     \                                 /  \          /   \
     [38]    [27]                           [3]   [9]      [82]   [10]


Why Merge Sort (O(n log n)) is faster than O(n²) algorithms like Bubble Sort for large lists
Key idea: Growth rate of time complexity
Bubble Sort: O(n²)

Bubble Sort compares almost every pair of elements.

If n = 10 → about 100 operations

If n = 1,000 → about 1,000,000 operations

If n = 1,000,000 → about 1,000,000,000,000 operations (1 trillion!)

Its work increases quadratically as n grows.

Merge Sort: O(n log n)

Merge Sort:

Splits the list into halves → log n levels of recursion.

Merges elements at each level → n work per level.

Total work:

𝑛
log
⁡
2
𝑛
nlog
2
	​

n

Examples:

If n = 10 → ≈ 10 × 3.3 = 33 operations

If n = 1,000 → ≈ 1,000 × 10 = 10,000 operations

If n = 1,000,000 → ≈ 1,000,000 × 20 = 20,000,000 operations

This grows much slower than n².

Intuitive explanation
Bubble Sort

Compares elements one by one repeatedly.

Very inefficient because it keeps scanning the list many times.

Merge Sort

Uses “divide and conquer”.

Breaks the problem into smaller pieces.

Sorts efficiently and combines results.

For large lists, Merge Sort does far fewer comparisons → much faster.

Graph intuition (important for understanding)

As n increases:

n² grows extremely fast.

n log n grows much slower.

So for large n:

𝑛
log
⁡
𝑛
≪
𝑛
2
nlogn≪n
2

That’s why Merge Sort is generally faster than Bubble Sort for big datasets.

2) Space Complexity of Merge Sort

Merge Sort needs extra memory to store temporary sublists during merging.

Extra space needed

For an array of size n:

Merge Sort creates temporary arrays to merge elements.

Total extra space ≈ n.

So the space complexity is:

𝑂
(
𝑛
)
O(n)
Why O(n)?

Even though there are many recursive calls:

At any given time, the total extra space used across all merges is proportional to n, not n log n.

The recursion stack adds extra space too.

More precise breakdown:

Temporary arrays for merging: O(n)

Recursion call stack: O(log n)

Total space complexity:

𝑂(𝑛)
O(n)

(because O(n) dominates O(log n))

3) Quick comparison table
Algorithm	Time Complexity	Space Complexity
Bubble Sort	O(n²)	O(1) (in-place)
Merge Sort	O(n log n)	O(n)
"""