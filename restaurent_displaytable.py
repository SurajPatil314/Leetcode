"""
https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

prototype class to create a page/list for restaurent managers to manage all restaurent orders. 

"""


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:

        tablefr = []
        tablefr.append("Table")
        foodl = []  #list to save ordered food items
        d = defaultdict(list)
        ans = []  #to save final list

        for i in orders:
            if i[2] not in foodl:
                foodl.append(i[2])
            d[i[1]].append(i[2])

        foodl.sort()   #sort food alphabetically
        tablefr.extend(foodl)

        # ans.append(tablefr)
        d1 = {}
        for i in foodl:
            d1[i] = 0
        for i, j in d.items():
            temp = []
            temp.append(i)

            for j1 in j:
                if j1 in d1:
                    d1[j1] = d1.get(j1) + 1
            # print(d1)

            for i11, j11 in d1.items():
                # print(j11)
                temp.append(str(j11))
                d1[i11] = 0

            # print(temp)
            ans.append(temp)
            # print('$$$$')
            # print(d1)

        ans = sorted(ans, key=lambda x: int(x[0]))   #sort all table orders by table numbers
        ans.insert(0, tablefr)

        return ans




