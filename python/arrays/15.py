def removingDuplicates(nums):
    insertIndex = 1
    n = len(nums)

    for i in range(1, n):
        if nums[i - 1] != nums[i]:
            nums[insertIndex] = nums[i]
            insertIndex += 1

    return insertIndex

print(removingDuplicates([1,1,2]))