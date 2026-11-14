class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # key : val

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        arr = []

        for n, cnt in count.items():
            arr.append([cnt, n])
        arr.sort()

        result = []

        while len(result) < k:
            result.append(arr.pop()[1])

        return result