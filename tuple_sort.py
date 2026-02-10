def selection_sort_tuples(arr):
    n = len(arr)
    
    for i in range(len(arr)):
        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j][1] < arr[min_idx][1]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


data = [('a', 5), ('b', 2), ('c', 9), ('d', 1), ('e', 7), ('f', 3), ('g', 8), ('h', 4), ('i', 6), ('j', 0)]
sorted_data = selection_sort_tuples(data)
print(sorted_data)


"""
Pass 1 (i = 0)
i = 0, min_idx = 0 (initially points to ('a', 5))
.

Inner loop searches for minimum:

j = 1: arr[0][1] = 5 > arr[1][1] = 2? Yes - min_idx = 1
j = 2: arr[1][1] = 2 > arr[2][1] = 9? No  - min_idx = 1
j = 3: arr[1][1] = 2 > arr[3][1] = 1? Yes - min_idx = 3
j = 4: arr[3][1] = 1 > arr[4][1] = 7? No  - min_idx = 3
j = 5: arr[3][1] = 1 > arr[5][1] = 3? No  - min_idx = 3
j = 6: arr[3][1] = 1 > arr[6][1] = 8? No  - min_idx = 3
j = 7: arr[3][1] = 1 > arr[7][1] = 4? No  - min_idx = 3
j = 8: arr[3][1] = 1 > arr[8][1] = 6? No  - min_idx = 3
j = 9: arr[3][1] = 1 > arr[9][1] = 0? Yes - min_idx = 9


Result: Minimum is ('j', 0) at index 9

Swap:

Before: [('a', 5), ('b', 2), ('c', 9), ('d', 1), ('e', 7), ('f', 3), ('g', 8), ('h', 4), ('i', 6), ('j', 0)]
        i=0                                                                                      min_idx=9

After:  [('j', 0), ('b', 2), ('c', 9), ('d', 1), ('e', 7), ('f', 3), ('g', 8), ('h', 4), ('i', 6), ('a', 5)]
        sorted

Pass 2 (i = 1)
i = 1, min_idx = 1 (initially points to ('b', 2))


Inner loop searches for minimum:

j = 2: arr[1][1] = 2 > arr[2][1] = 9? No  - min_idx = 1
j = 3: arr[1][1] = 2 > arr[3][1] = 1? Yes - min_idx = 3
j = 4: arr[3][1] = 1 > arr[4][1] = 7? No  - min_idx = 3
j = 5: arr[3][1] = 1 > arr[5][1] = 3? No  - min_idx = 3
j = 6: arr[3][1] = 1 > arr[6][1] = 8? No  - min_idx = 3
j = 7: arr[3][1] = 1 > arr[7][1] = 4? No  - min_idx = 3
j = 8: arr[3][1] = 1 > arr[8][1] = 6? No  - min_idx = 3
j = 9: arr[3][1] = 1 > arr[9][1] = 5? No  - min_idx = 3


Result: Minimum is ('d', 1) at index 3

Swap:

Before: [('j', 0), ('b', 2), ('c', 9), ('d', 1), ('e', 7), ('f', 3), ('g', 8), ('h', 4), ('i', 6), ('a', 5)]
            i=1      min_idx=3

After:  [('j', 0), ('d', 1), ('c', 9), ('b', 2), ('e', 7), ('f', 3), ('g', 8), ('h', 4), ('i', 6), ('a', 5)]
            sorted

Pass 3 (i = 2)
i = 2, min_idx = 2 (initially points to ('c', 9))


Inner loop searches for minimum:

j = 3: arr[2][1] = 9 > arr[3][1] = 2? Yes - min_idx = 3
j = 4: arr[3][1] = 2 > arr[4][1] = 7? No  - min_idx = 3
j = 5: arr[3][1] = 2 > arr[5][1] = 3? No  - min_idx = 3
j = 6: arr[3][1] = 2 > arr[6][1] = 8? No  - min_idx = 3
j = 7: arr[3][1] = 2 > arr[7][1] = 4? No  - min_idx = 3
j = 8: arr[3][1] = 2 > arr[8][1] = 6? No  - min_idx = 3
j = 9: arr[3][1] = 2 > arr[9][1] = 5? No  - min_idx = 3


Result: Minimum is ('b', 2) at index 3

Swap:

Before: [('j', 0), ('d', 1), ('c', 9), ('b', 2), ('e', 7), ('f', 3), ('g', 8), ('h', 4), ('i', 6), ('a', 5)]
                i=2     min_idx=3

After:  [('j', 0), ('d', 1), ('b', 2), ('c', 9), ('e', 7), ('f', 3), ('g', 8), ('h', 4), ('i', 6), ('a', 5)]
                sorted

Pass 4 (i = 3)
i = 3, min_idx = 3 (initially points to ('c', 9))


Inner loop searches for minimum:

j = 4: arr[3][1] = 9 > arr[4][1] = 7? Yes - min_idx = 4
j = 5: arr[4][1] = 7 > arr[5][1] = 3? Yes - min_idx = 5
j = 6: arr[5][1] = 3 > arr[6][1] = 8? No  - min_idx = 5
j = 7: arr[5][1] = 3 > arr[7][1] = 4? No  - min_idx = 5
j = 8: arr[5][1] = 3 > arr[8][1] = 6? No  - min_idx = 5
j = 9: arr[5][1] = 3 > arr[9][1] = 5? No  - min_idx = 5


Result: Minimum is ('f', 3) at index 5

Swap:

Before: [('j', 0), ('d', 1), ('b', 2), ('c', 9), ('e', 7), ('f', 3), ('g', 8), ('h', 4), ('i', 6), ('a', 5)]
                    i=3        min_idx=5

After:  [('j', 0), ('d', 1), ('b', 2), ('f', 3), ('e', 7), ('c', 9), ('g', 8), ('h', 4), ('i', 6), ('a', 5)]
                    sorted

Pass 5 (i = 4)
i = 4, min_idx = 4 (initially points to ('e', 7))


Inner loop searches for minimum:

j = 5: arr[4][1] = 7 > arr[5][1] = 9? No  - min_idx = 4
j = 6: arr[4][1] = 7 > arr[6][1] = 8? No  - min_idx = 4
j = 7: arr[4][1] = 7 > arr[7][1] = 4? Yes - min_idx = 7
j = 8: arr[7][1] = 4 > arr[8][1] = 6? No  - min_idx = 7
j = 9: arr[7][1] = 4 > arr[9][1] = 5? No  - min_idx = 7


Result: Minimum is ('h', 4) at index 7

Swap:

Before: [('j', 0), ('d', 1), ('b', 2), ('f', 3), ('e', 7), ('c', 9), ('g', 8), ('h', 4), ('i', 6), ('a', 5)]
                        i=4      min_idx=7

After:  [('j', 0), ('d', 1), ('b', 2), ('f', 3), ('h', 4), ('c', 9), ('g', 8), ('e', 7), ('i', 6), ('a', 5)]
                        sorted

Pass 6 (i = 5)
i = 5, min_idx = 5 (initially points to ('c', 9))


Inner loop searches for minimum:

j = 6: arr[5][1] = 9 > arr[6][1] = 8? Yes - min_idx = 6
j = 7: arr[6][1] = 8 > arr[7][1] = 7? Yes - min_idx = 7
j = 8: arr[7][1] = 7 > arr[8][1] = 6? Yes - min_idx = 8
j = 9: arr[8][1] = 6 > arr[9][1] = 5? Yes - min_idx = 9


Result: Minimum is ('a', 5) at index 9

Swap:

Before: [('j', 0), ('d', 1), ('b', 2), ('f', 3), ('h', 4), ('c', 9), ('g', 8), ('e', 7), ('i', 6), ('a', 5)]
                            i=5       min_idx=9

After:  [('j', 0), ('d', 1), ('b', 2), ('f', 3), ('h', 4), ('a', 5), ('g', 8), ('e', 7), ('i', 6), ('c', 9)]
                            sorted

Pass 7 (i = 6)
i = 6, min_idx = 6 (initially points to ('g', 8))


Inner loop searches for minimum:

j = 7: arr[6][1] = 8 > arr[7][1] = 7? Yes - min_idx = 7
j = 8: arr[7][1] = 7 > arr[8][1] = 6? Yes - min_idx = 8
j = 9: arr[8][1] = 6 > arr[9][1] = 9? No  - min_idx = 8


Result: Minimum is ('i', 6) at index 8

Swap:

Before: [('j', 0), ('d', 1), ('b', 2), ('f', 3), ('h', 4), ('a', 5), ('g', 8), ('e', 7), ('i', 6), ('c', 9)]
                                i=6      min_idx=8

After:  [('j', 0), ('d', 1), ('b', 2), ('f', 3), ('h', 4), ('a', 5), ('i', 6), ('e', 7), ('g', 8), ('c', 9)]
                                sorted

Pass 8 (i = 7)
i = 7, min_idx = 7 (initially points to ('e', 7))


Inner loop searches for minimum:

j = 8: arr[7][1] = 7 > arr[8][1] = 8? No - min_idx = 7
j = 9: arr[7][1] = 7 > arr[9][1] = 9? No - min_idx = 7


Result: Minimum is ('e', 7) at index 7

Swap:

Before: [('j', 0), ('d', 1), ('b', 2), ('f', 3), ('h', 4), ('a', 5), ('i', 6), ('e', 7), ('g', 8), ('c', 9)]
                                    i=7 min_idx=7

After:  [('j', 0), ('d', 1), ('b', 2), ('f', 3), ('h', 4), ('a', 5), ('i', 6), ('e', 7), ('g', 8), ('c', 9)]
                                    sorted

Pass 9 (i = 8)
i = 8, min_idx = 8 (initially points to ('g', 8))


Inner loop searches for minimum:

j = 9: arr[8][1] = 8 > arr[9][1] = 9? No - min_idx = 8


Result: Minimum is ('g', 8) at index 8

Swap:

Before: [('j', 0), ('d', 1), ('b', 2), ('f', 3), ('h', 4), ('a', 5), ('i', 6), ('e', 7), ('g', 8), ('c', 9)]
                                        i=8 min_idx=8

After:  [('j', 0), ('d', 1), ('b', 2), ('f', 3), ('h', 4), ('a', 5), ('i', 6), ('e', 7), ('g', 8), ('c', 9)]
                                        sorted

Final Sorted Array
[('j', 0), ('d', 1), ('b', 2), ('f', 3), ('h', 4), ('a', 5), ('i', 6), ('e', 7), ('g', 8), ('c', 9)]
"""
