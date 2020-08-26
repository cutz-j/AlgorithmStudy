def merge(left, right):
    res = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                res.append(left[0])
                left = left[1:]
            else:
                res.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            res.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            res.append(right[0])
            right = right[1:]
    return res
            

def merge_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    
    mid = length // 2
    left = arr[:mid]
    right = arr[mid:]
    left_arr = merge_sort(left)
    right_arr = merge_sort(right)
    res = merge(left_arr, right_arr)
    return res
    
    