
def bubble_sort(arr):

    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example Usage
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("Bubble Sort Result:", bubble_sort(unsorted_list))

