"""
https://leetcode.com/problems/longest-happy-string/
"""

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = ''

        while (a > 0 or b > 0 or c > 0):
            if a >= max(b, c):
                if len(ans) > 0 and ans[-1] == 'a':
                    ans = ans + 'a'
                    a = a - 1
                    if b == 0 and c == 0:
                        if a > 0:
                            ans = ans + 'a'
                            a = a - 1
                        break
                    if b >= c:
                        if b > 0:
                            ans = ans + 'b'
                            b = b - 1
                    else:
                        if c > 0:
                            ans = ans + 'c'
                            c = c - 1
                else:
                    if a > 1:
                        ans = ans + 'aa'
                        a = a - 2
                        if b == 0 and c == 0:
                            break
                        if b >= c:
                            if b > 0:
                                ans = ans + 'b'
                                b = b - 1
                        else:
                            if c > 0:
                                ans = ans + 'c'
                                c = c - 1
                    else:
                        if a == 1:
                            ans = ans + 'a'
                            a = a - 1
                        if b == 0 and c == 0:
                            break
                        if b >= c:
                            if b > 0:
                                ans = ans + 'b'
                                b = b - 1
                        else:
                            if c > 0:
                                ans = ans + 'c'
                                c = c - 1


            elif b >= max(a, c):
                if len(ans) > 0 and ans[-1] == 'b':
                    ans = ans + 'b'
                    b = b - 1
                    if a == 0 and c == 0:
                        if b > 0:
                            ans = ans + 'b'
                            b = b - 1
                        break
                    if a >= c:
                        if a > 0:
                            ans = ans + 'a'
                            a = a - 1
                    else:
                        if c > 0:
                            ans = ans + 'c'
                            c = c - 1
                else:
                    if b > 1:
                        ans = ans + 'bb'
                        b = b - 2
                        if a == 0 and c == 0:
                            break
                        if a >= c:
                            if a > 0:
                                ans = ans + 'a'
                                a = a - 1
                        else:
                            if c > 0:
                                ans = ans + 'c'
                                c = c - 1
                    else:
                        if b == 1:
                            ans = ans + 'b'
                            b = b - 1
                        if a == 0 and c == 0:
                            break
                        if a >= c:
                            if a > 0:
                                ans = ans + 'a'
                                a = a - 1
                        else:
                            if c > 0:
                                ans = ans + 'c'
                                c = c - 1


            else:
                if len(ans) > 0 and ans[-1] == 'c':
                    ans = ans + 'c'
                    c = c - 1
                    if a == 0 and b == 0:
                        if c > 0:
                            ans = ans + 'c'
                            c = c - 1
                        break
                    if a >= b:
                        if a > 0:
                            ans = ans + 'a'
                            a = a - 1
                        else:
                            if b > 0:
                                ans = ans + 'b'
                                b = b - 1
                else:
                    if c > 1:
                        ans = ans + 'cc'
                        c = c - 2
                        if a == 0 and b == 0:
                            break
                        if a >= b:
                            if a > 0:
                                ans = ans + 'a'
                                a = a - 1
                        else:
                            if b > 0:
                                ans = ans + 'b'
                                b = b - 1
                    else:
                        if c == 1:
                            ans = ans + 'c'
                            c = c - 1
                        if a == 0 and b == 0:
                            break
                        if a >= b:
                            if a > 0:
                                ans = ans + 'a'
                                a = a - 1
                        else:
                            if b > 0:
                                ans = ans + 'b'
                                b = b - 1

        return ans


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = ''

        while (a > 0 or b > 0 or c > 0):
            if a >= max(b, c):
                if len(ans) > 0 and ans[-1] == 'a':
                    ans = ans + 'a'
                    a = a - 1
                    if b == 0 and c == 0:
                        if a > 0:
                            ans = ans + 'a'
                            a = a - 1
                        break
                    if b >= c:
                        if b > 0:
                            ans = ans + 'b'
                            b = b - 1
                    else:
                        if c > 0:
                            ans = ans + 'c'
                            c = c - 1
                else:
                    if a > 1:
                        ans = ans + 'aa'
                        a = a - 2
                        if b == 0 and c == 0:
                            break
                        if b >= c:
                            if b > 0:
                                ans = ans + 'b'
                                b = b - 1
                        else:
                            if c > 0:
                                ans = ans + 'c'
                                c = c - 1
                    else:
                        if a == 1:
                            ans = ans + 'a'
                            a = a - 1
                        if b == 0 and c == 0:
                            break
                        if b >= c:
                            if b > 0:
                                ans = ans + 'b'
                                b = b - 1
                        else:
                            if c > 0:
                                ans = ans + 'c'
                                c = c - 1


            elif b >= max(a, c):
                if len(ans) > 0 and ans[-1] == 'b':
                    ans = ans + 'b'
                    b = b - 1
                    if a == 0 and c == 0:
                        if b > 0:
                            ans = ans + 'b'
                            b = b - 1
                        break
                    if a >= c:
                        if a > 0:
                            ans = ans + 'a'
                            a = a - 1
                    else:
                        if c > 0:
                            ans = ans + 'c'
                            c = c - 1
                else:
                    if b > 1:
                        ans = ans + 'bb'
                        b = b - 2
                        if a == 0 and c == 0:
                            break
                        if a >= c:
                            if a > 0:
                                ans = ans + 'a'
                                a = a - 1
                        else:
                            if c > 0:
                                ans = ans + 'c'
                                c = c - 1
                    else:
                        if b == 1:
                            ans = ans + 'b'
                            b = b - 1
                        if a == 0 and c == 0:
                            break
                        if a >= c:
                            if a > 0:
                                ans = ans + 'a'
                                a = a - 1
                        else:
                            if c > 0:
                                ans = ans + 'c'
                                c = c - 1


            else:
                if len(ans) > 0 and ans[-1] == 'c':
                    ans = ans + 'c'
                    c = c - 1
                    if a == 0 and b == 0:
                        if c > 0:
                            ans = ans + 'c'
                            c = c - 1
                        break
                    if a >= b:
                        if a > 0:
                            ans = ans + 'a'
                            a = a - 1
                        else:
                            if b > 0:
                                ans = ans + 'b'
                                b = b - 1
                else:
                    if c > 1:
                        ans = ans + 'cc'
                        c = c - 2
                        if a == 0 and b == 0:
                            break
                        if a >= b:
                            if a > 0:
                                ans = ans + 'a'
                                a = a - 1
                        else:
                            if b > 0:
                                ans = ans + 'b'
                                b = b - 1
                    else:
                        if c == 1:
                            ans = ans + 'c'
                            c = c - 1
                        if a == 0 and b == 0:
                            break
                        if a >= b:
                            if a > 0:
                                ans = ans + 'a'
                                a = a - 1
                        else:
                            if b > 0:
                                ans = ans + 'b'
                                b = b - 1

        return ans
