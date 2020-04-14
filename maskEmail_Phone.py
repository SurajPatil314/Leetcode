#https://leetcode.com/problems/masking-personal-information/


class Solution:

    def maskPII(self, S: str) -> str:
        def processEmail(S):
            name = S.split('@')
            f = name[0].lower()
            inter = '*****'
            result = f[0] + inter + f[-1] + '@' + name[1].lower()
            return result

        def processPhone(S):
            setter = ['(', ')', '+', '-', ' ']
            s = ''
            for i in S:
                if i not in setter:
                    s += i
            if len(s) == 10:
                sy = '***-***-'
                out = sy + s[6:]
                return out
            if len(s) > 10:
                phonesy = '+'
                for i in range(len(s[:len(s) - 10])):
                    phonesy += '*'
                sy = '-***-***-'
                out = s[len(s) - 4:]
                out = phonesy + sy + out
                return out

        if '@' in S:
            return processEmail(S)
        else:
            return processPhone(S)

