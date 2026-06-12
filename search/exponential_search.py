def exponential_search(arr, target):
    """Search for target using exponential search.
    Time Complexity: O(log n)
    Space Complexity: O(log n)
    """
    n = len(arr)
    
    if arr[0] == target:
        return 0
    
    i = 1
    while i < n and arr[i] < target:
        i *= 2
    
    return binary_search_range(arr, target, i // 2, min(i, n - 1))

def binary_search_range(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    test_arr = [11, 12, 22, 25, 34, 64, 90]
    print("Index of 25:", exponential_search(test_arr, 25))
    print("Index of 100:", exponential_search(test_arr, 100))
