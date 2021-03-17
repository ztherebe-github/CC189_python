class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        S=S[0:length]
        t=list(S)
        s1=""
        for i in range(length):
            if t[i]==" ":
                t[i]='%20'
            s1=s1+t[i]
        return s1
