// Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

// You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

// Return the answer with the smaller index first.


function hasSum(arr: number[], target: number): number[] {
    let indices = [];
    for (const [index, i] of arr.entries()) {
        if (arr.includes(target - i)) {
           indices.push(index);
           indices.push(arr.indexOf(target - i));
           break;
        }
    }
    return indices;
}

const list = [1,2,3];
console.log(hasSum(list, 3));

