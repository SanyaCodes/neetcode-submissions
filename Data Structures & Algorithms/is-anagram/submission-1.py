class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t) or len(set(s)) != len(set(t)):
            return False

        res = [0]*26
        
        n = len(s)

        for i in range(n):
            res[ord(s[i]) - ord('a')] += 1
            res[ord(t[i]) - ord('a')] -= 1
        
        return set(res)=={0}
        