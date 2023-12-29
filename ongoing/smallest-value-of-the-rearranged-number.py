class Solution:
    def smallestNumber(self, num: int) -> int: 
        str_int = str(num)
        myList = []
        flag = False
        if num < 0:
            myList = list(str_int[1:])
            flag = True
        else:
            myList = list(str_int[0:])
        if flag:
            myList.sort()
            myList.reverse()
            myList[0] = str(0-int(myList[0]))
        else: 
            myList = list(int(str_int[i]) for i in range(len(str_int)))
            myList.sort()
            if min(myList) == 0:
                for i in range(len(myList)):
                    if myList[i] != 0:
                        myList[0], myList[i] = myList[i], myList[0]
                        break
        str_num = list(str(myList[i]) for i in range(len(myList)))
        result = ''.join(str_num)
        return int(result)


