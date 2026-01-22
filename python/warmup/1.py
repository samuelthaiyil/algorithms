def twoSum(nums, target):
    hashmap = dict()
    n = len(nums)

    for i in range(n):
        hashmap[nums[i]] = i
    
    for j in range(n):
        diff = target - nums[j]

        if diff in hashmap and nums[diff] != j:
            return [j, nums[diff]] 
