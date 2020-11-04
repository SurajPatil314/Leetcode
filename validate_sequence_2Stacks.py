"""
https://leetcode.com/problems/validate-stack-sequences/


Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.
"""


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        i = 0
        j = 0

        visited = []

        if len(pushed) != len(popped):
            return False

        while j < len(popped):

            if i >= len(pushed):
                i = len(pushed) - 1
                if len(visited) > 0:
                    if visited[-1] == popped[j]:
                        pushed.remove(visited[-1])
                        del visited[-1]
                        del popped[j]
                else:
                    if pushed[i] == popped[j]:
                        del pushed[i]
                        del popped[j]
                    else:
                        return False
            else:
                if len(visited) > 0:
                    if visited[-1] == popped[j]:
                        pushed.remove(visited[-1])
                        del visited[-1]
                        del popped[j]
                        i = i - 1

                    else:
                        if pushed[i] == popped[j]:
                            del pushed[i]
                            del popped[j]

                        else:
                            if popped[j] in visited:
                                return False
                            else:
                                visited.append(pushed[i])
                                i += 1
                else:
                    if pushed[i] == popped[j]:
                        del pushed[i]
                        del popped[j]

                    else:
                        if popped[j] in visited:
                            return False
                        else:
                            visited.append(pushed[i])
                            i += 1

        if len(pushed) == 0 and len(popped) == 0:
            return True
        else:
            return False


