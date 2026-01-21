// Valid Anagram
// Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

// An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

function isAnagram(l: string, s: string): boolean {
    if (s.length !== l.length) return false;

    for (const i of s) {
        if (!l.includes(i)) return false;
    }

    return true;
}

console.log(isAnagram("car", "rac"));