def counting_sort(arr):
    """Sort array using counting sort algorithm.
    Time Complexity: O(n + k) where k is the range
    Space Complexity: O(k)
    """
    if not arr:
        return arr
    
    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1
    
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1
    
    result = []
    for i, cnt in enumerate(count):
        result.extend([i + min_val] * cnt)
    
    return result

if __name__ == "__main__":
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print("Sorted array:", counting_sort(test_arr))
