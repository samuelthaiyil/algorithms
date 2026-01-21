function validPalindrome(str: string): boolean {
  let reversedStr = "";

  for (let i = str.length - 1; i >= 0; i--) {
    reversedStr += str[i];
  }

  console.log(reversedStr);

  return (
    reversedStr.toLowerCase().replaceAll(" ", "") ===
    str.toLowerCase().replaceAll(" ", "")
  );
}

console.log(validPalindrome("Was it a car or a cat I saw"));
