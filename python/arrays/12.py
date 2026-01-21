def twoSum(nums, target):
    hashmap = dict()

    for i in range(len(nums)):
        hashmap[nums[i]] = i
    
    for j in range(len(nums)):
        diff = target - nums[j]
        if diff in hashmap and hashmap[diff] != i:
            return [i, hashmap[diff]]
    