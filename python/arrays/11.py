def moveZeroes(nums):
    write = 0

    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1
        print(write, nums[read])

    for i in range(write, len(nums)):
        nums[i] = 0
    
moveZeroes([0,1,0,3,12])
        