import math

def jump_search(arr, target):
    """Search for target using jump search.
    Time Complexity: O(sqrt(n))
    Space Complexity: O(1)
    """
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    if arr[prev] == target:
        return prev
    
    return -1

if __name__ == "__main__":
    test_arr = [11, 12, 22, 25, 34, 64, 90]
    print("Index of 25:", jump_search(test_arr, 25))
    print("Index of 100:", jump_search(test_arr, 100))
