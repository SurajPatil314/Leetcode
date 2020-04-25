"""
https://leetcode.com/problems/all-paths-from-source-to-target/


Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.
"""


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        ans = []

        allpath = []
        start = [0]
        allpath.append(start)

        finalnode = len(graph) - 1

        while len(allpath) > 0:
            qw = allpath.pop()

            fnode = qw[-1]

            if fnode == finalnode:
                ans.append(qw)

            else:
                for i in graph[fnode]:
                    nnlist = []
                    nnl = []
                    nnl.extend(qw)
                    nnl.append(i)
                    allpath.append(nnl)

        return ans






