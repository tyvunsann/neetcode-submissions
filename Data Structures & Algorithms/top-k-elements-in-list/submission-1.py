class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # val : index

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # We can try to sort by frequency which will give us a time complexity of klog(n)

        arr = []

        # Flip the pair
        for num, cnt in count.items():
            arr.append([cnt, num])
        # Sort lowest to highest
        arr.sort()

        res = []
        while len(res) < k: 
            res.append(arr.pop()[1])
        return res