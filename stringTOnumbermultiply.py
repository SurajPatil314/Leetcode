'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''



class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        d={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        
        num11= num1[::-1]
        num22= num2[::-1]
        
        ten=1
        ten1=1
        j1=0
        j2=0
        for i in num11:
            if i in d:
                j1=j1+d[i]*ten
                ten=ten*10
                
        for i1 in num22:
            if i1 in d:
                j2=j2+d[i1]*ten1
                ten1=ten1*10
                
        print(j1)
        print(j2)
        
        return str(j1*j2)