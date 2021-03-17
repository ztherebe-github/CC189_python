class Solution:
    def compressString(self, S: str) -> str:
        
        s=S+"1"
        first=0
        l=len(s)
        s1=""
        for second in range(0,l):
            if  s[first] != s[second] :
                num=second-first
                s1=s1+s[first]+str(num)
                first = second
        if len(s1)>=len(S):
            return S
        else:
            return s1
