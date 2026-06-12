def max_sliding_window(arr, k):
    """Find maximum in each sliding window.
    Time Complexity: O(n)
    Space Complexity: O(k)
    """
    from collections import deque
    
    if not arr or k <= 0:
        return []
    
    result = []
    dq = deque()
    
    for i in range(len(arr)):
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(arr[dq[0]])
    
    return result

def longest_substring_without_repeating(s):
    """Find longest substring without repeating characters.
    Time Complexity: O(n)
    Space Complexity: O(min(n, m)) where m is charset size
    """
    char_index = {}
    max_length = 0
    start = 0
    
    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        
        char_index[char] = i
        max_length = max(max_length, i - start + 1)
    
    return max_length

if __name__ == "__main__":
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(f"Max sliding window: {max_sliding_window(arr, k)}")
    
    s = "abcabcbb"
    print(f"Longest substring without repeating: {longest_substring_without_repeating(s)}")
