def sieve_of_atkin(limit):
    """Sieve of Atkin for finding all primes up to limit.
    Time Complexity: O(n / log log n)
    Space Complexity: O(n)
    """
    
    if limit < 2:
        return []
    
    is_prime = [False] * (limit + 1)
    
    for x in range(1, int(limit**0.5) + 1):
        for y in range(1, int(limit**0.5) + 1):
            n = 4 * x * x + y * y
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                is_prime[n] = not is_prime[n]
            
            n = 3 * x * x + y * y
            if n <= limit and n % 12 == 7:
                is_prime[n] = not is_prime[n]
            
            n = 3 * x * x - y * y
            if x > y and n <= limit and n % 12 == 11:
                is_prime[n] = not is_prime[n]
    
    for i in range(5, int(limit**0.5) + 1):
        if is_prime[i]:
            n = i * i
            while n <= limit:
                is_prime[n] = False
                n += i * i
    
    return [2, 3] + [i for i in range(5, limit + 1) if is_prime[i]]

if __name__ == "__main__":
    limit = 100
    primes = sieve_of_atkin(limit)
    print(f"Primes up to {limit}: {primes}")
