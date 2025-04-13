def binary_search(arr:list, target:int):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if target == arr[mid]:
            return mid
        if target > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1

print(binary_search([1,2,4,6,7,8,9,11,12], 9))
