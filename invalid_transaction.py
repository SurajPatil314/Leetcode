"""
https://leetcode.com/problems/invalid-transactions/


A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.

Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.
"""

from collections import defaultdict


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ans = set()
        dis = defaultdict(list)

        for i in transactions:

            i1 = i.split(',')

            if int(i1[2]) > 1000:
                ans.add(i)
            ke = i1.pop(0)
            dis[ke].append(i1)

        for k, v in dis.items():

            if len(v) > 1:
                i = 0
                j = 1
                while (i < len(v)):
                    j = i + 1
                    temp = []
                    while (j < len(v)):
                        w1 = int(v[i][0])
                        w2 = int(v[j][0])
                        if (abs(w1 - w2) <= 60) and (v[i][2] != v[j][2]):
                            if v[i] not in temp:
                                temp.append(v[i])
                                ans1 = k + ',' + ','.join(v[i])
                                ans.add(ans1)
                            if v[j] not in temp:
                                temp.append(v[j])
                                ans1 = k + ',' + ','.join(v[j])
                                ans.add(ans1)
                        j += 1
                    i += 1

        return ans




