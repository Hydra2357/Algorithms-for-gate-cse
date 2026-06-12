def maximum_subarray_kadane(arr):
    """Kadane's algorithm for maximum subarray sum.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    
    max_sum = arr[0]
    current_sum = arr[0]
    
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def maximum_subarray_with_indices(arr):
    """Return maximum sum and the subarray indices."""
    
    max_sum = arr[0]
    current_sum = arr[0]
    start = 0
    end = 0
    temp_start = 0
    
    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return max_sum, start, end, arr[start:end + 1]

if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Maximum sum: {maximum_subarray_kadane(arr)}")
    
    max_sum, start, end, subarray = maximum_subarray_with_indices(arr)
    print(f"Maximum sum: {max_sum}, Start: {start}, End: {end}, Subarray: {subarray}")
