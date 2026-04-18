class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_ord(s):
            a = [0]*26
            for i in s.lower():
                a[ord(i) - ord('a')] += 1
            return a
        
        s_dict = dict()
        for string in strs:
            order = str(get_ord(string))
            if order in s_dict.keys():
                s_dict[order].append(string)
            else:
                s_dict[order] = [string]
        
        return list(s_dict.values())

        