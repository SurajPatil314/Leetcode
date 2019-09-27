'''
Find the minimum length word from a given dictionary words, which has all the letters from the string licensePlate. Such a word is said to complete the given string licensePlate

Here, for letters we ignore case. For example, "P" on the licensePlate still matches "p" on the word.

It is guaranteed an answer exists. If there are multiple answers, return the one that occurs first in the array.

The license plate might have the same letter occurring multiple times. For example, given a licensePlate of "PP", the word "pair" does not complete the licensePlate, but the word "supper" does.
'''


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
        ans1=[]
        ans3=[]
        
        if(len(licensePlate) ==0 or len(words)==0):
            return None
        
        for char1 in licensePlate:
            if char1.isalpha():
                ans1.append(char1.lower())
                
        print(ans1)
        
        for litem in words:
            ans2=[]
            ans2 = ans1.copy()
            for litemchar in litem:
                if litemchar.isalpha():
                    if litemchar.lower() in ans2:
                        ans2.remove(litemchar.lower())
            if len(ans2)==0:
                ans3.append(litem)
                
        print("ans3::")
        print(ans3)
                
        if len(ans3)==0:
            return None
        else:
            len1= len(ans3[0])
            fans= ans3[0]
            for qw in ans3:
                if len(qw)<len1:
                    fans=qw
                    len1= len(qw)
            return fans