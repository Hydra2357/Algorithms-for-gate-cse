def two_sum(arr, target):
    """Find two numbers that sum to target using two pointers.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [arr[left], arr[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None

def container_with_most_water(heights):
    """Find two lines that can hold most water.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    max_area = 0
    left, right = 0, len(heights) - 1
    
    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        area = width * height
        max_area = max(max_area, area)
        
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

if __name__ == "__main__":
    arr = [2, 7, 11, 15]
    target = 9
    print(f"Two sum for target {target}: {two_sum(arr, target)}")
    
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Max water area: {container_with_most_water(heights)}")
