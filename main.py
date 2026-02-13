import time

# ==============================
# QUICK SORT (PRIMARY ALGORITHM)
# ==============================
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# ==============================
# MERGE SORT (ALTERNATE ALGORITHM)
# ==============================
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# ==============================
# MAIN PROGRAM
# ==============================
def main():
    print("==== SMART SORTING SYSTEM ====")
    print("Primary Algorithm: Quick Sort")
    print("Alternate Algorithm: Merge Sort")
    print()

    try:
        data = input("Enter numbers separated by commas: ")
        numbers = list(map(int, data.split(",")))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return

    print("\nChoose Sorting Algorithm:")
    print("Q - Quick Sort")
    print("M - Merge Sort")

    choice = input("Your choice: ").upper()

    print("\nChoose Order:")
    print("A - Ascending")
    print("D - Descending")

    order = input("Your choice: ").upper()

    start_time = time.time()

    if choice == "Q":
        sorted_numbers = quick_sort(numbers)
        algorithm_used = "Quick Sort"
    elif choice == "M":
        sorted_numbers = merge_sort(numbers)
        algorithm_used = "Merge Sort"
    else:
        print("Invalid algorithm choice!")
        return

    if order == "D":
        sorted_numbers.reverse()
    elif order != "A":
        print("Invalid order choice!")
        return

    end_time = time.time()

    print("\n===== RESULTS =====")
    print("Algorithm Used:", algorithm_used)
    print("Sorted Result:", sorted_numbers)
    print("Execution Time:", round(end_time - start_time, 6), "seconds")


# Run Program
if __name__ == "__main__":
    main()
