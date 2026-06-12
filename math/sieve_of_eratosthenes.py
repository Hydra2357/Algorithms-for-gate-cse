def sieve_of_eratosthenes(n):
    """Find all primes up to n using Sieve of Eratosthenes.
    Time Complexity: O(n log log n)
    Space Complexity: O(n)
    """
    if n < 2:
        return []
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    
    return [i for i in range(n + 1) if is_prime[i]]

def sieve_of_eratosthenes_optimized(n):
    """Optimized version marking only odd numbers."""
    if n < 2:
        return []
    if n == 2:
        return [2]
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if is_prime[i]:
            for j in range(i*i, n + 1, 2*i):
                is_prime[j] = False
    
    return [2] + [i for i in range(3, n + 1, 2) if is_prime[i]]

if __name__ == "__main__":
    n = 50
    print(f"Primes up to {n}: {sieve_of_eratosthenes(n)}")
