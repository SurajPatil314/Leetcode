if __name__ == "__main__":


    l1=[]
    l2=[]


    for i in range(1,1000):
        for i1 in range(1,1000):
            i2=i*i1
            if i2<1001:
                istr = list(int(d) for d in str(i2))


                gh=0
                #print('first::'+str(i1)+"second::"+str(i))
                #print(istr)
                if len(istr)==1:
                    l2=[]
                    l2.append(i1)
                    l2.append(i)
                    print('l2 data before')
                    print(l2)
                    l2.sort()
                    if l2 not in l1:
                        print('l2 data')
                        print(l2)
                        #print("found::")
                        #print(l2)
                        l1.append(l2)
                else:
                    #print('first::'+str(i1)+"second::"+str(i))
                    #print(istr)
                    for y in range(1,len(istr)):
                        if istr[y-1]<istr[y]:
                            gh=0
                        if istr[y-1]==istr[y]:
                            gh=1
                            break
                        if istr[y-1]>istr[y]:
                            gh = 1
                            break

                    if (gh == 0):
                        l2=[]
                        l2.append(i1)
                        l2.append(i)
                        l2.sort()
                        if l2 not in l1:
                           # print("found::")
                            #print(l2)
                            l1.append(l2)

            else:
                continue
    print('final array')
    print(l1)
    print(len(l1))






