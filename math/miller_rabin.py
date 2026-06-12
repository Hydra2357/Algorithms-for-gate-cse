def miller_rabin_primality_test(n, k=5):
    """Miller-Rabin probabilistic primality test.
    Time Complexity: O(k log^3 n)
    Space Complexity: O(log n)
    """
    
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    import random
    
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True

if __name__ == "__main__":
    test_numbers = [17, 18, 97, 100]
    for num in test_numbers:
        print(f"{num} is prime: {miller_rabin_primality_test(num)}")
