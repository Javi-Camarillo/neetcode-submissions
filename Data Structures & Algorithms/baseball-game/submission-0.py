class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sum_val = 0
        record = []
        if not operations:
            return 0
        for op in operations:
            if op == '+':
                add = record[-1] + record[-2]
                record.append(add)
            elif op == 'D':
                double = 2 * record[-1]
                record.append(double)
            elif op == 'C':
                record.pop()
            else:
                num = int(op)
                record.append(num)
        return sum(record)