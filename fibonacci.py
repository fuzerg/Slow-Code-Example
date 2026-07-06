def fibonacci(n):
    """
    An optimized iterative implementation of Fibonacci numbers.
    This implementation has linear time complexity O(n) and constant space complexity O(1).
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
