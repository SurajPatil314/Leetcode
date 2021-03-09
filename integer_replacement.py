"""
https://leetcode.com/problems/integer-replacement/submissions/

Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.



"""


class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2

        while (n != 1):
            if n == 3:
                count += 2
                break
            if n % 2 == 1:
                n1 = n + 1
                n2 = n - 1

                a = 4
                while True:
                    if n1 % a == 0 and n2 % a == 0:
                        a = a * 2
                    else:
                        if n1 % a == 0:
                            n = n1
                            break
                        else:
                            n = n2
                            break
                count += 1
            else:
                n = int(n / 2)
                count += 1

        return count


