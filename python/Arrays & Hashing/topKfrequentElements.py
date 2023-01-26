class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}T
        freq = [[] for i in range(len(nums) + 1) ]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n) #count is the index, at index count, append to the list the value n, value n appears c number of times
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
