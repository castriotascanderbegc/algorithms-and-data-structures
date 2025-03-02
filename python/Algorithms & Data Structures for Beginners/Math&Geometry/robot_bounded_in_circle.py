"""
    Q: Robot Bounded in Circle

    On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

    The north direction is the positive direction of the y-axis.
    The south direction is the negative direction of the y-axis.
    The east direction is the positive direction of the x-axis.
    The west direction is the negative direction of the x-axis.
    The robot can receive one of three instructions:

    "G": go straight 1 unit.
    "L": turn 90 degrees to the left (i.e., anti-clockwise direction).
    "R": turn 90 degrees to the right (i.e., clockwise direction).
    The robot performs the instructions given in order, and repeats them forever.

    Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

"""
class Solution:
    """
        The idea here is that our Robot will be in a loop if either of two conditions are true:
            1. Position does not change, i.e. final position will still be (0, 0)
            2. Directiond does change, i.e. final direction will be different from original (0,1) direction
    """
    # Time Complexity: T(n) = O(n)
    # Space Complexity: S(n) = O(1)
    def isRobotBounded(self, instructions: str) -> bool:
        # initialize our direction
        dirX, dirY = 0, 1
        # initialize our position
        posX, posY = 0, 0

        # go over the instructions
        for i in instructions:
            # direction == GO
            if i == 'G':
                posX, posY = posX + dirX, posY + dirY
            
            # direction == TURN LEFT
            elif i == 'L':
                dirX, dirY = -1 * dirY, dirX
            
            # direction == TURN RIGHT
            else:
                dirX, dirY = dirY, -1 * dirX
        
        # either our position did not change or our direction did change
        return (posX, posY) == (0, 0) or (dirX, dirY) != (0, 1)


        