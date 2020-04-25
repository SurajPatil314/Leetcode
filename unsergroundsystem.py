"""
https://leetcode.com/problems/design-underground-system/
"""

class UndergroundSystem:
    alltravel = []

    def __init__(self):
        self.alltravel = []

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        ins = []
        ins.append(id)
        ins.append(stationName)
        ins.append(t)
        ins.append(-1)

        self.alltravel.append(ins)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        ins = []
        ins.append(id)
        ins.append(stationName)
        ins.append(-1)
        ins.append(t)

        self.alltravel.append(ins)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        ans = 0.0

        startq = []
        endq = []

        for i in self.alltravel:
            if i[1] == startStation and i[2] != -1:
                startq.append(i)

            if i[1] == endStation and i[3] != -1:
                endq.append(i)

        print('!!')
        print(startq)
        print('@@')
        print(endq)
        count = 0

        i = 0
        j = 0

        while (i < len(startq)):
            j = 0
            while (j < len(endq)):
                if endq[j][0] == startq[i][0]:
                    ans = ans + endq[j][3] - startq[i][2]
                    count += 1
                    break
                else:
                    j += 1

            i += 1
        print('$$$')
        print(ans)
        print(count)
        return ans / count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)