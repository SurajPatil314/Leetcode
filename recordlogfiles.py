class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        if len(logs) == 0:
            return logs

        let = {}
        dig = []

        for log in logs:
            firstword = log[0]
            my_list1 = log.split(" ")
            if my_list1[1].isdigit():
                dig.append(str(log))
            else:
                my_list = log.split(" ")
                let1 = []
                i = 0
                for i2 in range(1, len(my_list)):
                    let1.append(my_list[i2])

                value = " ".join(str(x) for x in let1)
                let[my_list[0]] = str(value)

        let2 = {}
        let2 = sorted(let.items(), key=lambda x: (x[1], x[0]))

        fans = []
        for k in let2:
            s = " "
            s = s.join(k)

            fans.append(str(s))

        fans.extend(dig)
        print(fans)

        return fans


