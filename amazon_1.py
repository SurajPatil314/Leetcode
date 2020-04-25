

def fn(que):
    word = {}

    num = []

    for i in que:
        i1 = i.split(' ')
        if i1[1].isdigit():
            num.append(i)
        else:
            word[i1[0]] = i1[1:]

    if len(word) == 0:
        return num

    word1 = sorted(word.items(), key=lambda x: (x[1], x[0]))
    #sorted(word.items(), lambda a, b: b[1] - a[1] or a[0] - b[0])

    print(word1)
    ans = []

    for k in word1:
        v1 = ''
        i2 = 0
        for i1 in k[1]:
            if i2 == 0:
                v1 = i1
                i2+=1
            else:
                v1 = v1+' '+i1
        kv = k[0] + ' ' +v1
        ans.append(kv)

    ans.extend(num)

    print(ans)


def main():
    que = []
    que.append('a1 9 2 3 1')
    que.append('gl act car')
    que.append('zo4 4 7')
    que.append('abl off key dog')
    que.append('bcl off key dog')
    que.append('za8 5 7')
    que.append('a8 act zoo')
    fn(que)

if __name__ == '__main__':
    main()