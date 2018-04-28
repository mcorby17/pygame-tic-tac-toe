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

    def Draw(self):
        """
        Draw the board
        :return:
        """
        # Where we will start creating objects
        xy_location = list(self.START)

        # Keep track of lines made - we don't want more than 4
        linesMade = 0

        for y in range(3):
            for x in range(3):

                # Create a new space and put in list to keep track of
                self.spaces.append(Space(self.screen, self.spaceHeight, self.spaceWidth,
                                         tuple(xy_location)))

                # Update xy_location list to correct position
                xy_location[0] += self.spaceWidth

                # Create the line if we haven't reached limit of 4
                if linesMade < 4 and x != 2:

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