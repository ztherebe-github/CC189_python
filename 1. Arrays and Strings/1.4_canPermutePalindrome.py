class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
            num=0
            l = len(s)
            s1=""
            for i in s:
                if s.count(i)%2 !=0:
                    if i not in s1:
                        s1=s1+i
            if len(s1) > 1:
                return False
            else:
                return True
