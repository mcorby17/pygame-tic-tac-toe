import pygame, math
from Space import Space
from pygame.locals import *

class Board:
    """
    This class is meant to represent the entire 3x3 board in a
    tic-tac-toe game. It should consist of 9 separate Space instances
    and be able to keep track of game status (win, tie) and who's turn
    it is.

    Challenges:
        1. Sizing is going to be a bitch. Or maybe not. Lotsa math!!
            - Could pass the Screen and do sizing based on that
        2. How do I know if a particular space object is clicked? Do
           I compare x,y of the click with all the dimensions?
    """

    def __init__(self, screen):
        self.screen = screen

        # Array to keep track of game status
        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]

        # Array of spaces
        self.spaces = []

        # Layout attributes (uppercase means const)
        self.LINE_THICKNESS = 15
        self.HALF_LINE_THICKNESS = self.LINE_THICKNESS / 2

        # Where to start drawing from (this would be the upper left corner of the board
        self.START = (0, 0)

        self.BLACK = (0, 0, 0)

        # get width of entire screen, subtract width of 2 lines, divide remaining by 3 for each
        # space, and
        self.spaceWidth = math.ceil((self.screen.get_width() - (2 * self.LINE_THICKNESS)) / 3)
        self.spaceHeight = math.ceil((self.screen.get_height() - (2 * self.LINE_THICKNESS)) / 3)

        self.WIDTH_DIFF = self.spaceWidth + self.LINE_THICKNESS
        self.HEIGHT_DIFF = self.spaceHeight + self.LINE_THICKNESS

        # Keep track of player
        self.player = 'X'

    def Draw(self):
        """
        Draw the board
        :return:
        """
        # Where we will start creating objects
        xy_location = list(self.START)

        # Keep track of lines made - we don't want more than 4
        linesMade = 0

        for x in range(3):
            for y in range(3):

                # Create a new space and put in list to keep track of
                # Need a new argument to know what position the space is on the board
                #   This is the (x, y) tuple
                self.spaces.append(Space(self.screen, (x, y), self.spaceHeight, self.spaceWidth,
                                         tuple(xy_location)))

                # Update xy_location list to correct position
                xy_location[0] += self.spaceWidth

                # Create the line if we haven't reached limit of 4
                if linesMade < 4 and y != 2:

                    # Move half the line thickness so there's no overlap between the line
                    # and the Space
                    xy_location[0] += self.HALF_LINE_THICKNESS

                    pygame.draw.line(self.screen, self.BLACK, xy_location,
                                     (xy_location[0], self.screen.get_height()),
                                     self.LINE_THICKNESS)

                    linesMade += 1
                    xy_location[0] += self.HALF_LINE_THICKNESS

                else:
                    # If we already have all lines, just move by the number of pixels the
                    # existing line takes up
                    xy_location[0] += self.LINE_THICKNESS

            # Reset x value to 0
            xy_location[0] = 0

            # incriment y value
            xy_location[1] += self.spaceHeight

            # Draw line if all lines haven't been drawn
            if linesMade < 5:
                xy_location[1] += self.HALF_LINE_THICKNESS
                pygame.draw.line(self.screen, self.BLACK, xy_location,
                                 (self.screen.get_width(), xy_location[1]),
                                 self.LINE_THICKNESS)
                linesMade += 1
                xy_location[1] += self.HALF_LINE_THICKNESS

    def TogglePlayer(self):
        """
        Toggle the current player's turn. Should be used when the previous
        player has placed their piece
        :return:
        """
        if self.player == 'X':
            self.player = 'O'
            return
        if self.player == 'O':
            self.player = 'X'
            return

    def UpdateBoardStatus(self, space):
        """
        Update board array with the status of each Space object for reference later
        so we can see if a player has won the game or if the game ended in a tie
        :return:
        """
        self.board[space.boardPosition[0]][space.boardPosition[1]] = space.status


    def HandleClick(self, mousePosition):
        """
        React to use mouse click. Essentially pass the mouse position to the
        ShowPiece() method for each Space object.

        :param mousePosition:
        :return:
        """
        for space in self.spaces:
            if space.ShowPiece(self.player, mousePosition):
                self.UpdateBoardStatus(space)
                self.CheckGameOver()
                self.TogglePlayer()

    def CheckGameOver(self):
        """
        Determine if either a player has won or a tie has occurred by scanning through
        this object's board array for win conditions. If there are no "None" spaces left,
        the game has ended in a tie.
        :return:
        """
        # Tie testing will check entire self.board array for a "None" value. If one
        # is found then tie will be set to false. Upon a new game over check, this var
        # will be reset to True.
        # Note: Apparently I can't see this var inside of a for loop? Wtf?
        #tie = True

        for row in range(3):
            if self.board[row][0] == self.player and self.board[row][1] == self.player \
            and self.board[row][2] == self.player:
                print("Player " + self.player + " has won!")

        for col in range(3):
            if self.board[0][col] == self.player and self.board[1][col] == self.player \
            and self.board[2][col] == self.player:
                print("Player " + self.player + " has won!")

        if self.board[0][0] == self.player and self.board[1][1] == self.player \
        and self.board[2][2] == self.player:
            print("Player " + self.player + " has won!")

        if self.board[2][0] == self.player and self.board[1][1] == self.player \
        and self.board[0][2] == self.player:
            print("Player " + self.player + " has won!")

        # Check for tie by seeing if there are no "None" values left
        #for row in range(3):
        #    for col in range(3):
        #        if self.board[row][col] is None:
        #            tie = False
        #            break