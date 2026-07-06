def find_duplicates(nums):
    # Optimized to O(N) time complexity using hash sets
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)
