class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:

        l1=len(first)
        l2=len(second)
        if abs(l1-l2)>1:
            return False
        else:
            if first==second:
                return True
            num=0
            if l1==l2:
                for i in range(l1):
                    if first[i] != second[i]:
                        num += 1
                if num == 1:
                    return True
                else:
                    return False
            else:        
                if l2>l1:
                    first,second=second,first
                for i in range(len(second)):
                    if first[i] != second[i]:
                        if first[0:i]+first[i+1:] != second:
                            return False
                        else:
                            return True    
                return True  
