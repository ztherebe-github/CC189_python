class Solution:
    def isUnique(self, astr: str) -> bool:
        l=len(astr)
        a=""
        for i in range(l):
            if astr[i] not in a:
                a=a+astr[i]
            else:
                return False
        return True
