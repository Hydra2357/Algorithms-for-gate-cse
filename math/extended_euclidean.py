def extended_euclidean_algorithm(a, b):
    """Extended Euclidean algorithm.
    Finds GCD and coefficients x, y such that ax + by = gcd(a, b)
    Time Complexity: O(log(min(a, b)))
    Space Complexity: O(log(min(a, b)))
    """
    
    if b == 0:
        return a, 1, 0
    
    gcd, x1, y1 = extended_euclidean_algorithm(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd, x, y

def modular_inverse(a, m):
    """Find modular inverse of a modulo m using extended Euclidean algorithm.
    Time Complexity: O(log(min(a, m)))
    """
    
    gcd, x, _ = extended_euclidean_algorithm(a, m)
    
    if gcd != 1:
        return None  # Modular inverse doesn't exist
    
    return (x % m + m) % m

if __name__ == "__main__":
    a, b = 35, 15
    gcd, x, y = extended_euclidean_algorithm(a, b)
    print(f"GCD({a}, {b}) = {gcd}")
    print(f"Coefficients: {a}*{x} + {b}*{y} = {gcd}")
    
    a, m = 3, 11
    inv = modular_inverse(a, m)
    print(f"Modular inverse of {a} mod {m}: {inv}")
