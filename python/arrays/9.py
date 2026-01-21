def largest_perimeter(nums: [int]):
    nums.sort()

    sum_of_sides = 0

    for i in nums:
         if i < sum_of_sides:
            sum_of_sides += i

    return sum_of_sides
        
        