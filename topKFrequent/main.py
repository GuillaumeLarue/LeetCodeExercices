class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for e in nums:
            d[e] += 1

        d = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
        res = []
        for i in range(k):
            res.append(d[i][0])
        return res