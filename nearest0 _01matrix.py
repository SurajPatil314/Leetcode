'''
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
'''
class Solution:

    def bfs1(self ,matrix, bfslist: List[List[int]], score1) - >int:
        newbf s= []
        score1 1 =score1
        for i in bfslist:

            if i[0 ] - 1> =0:
                if matrix[i[0 ] -1][i[1]] == 0:
                    return score11
                else:
                    q p =[]
                    qp.append(i[0 ] -1)
                    qp.append(i[1])
                    newbfs.append(qp)

            if i[0 ] + 1 <len(matrix):
                if matrix[i[0 ] +1][i[1]] == 0:
                    return score11
                else:
                    q p =[]
                    qp.append(i[0 ] +1)
                    qp.append(i[1])
                    newbfs.append(qp)

            if i[1 ] - 1> =0:
                if matrix[i[0]][i[1 ] -1] == 0:
                    return score11
                else:
                    q p =[]
                    qp.append(i[0])
                    qp.append(i[1 ] -1)
                    newbfs.append(qp)

            if i[1 ] + 1 <len(matrix[0]):
                if matrix[i[0]][i[1 ] +1] == 0:
                    return score11
                else:
                    q p =[]
                    qp.append(i[0])
                    qp.append(i[1 ] +1)
                    newbfs.append(qp)




        score1 1= score1 1 +1
        return self.bfs1(matrix, newbfs, score11)


    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        oute r= []
        inne r= []
        bfslis t =[]
        o 1 =0
        o 2 =0
        for i in matrix:
            for i1 in i:
                if i1 == 0:
                    inner.append(0)
                    scor e =0
                else:
                    p u =[]
                    pu.append(o1)
                    pu.append(o2)
                    score 1 =0
                    score 1 =score 1 +1
                    bfslist.append(pu)
                    score2 1 =0
                    score21 = self.bfs1(matrix, bfslist, score1)
                    print(score21)
                    inner.append(score21)
                o 2 =o 2 +1
                bfslist = []


            outer.append(inner)
            inne r =[]

            o 1= o 1 +1
            o 2 =0

        return outer

