class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        else:
            for i in s1:
                if s1.count(i)!=s2.count(i):
                    return False
            return True
