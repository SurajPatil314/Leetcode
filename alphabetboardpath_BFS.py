'''
https://leetcode.com/problems/alphabet-board-path/

We may make the following moves:

'U' moves our position up one row, if the position exists on the board;
'D' moves our position down one row, if the position exists on the board;
'L' moves our position left one column, if the position exists on the board;
'R' moves our position right one column, if the position exists on the board;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.
'''
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z1111"]
        ans = ''
        outerstack = []
        target1 = []

        for i3 in target:
            target1.append(i3
                           )
        outerstack.append([0, 0])
        count = 0
        previ = 0
        prevj = 0

        while len(outerstack) > 0 and len(target1) > 0:
            # print(target)
            # print(outerstack)

            running = outerstack[0]
            i = running[0]
            j = running[1]

            # found answer
            if board[i][j] == target1[0]:
                # print('found::%s'%target1[0])
                # print('i::%d::j::%d'%(i,j))
                # print('new previ::%d::prevj::%d'%(previ,prevj))

                del target1[0]

                if i == 5:  # special 'z' case
                    if prevj == 0:
                        if previ != i:
                            iinc = i - previ
                            for i2 in range(iinc):
                                ans = ans + 'D'
                    else:
                        iinc = i - previ
                        for i2 in range(iinc - 1):
                            ans = ans + 'D'
                        jinc = prevj - j
                        for i2 in range(jinc):
                            ans = ans + 'L'

                        ans = ans + 'D'

                else:
                    if previ > i:
                        iinc = previ - i
                        for i2 in range(iinc):
                            ans = ans + 'U'
                    if previ < i:
                        iinc = i - previ
                        for i2 in range(iinc):
                            ans = ans + 'D'
                    if prevj > j:
                        jinc = prevj - j
                        for i2 in range(jinc):
                            ans = ans + 'L'
                    if prevj < j:
                        jinc = j - prevj
                        for i2 in range(jinc):
                            ans = ans + 'R'

                ans = ans + '!'  # append a the end
                outerstack = []
                outerstack.append([i, j])

                previ = i
                prevj = j
                # print('new previ::%d::prevj::%d'%(previ,prevj))





            # BFS call
            else:
                if running[0] > 0:
                    outerstack.append([i - 1, j])
                if running[0] > 0 and running[1] > 0:
                    outerstack.append([i - 1, j - 1])
                if running[0] < len(board) - 1:
                    outerstack.append([i + 1, j])
                if running[0] > (len(board) - 1) and running[1] < len(board[0]) - 1:
                    outerstack.append([i + 1, j + 1])
                if running[1] < len(board[0]) - 1:
                    outerstack.append([i, j + 1])
                if running[1] > 0:
                    outerstack.append([i, j - 1])

                del outerstack[0]

        return ans


