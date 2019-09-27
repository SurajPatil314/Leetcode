'''
We have a string S of lowercase letters, and an integer array shifts.

Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). 

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

Return the final string after all such shifts to S are applied.
'''

class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        
        alpha= {}
        i=1
        ans=[]
        letters = list(string.ascii_lowercase)
        for c in letters:
            alpha.update({c:i})
            i=i+1
            
        #print(alpha)
       
        i1=0
        
        reversealpha = dict([(value, key) for key, value in alpha.items()])
        #print(reversealpha)
        
        for ch in S:            
            
            nq= alpha[ch]
            
            for nu in range(i1,len(shifts)):
                nq=nq+shifts[nu]
            la=nq%26
            chq=None
            if la==0:
                chq='z'
            else:
                chq= reversealpha[la]
            ans.append(chq)
            i1=i1+1
        
        
        
        finalstring = ''.join(map(str, ans))
    
        return finalstring
      
            
        