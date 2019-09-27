def binarysearch(eleset, l, r, number):
    if r>=l:
        m = int(l + (r - l)/2)
        print(m)
        if(eleset[m]==number):
            print("found element at index::"+str(m))

        elif (eleset[m]>number):
            binarysearch(eleset,l,m-1,number)
        else:
            binarysearch(eleset,m+1,r,number)
    else:
        print('element not found')

if __name__ == "__main__" :
    eleset=[]
    numberofelement=  int(input("enter number of elements::"))
    i=0
    while(i<numberofelement):
        number=int(input("enter element::"))
        eleset.append(number)
        i=i+1



    eleset.sort()
    print(eleset)
    ser= int(input("enter element for search::"))
    binarysearch(eleset,0,numberofelement-1,ser)