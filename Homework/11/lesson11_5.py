def remove_duplicates(nums: list) -> int:
    if not nums:
        return 0
    unique_index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[unique_index] = nums[i]
            unique_index += 1
    while unique_index < len(nums):
        nums[unique_index] = "_"
        unique_index += 1
    return unique_index


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = remove_duplicates(nums)
print(k)
print(nums)
