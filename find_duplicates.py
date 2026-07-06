def find_duplicates(nums):
    # O(N) time complexity using sets to track seen elements and duplicates
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)
