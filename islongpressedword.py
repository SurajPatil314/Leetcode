
"""
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed,
 and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with
 some characters (possibly none) being long pressed.
"""
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        if not name or not typed:
            return False

        count = 0
        count1 = 0

        while (count < len(name)):
            if count1 >= len(typed):
                return False
            if name[count] != typed[count1]:
                return False
            else:
                if count + 1 >= len(name):
                    break
                inc = 0
                while True:
                    if count + 1 < len(name):
                        if name[count + 1] == name[count]:
                            inc = inc + 1
                            count = count + 1
                        else:
                            break
                    else:
                        break

                while True:
                    if (count1 + 1) < len(typed):
                        if typed[count1 + 1] == typed[count1]:
                            if inc > 0:
                                inc = inc - 1

                            count1 = count1 + 1
                        else:
                            break
                    else:
                        break

                if inc > 0:
                    return False
                count = count + 1
                count1 = count1 + 1

        return True


