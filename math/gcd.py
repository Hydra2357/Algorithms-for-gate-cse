def gcd_euclidean(a, b):
    """Calculate GCD using Euclidean algorithm.
    Time Complexity: O(log(min(a, b)))
    Space Complexity: O(1)
    """
    while b:
        a, b = b, a % b
    return a

def gcd_recursive(a, b):
    """Recursive implementation of Euclidean algorithm."""
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

def lcm(a, b):
    """Calculate LCM using GCD."""
    return (a * b) // gcd_euclidean(a, b)

if __name__ == "__main__":
    a, b = 48, 18
    print(f"GCD({a}, {b}) = {gcd_euclidean(a, b)}")
    print(f"LCM({a}, {b}) = {lcm(a, b)}")
