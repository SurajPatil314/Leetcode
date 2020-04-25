def fn(numfeature,topfeature,possiblefeature,numfreq,freq):
    mapans = {}
    for i in freq:
        templ = []
        temp2 = i.split(' ')
        for j in temp2:
            if j in possiblefeature:
                if j not in templ:
                    templ.append(j)
                    if j in mapans:
                        mapans[j] = mapans.get(j) + 1
                    else:
                        mapans[j] = 1
    print(mapans)
    word1 = sorted(mapans.items(), key=lambda x: (x[1], x[0]), reverse=True)

    ans = []

    print(word1)
    if numfeature<= topfeature:
        for i1 in word1:
            ans.append(i1[0])

        print(ans)

    else:
        for i1 in range(topfeature):
            ans.append(word1[i1][0])

        print(ans)




def main():
    numfeature = 6
    topfeature = 2
    possiblefeature = ['storage', 'battary', 'hover','alexa','waterproof','solar']
    numfreq = 7
    freq = ['sas asds battary sdf s','wish my kindle dsad sadsad','waterproof ewdw ewd' ,'i rad bath and awd kindle','waterproof adsd sd asds '
                                                                                               'battary fsd df','kindlw dsf dsfsdf',
            'waterproof das waterprrof', 'fes dsfdsf  kindle sfds dsfdsf not in use', 'df dsf dfkin kindle fsdf fd sun via  power', 'sfsfd dsf hover dsf dsf df solar']

    fn(numfeature,topfeature,possiblefeature,numfreq,freq)

if __name__ == '__main__':
    main()