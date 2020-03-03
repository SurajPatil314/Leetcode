"""
A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring
stops where distance[i] is the distance between the stops number i and (i + 1) % n.

The bus goes along both directions i.e. clockwise and counterclockwise.

Return the shortest distance between the given start and destination stops.


"""

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        ans = 0
        ans1 = 0
        q = 0
        count = 0
        i1 = 0

        if start > destination:
            q11 = destination
            destination = start
            start = q11

        for i in range(len(distance)):
            if count == destination:
                break

            if count == start:
                i1 = 1

            if i1 == 1:
                ans = ans + distance[i]

            if i1 == 0:
                q = q + distance[i]

            count += 1

        distance.reverse()
        destination = len(distance) - destination
        count = 0

        for i in range(len(distance)):
            if count == destination:
                break
            ans1 = ans1 + distance[i]

            count += 1

        if start != 0:
            ans1 = ans1 + q
        print(ans)
        if ans1 > ans:
            return ans
        else:
            return ans1

