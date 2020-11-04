"""
https://leetcode.com/problems/keys-and-rooms/

There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have
 some keys to access the next room.

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where
N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0).

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.
"""


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = []
        keys = []

        num1 = 0

        if len(rooms[0]) == 0 and len(rooms) < 2:
            return True

        if len(rooms[0]) == 0 and len(rooms) > 1:
            return False
        else:
            keys.extend(rooms[0])
            visited.append(0)

        while len(keys) > 0:
            temp = keys.pop()
            if temp not in visited:
                visited.append(temp)
                for i in range(len(rooms[temp])):
                    if rooms[temp][i] not in keys:
                        keys.append(rooms[temp][i])

        if len(visited) == len(rooms):
            return True
        else:
            return False

