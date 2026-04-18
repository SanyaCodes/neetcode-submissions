class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = dict()
        for num in nums:
            if num not in count_map.keys():
                count_map[num] = 1
            else:
                count_map[num] += 1
        
        sorted_dict = dict(sorted(count_map.items(), key=lambda item: item[1], reverse=True))   

        return list(sorted_dict.keys())[:k]
        