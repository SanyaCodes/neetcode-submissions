class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def get_order(s):
            a = [0] * 26
            for i in s.lower():
                a[ord(i)-ord('a')] += 1
            return a

        if get_order(s) == get_order(t): return True
        else: return False