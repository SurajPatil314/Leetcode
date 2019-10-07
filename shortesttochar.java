/*
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.
*/
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        
        ab=[]
        ans=[]
        i=0
        i1=0
        for ch in S:
            if ch==C:
                ab.append(i)
            i=i+1
        
            
        for ch1 in S:
            if ch1==C:
                ans.append(0)
            else:
                qw=min(ab,key=lambda x:abs(x-i1))
                we=abs(qw-i1)
                ans.append(we)
                
                
            i1=i1+1
        
        return ans
            
