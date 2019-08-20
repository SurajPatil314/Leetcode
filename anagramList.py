'''
Given an array of strings, group anagrams together.
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        w=0
        list3=[]
        if len(strs)==0:
            return list3
        if len(strs)==1:
            return [strs]
        for el in strs:
            list1=[]
            list2=[]
            if el=="":
                print("empty")
                
                for we1 in strs:
                    if we1=="":
                        list2.append(el)
                if list2 not in list3:
                    list3.append(list2)
                print(list3)
            else:
                print("word is::"+el)
                print(list1)
                w=1
                for q in el:
                    list1.append(q)
                for we in strs:
                    a=1
                    
                    if we=="":
                        continue
                    else:
                        for w in we:
                            if w in list1:
                                
                                a=1
                            else:
                                
                                a=0
                                break
                        if ((a==1) and sorted(el)==sorted(we)):
                            print("we::"+we)
                            list2.append(we)
                print("list2 after iteration")
                print(list2)
            if list2 not in list3:
                list3.append(list2)
        
        if w==0:
            return [strs]
        print("final list::")
        print(list3)
        
        return list3
            
                
                        
                        
                        
        