class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # A list of strings, and we need to sort all the anagrams together in one list (sublists).
        res = defaultdict(list) # mapping charCount to list of anagrams

        for s in strs:
            count = [0] * 26 # lower case a - z

            for c in s:
                # Use ord to turn char into the ascii value
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())