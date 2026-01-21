function groupAnagrams(list: string[]): string[][] {
  function isAnagram(l: string, s: string): boolean {
    if (s.length !== l.length) return false;

    for (const i of s) {
      if (!l.includes(i)) return false;
    }

    return true;
  }

  let results: string[][] = [[list[0]!]];

  for (const word of list) {
    let found = false;
    for (const i of results) {
      if (isAnagram(i[0]!, word)) {
        i.push(word);
        found = true;
      }
    }
    if (!found) {
      results.push([word]);
    }
  }

  return results;
}

console.log(groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]));
