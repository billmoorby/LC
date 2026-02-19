class Solution:

  def topKFrequent(self, nums, k):
    freq_map = {}
    buckets = [[] for i in range(len(nums)+1)]
    res = []

    for n in nums:
      freq_map[n] = freq_map.get(n, 0)+1

    for n, freq in freq_map.items():
      buckets[freq].append(n)
    
    for i in range(len(buckets)-1, -1, -1):
      if buckets[i]:
        for j in buckets[i]:
          res.append(j)
          if len(res) == k:
            return res
