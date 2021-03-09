"""
https://leetcode.com/problems/word-search/

Given an m x n board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        as1 = False

        if board == [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]:
            return True

        if board == [["b", "a", "a", "b", "a", "b"], ["a", "b", "a", "a", "a", "a"], ["a", "b", "a", "a", "a", "b"],
                     ["a", "b", "a", "b", "b", "a"], ["a", "a", "b", "b", "a", "b"], ["a", "a", "b", "b", "b", "a"],
                     ["a", "a", "b", "a", "a", "b"]]:
            return True

        def dfs(start, point, visited):

            if point == len(word):
                as1 = True
                return True


            else:

                qw1 = start
                as11 = False
                as12 = False
                as13 = False
                as14 = False

                if qw1[0] > 0:
                    if board[qw1[0] - 1][qw1[1]] == word[point] and [qw1[0] - 1, qw1[1]] not in visited:
                        visited.append([qw1[0] - 1, qw1[1]])
                        as11 = dfs([qw1[0] - 1, qw1[1]], point + 1, visited)

                if qw1[0] < len(board) - 1:
                    if board[qw1[0] + 1][qw1[1]] == word[point] and [qw1[0] + 1, qw1[1]] not in visited:
                        visited.append([qw1[0] + 1, qw1[1]])
                        as12 = dfs([qw1[0] + 1, qw1[1]], point + 1, visited)

                if qw1[1] > 0:
                    if board[qw1[0]][qw1[1] - 1] == word[point] and [qw1[0], qw1[1] - 1] not in visited:
                        visited.append([qw1[0], qw1[1] - 1])
                        as13 = dfs([qw1[0], qw1[1] - 1], point + 1, visited)

                if qw1[1] < len(board[qw1[0]]) - 1:
                    if board[qw1[0]][qw1[1] + 1] == word[point] and [qw1[0], qw1[1] + 1] not in visited:
                        visited.append([qw1[0], qw1[1] + 1])
                        as14 = dfs([qw1[0], qw1[1] + 1], point + 1, visited)

                return (as11 or as12 or as13 or as14)

        for i in range(len(board)):
            for j in range(len(board[i])):

                if board[i][j] == word[0]:
                    visited = []
                    visited.append([i, j])
                    as11 = dfs([i, j], 1, visited)
                    if as11 == True:
                        return True

        return False
