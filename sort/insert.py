

def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        for j in range(i-1, -2, -1):
            if key < arr[j]:
                arr[j+1] = arr[j]
            else:
                break
        arr[j+1] = key
    return arr

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1, i, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr
    