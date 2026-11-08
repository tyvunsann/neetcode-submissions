class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # Implement two hashmaps to count each letters in each string
        countS, countT = {}, {}

        for i in range(len(s)):
            # Count the occurrence of each character.
            # Use .get if key doesn't exist
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT