class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def make_rep(string):
            rep = [0]*26
            for s in string:
                rep[ord(s)-ord('a')] += 1

            return rep
        
        if make_rep(s) == make_rep(t):
            return True
        
        return False
            

        