"""
    Connect Four is a popular game played on a 7x6 grid. 
    Two players take turns dropping colored discs into the grid. 
    The first player to get four discs in a row (vertically, horizontally or diagonally) wins.

    
    Basics
        The game will be played by only two players, player vs player
        The game board should be of variable dimensions
        The target is to connect N discs in a row (vertically, horizontally or diagonally)
            N is a variable (e.g. connect 4, 5, 6, etc)
        There should be a score tracking system
        After a player reaches the target score, they are the winner
"""


# we will use an enum for the GridPosition
import enum
class GridPosition(enum.Enum): 
    EMPTY   = 0,    # Empty cell
    RED     = 1,    # Player 1
    YELLOW  = 2     # Player 2

# The Grid will maitain the state of the 2D board and all of the pieces
# It will also check for a win condition
class Grid:
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._grid = None
        self.initGrid()

    # we initialize the board here
    def initGrid(self):
        self._grid = [[GridPosition.EMPTY for _ in range(self._columns)] for _ in range(self._rows)]
    
    # get the grid
    def getGrid(self):
        return self._grid
    
    # get the columns
    def getColumnsCount(self):
        return self._columns
    
    # make a move
    def placePiece(self, column, piece):
        if column < 0 or column >= self._columns:
            raise ValueError("Invalid Column")
        if piece == GridPosition.EMPTY:
            raise ValueError("Invald Piece")
        for row in range(self._rows - 1, -1, -1):
            if self._grid[row][column] == GridPosition.EMPTY:
                self._grid[row][column] = piece
                return row
    
    # check win condition - N connected (horizontally, vertically, diagonally)
    def checkNConnected(self, connectN, row, col, piece):
        count = 0

        # check horizontal
        for c in range(self._columns):
            if self._grid[row][c] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True
        
        # check vertical
        count = 0
        for r in range(self._rows):
            if self._grid[r][col] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True
        
        # check diagonal
        count = 0
        for r in range(self._rows):
            c = row + col - r
            if c >= 0 and c < self._columns and self._grid[r][c] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True

        # check anti-diagonal
        count = 0
        for r in range(self._rows):
            c = col - row + r
            if c >= 0 and c < self._columns and self._grid[r][c] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True 
        
        return False
    

# A Player class is only needed to encapsulate player's info, especially the piece color
class Player:
    def __init__(self, name, pieceColor):
        self._name = name
        self._pieceColor = pieceColor

    def getName(self):
        return self._name

    def getPieceColor(self):
        return self._pieceColor
    

# The Game class is used to play the game
# will keep track of the players, score, grid
# Run the game loop
class Game:
    def __init__(self, grid, connectN, targetScore):
        self._grid = grid
        self._connectN = connectN
        self._targetScore = targetScore

        self._players = [
            Player("Player1", GridPosition.RED),
            Player("Player2", GridPosition.YELLOW)
        ]

        self._score = {}
        for player in self._players:
            self._score[player.getName()] = 0

    def printBoard(self):
        print("Board:\n")
        grid = self._grid.getGrid()
        for i in range(len(grid)):
            row = ''
            for piece in grid[i]:
                if piece == GridPosition.EMPTY:
                    row += '0 '
                elif piece == GridPosition.RED:
                    row += 'R '
                elif piece == GridPosition.YELLOW:
                    row += 'Y '
            print(row)
        print('')

    def playMove(self, player):
        self.printBoard()
        print(f"{player.getName()}'s turn")
        colCnt = self._grid.getColumnsCount()
        moveColumn = int(input(f"Enter column between {0} and {colCnt - 1} to add a piece: "))
        moveRow = self._grid.placePiece(moveColumn, player.getPieceColor())
        return (moveRow, moveColumn)
    
    def playRound(self):
        while True:
            for player in self._players:
                row, col = self.playMove(player)
                pieceColor = player.getPieceColor()
                if self._grid.checkNConnected(self._connectN, row, col, pieceColor):
                    self._score[player.getName()] += 1
                    return player
    
    def play(self):
        maxScore = 0
        winner = None
        while maxScore < self._targetScore:
            winner = self.playRound()
            print(f"{winner.getName()} won the round")
            maxScore = max(self._score[winner.getName()], maxScore)

            self._grid.initGrid()    # reset the grid
        print(f"{winner.getName()} won the game")

    
if __name__ == "__main__":
    grid = Grid(6, 7)
    game = Game(grid, 4, 2)
    game.play()
                
