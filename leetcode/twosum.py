def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        buff = target - num
        if buff in seen:
            return [seen[buff], i]
        seen[num] = i