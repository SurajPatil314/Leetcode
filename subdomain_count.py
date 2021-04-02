"""
https://leetcode.com/problems/subdomain-visit-count/

A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the
 next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like
 "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a
 space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format
 as the input, and in any order), that explicitly counts the number of visits to each subdomain.
"""


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        qw = defaultdict(int)

        for i in range(len(cpdomains)):
            qw1 = cpdomains[i].split(' ')

            val = int(qw1[0])

            for j in range(len(qw1[1])):
                if j == 0:
                    qw[qw1[1]] = qw[qw1[1]] + val
                else:
                    if qw1[1][j] == '.':
                        qw[qw1[1][j + 1:]] = qw[qw1[1][j + 1:]] + val

        ans = []

        for i, j in qw.items():
            ans1 = str(j) + ' ' + i
            ans.append(ans1)

        print(ans)

        return ans



