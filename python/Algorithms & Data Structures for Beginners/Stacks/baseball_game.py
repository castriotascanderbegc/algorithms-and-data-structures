class Solution:

    """
        Below solutions both have following space/time complexities.
        Time Complexity: O(n)
        Space Complexity: O(n)

        Sol.1 Make assumptions
        Sol.2 Take into considerations edge cases
    
    """


    def calPoints(self, operations: list[str]) -> int:
        """
            operations is a list of string
            our record is a stack --> dynamic array
            our total record is sum of the stack, no need to keep track. Can simply return the sum(record)

            Below solution assumes the following:
                - for a "+" operation there will always be at least two records in the score
                - for a "D" or "C" operation there will always be at least one record in the score 

        """
        record = []
        for op in operations: 
            if op == 'C':
                record.pop()
            elif op == 'D':
                record.append(record[-1] * 2) 
            elif op == '+':
                record.append(record[-1] + record[-2])
            else:
                record.append(int(op))
        return sum(record)
    

    def keepScore(self, operations: list[str]) -> int:

        ### no assumptions here

        record = []
        for op in operations: 
            if op == 'C' and len(record) >= 1:
                record.pop()
            elif op == 'D' and len(record) >= 1:
                record.append(record[-1] * 2)
            elif op == '+' and len(record) >= 2:
                record.append(record[-1] + record[-2])
            else:
                record.append(int(op))

        return sum(record) 
    

if __name__ == "__main__":
    sol = Solution()
    ops = ["5","2","C","D","+"]

    print("Test 1")
    print("nums: ", ops)

    print("Output Test 1: ", sol.calPoints(operations=ops))

    print("-------------------------")

    ops = ["5","-2","4","C","D","9","+","+"]
    print("Test 2")
    print("nums: ", ops)

    print("Output Test 2: ", sol.keepScore(operations=ops))
