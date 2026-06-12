def ternary_search(arr, target):
    """Search for target in sorted array using ternary search.
    Time Complexity: O(log3 n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        
        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    
    return -1

if __name__ == "__main__":
    test_arr = [11, 12, 22, 25, 34, 64, 90]
    print("Index of 25:", ternary_search(test_arr, 25))
    print("Index of 100:", ternary_search(test_arr, 100))
