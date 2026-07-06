def find_duplicates(nums):
    # O(N) time complexity using a set to keep track of seen elements
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)
