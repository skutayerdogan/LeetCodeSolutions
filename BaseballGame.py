class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []
        lastNum = 0
        sum = 0
        for operation in operations:
            if operation == 'C':
                lastNum = record.pop()
            elif operation == 'D':
                sum = record[-1] * 2
                record.append(sum)
            elif operation == '+':
                try:
                    sum = record[-1] + record[-2]
                except:
                    sum = record[-1] * lastNum
                record.append(sum)
            else:
                number = int(operation)
                record.append(number)
        totalSum = 0
        for num in record:
            totalSum += num
        return totalSum
sol = Solution()
sol.calPoints(["5","-2","4","C","D","9","+","+"])