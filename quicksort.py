import random

def partition(arr, low, high):
    pivot = arr[high]  # choosing the last element as the pivot
    i = low - 1  
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def random_partition(arr, low, high):
    rand_index = random.randint(low, high)
    arr[high], arr[rand_index] = arr[rand_index], arr[high]
    return partition(arr, low, high)

def random_quicksort(arr, low, high):
    if low < high:
        pi = random_partition(arr, low, high)
        random_quicksort(arr, low, pi - 1)
        random_quicksort(arr, pi + 1, high)


arr = [11, 8, 9, 10, 2, 6]
n = len(arr)
quicksort(arr, 0, n - 1)
print("Sorted array (non-random pivot):", arr)

arr = [1, 17, 8, 2, 3, 20]
n = len(arr)
random_quicksort(arr, 0, n - 1)
print("Sorted array (random pivot):", arr)
