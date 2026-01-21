function productExceptSelf(arr: number[]): number[] {
  const results: number[] = [];

  let fullProduct = 1;

  for (const num of arr) {
    fullProduct *= num;
  }

  for (const num of arr) {
    results.push(fullProduct / num);
  }

  return results;
}

console.log(productExceptSelf([1,2,4,6]));
