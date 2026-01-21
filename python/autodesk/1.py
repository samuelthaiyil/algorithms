def rotated_arr_search(nums, target):
    n = len(nums)
    left, right = 0, n - 1

# determine pivot (smallest number in the array)
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] > nums[-1]:
            left = mid + 1
        else:
            right = mid - 1
        
        print(f"pivot at index {left}")
        
        # standard binary search
        def binary_search(lb, rb, target):
            left, right = lb, rb

            # while the left pointer is less than or equal to the right pointer 
            while left <= right:
                # determine the mid point 
                mid = (left + right) // 2

                # if the target is equal to the mid point ereturn the mid point
                if nums[mid] == target:
                    return mid
                # if the target is less than the mid point, search the first segment; set the right pointer to the end of the first segment (mid point index - 1)
                elif nums[mid] > target:
                    right = mid - 1
                # if the target is greater than the mid point search the second segment; set the left pointer to the beginning of the second segment (mid point index + 1)
                else:
                    left = mid + 1
                
            # if no target found in nums return -1
            return -1
        
        # search first segment
        if (answer := binary_search(0, left - 1, target)) != -1:
            return answer

        # search second segment
        return binary_search(left, n - 1, target)

print(rotated_arr_search([4,5,6,7,0,1,2], 5))

        

        
