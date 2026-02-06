def searchInSorted(nums, target):
    # find pivot point
    n = len(nums)
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2

        # update the search space
        if nums[mid] > nums[-1]:
            left = mid + 1
        else:
            right = mid - 1
    
    def binarySearch(lb, rb, target):
        left, right = lb, rb

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            # update search space
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            
        return -1
    
    if (answer := binarySearch(0, left - 1, target) != - 1):
        return answer
    
    return binarySearch(left, n - 1, target)


                