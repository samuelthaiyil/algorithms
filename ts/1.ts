// Contains Duplicate
// Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

// Example 1:

// Input: nums = [1, 2, 3, 3]

// Output: true

// Example 2:

// Input: nums = [1, 2, 3, 4]

// Output: false
function hasDuplicates(list: number[]): boolean {
    const elements = new Set<number>();
    for (const i of list) {
        if (elements.has(i)) return true;
        elements.add(i);
    }
    return false;
}

const l = [1,9,2];
console.log(hasDuplicates(l));

