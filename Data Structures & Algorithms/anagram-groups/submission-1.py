class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict

        def make_rep(word):
            rep = [0]*26
            for c in word:
                rep[ord(c) - ord('a')] += 1
            return rep

        hm = defaultdict(list)

        for string in strs:
            rep = make_rep(string)
            hm[str(rep)].append(string)

        res = []

        for k,v in hm.items():
            res.append(v)
        
        return res


        