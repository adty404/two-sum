def two_sum(nums, target):
    index_map = {}

    for i, num in enumerate(nums):
        complement = target - num

        # Check if the complement exists in the map
        if complement in index_map:
            return [index_map[complement], i]

        # Add the current element and its index to the map
        index_map[num] = i

    # If no such indices are found, return an empty list
    return []
