def linear_search(arr, target):
    """Search for target in array using linear search.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print("Index of 25:", linear_search(test_arr, 25))
    print("Index of 100:", linear_search(test_arr, 100))
