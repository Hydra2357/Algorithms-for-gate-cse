def bucket_sort(arr):
    """Sort array using bucket sort algorithm.
    Time Complexity: O(n + k) average
    Space Complexity: O(n + k)
    """
    if not arr:
        return arr
    
    min_val = min(arr)
    max_val = max(arr)
    bucket_count = len(arr)
    bucket_range = (max_val - min_val) / bucket_count
    
    buckets = [[] for _ in range(bucket_count)]
    
    for num in arr:
        if num == max_val:
            buckets[bucket_count - 1].append(num)
        else:
            index = int((num - min_val) / bucket_range)
            buckets[index].append(num)
    
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    
    return sorted_arr

if __name__ == "__main__":
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print("Sorted array:", bucket_sort(test_arr))
