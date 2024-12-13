class Solution:
    """
        The idea is: 
            We will use a stack to keep track of open/close brackets
            We scan through the input string s, and
                if we see an open bracket then we can push in the stack and continue
                if we see a close bracket then:
                    if stack is empty or the current close bracket does not have a corresponding open bracket at the top of the stack, we have a not valid string
                    else we pop from the stack and continue
            At this point, either we already returned or if we scanned the entire input string s, we can simply check
            if our stack is empty or not. If empty, our string is valid. Differently, if stack is not empty we have a not valid string.
    """
    def myBruteForceSolution(self, s: str) -> bool:
        # s is a string of open/closing brackets
        # scan through the input string s
        # keep a stack to monitor open and closing brackets
        stack = []
        for bracket in s:
            # if it is an open bracket let's push in the stack
            if bracket == '(' or bracket == '[' or bracket == '{':
                stack.append(bracket)
            else:
                # did we push something in the stack already?
                # edge case where we are starting with a string with already closing brackets
                if not stack:
                    return False
                # if it a closing bracket, let's pop from the stack
                # if we popped, we need to make sure LIFO is valid, Last IN == First OUT
                firstOut = stack.pop()
                if firstOut == '(' and bracket != ')':
                    return False
                if firstOut == '[' and bracket != ']':
                    return False
                if firstOut == '{' and bracket != '}':
                    return False      
        return not stack
    
    def isValid(self, s: str) -> bool:
        """
            The idea here is to keep a HashMap to store our mapping to simplify code:
            close bracket --> open bracket mapping
        """

        Map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for bracket in s:
            if bracket not in Map:
                stack.append(bracket)
                continue
            if not stack or stack[-1] != Map[bracket]:
                return False
            stack.pop()
        
        return not stack



if __name__ == "__main__":
    sol = Solution()
    s = "([{}])"

    print("Test 1")
    print("s: ", s)

    print("Output Test 1: ", sol.isValid(s=s))

    print("-------------------------")

    s = "[(])"
    print("Test 2")
    print("s: ", s)

    print("Output Test 2: ", sol.isValid(s=s))

    print("-------------------------")

    s = "[]"
    print("Test 3")
    print("s: ", s)

    print("Output Test 3: ", sol.isValid(s=s))