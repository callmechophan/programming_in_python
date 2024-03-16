# time is measured by how long it takes
# space is about how much memory it uses
#
# constant time - O(1)
# - same time and space despite size
#
# linear time - O(n)
# - will grow depending on the size of the input (the bigger the range, the bigger the running time)
# 
# logarithmic time - O(logn)
# - refers to the running time of the inputs againts the number of operations
#
# quadratic time - O(n^2)
# - refers to a linear operation of each value of the input data squared

# constant time
def access_element(arr, index):
    return arr[index]


# linear time
def linear_search(arr, target):
    for i in arr:
        if i == target:
            return True
    return False

# logarithmic time
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

# quadratic time
def bubble_sort(arr):
    n = len(arr) - 1
    for i in range(n):
        for j in range(0, n - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
