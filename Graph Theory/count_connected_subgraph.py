"""
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/


You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that
 there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.
"""


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        visited = []

        if len(edges) == 0:
            return n

        while (len(visited) <= n):

            if len(visited) == n:
                return ans

            # print(visited)
            # print('%%%%')
            ans += 1
            dfs = []

            for i in range(n):
                if i not in visited:
                    visited.append(i)
                    dfs.append(i)
                    break

            while (len(dfs) > 0):
                # print(dfs)
                # print('&&&')
                found = 0
                for i in range(len(edges)):
                    if edges[i][0] == dfs[-1]:
                        if edges[i][1] not in visited:
                            visited.append(edges[i][1])
                            dfs.append(edges[i][1])
                            found = 1
                            break

                    if edges[i][1] == dfs[-1]:
                        if edges[i][0] not in visited:
                            visited.append(edges[i][0])
                            dfs.append(edges[i][0])
                            found = 1
                            break

                if found != 1:
                    # print('***')
                    dfs.pop(-1)

        return ans


