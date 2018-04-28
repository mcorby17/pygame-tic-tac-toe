import pygame
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
        # Array to keep track of game status
        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]

        # Array of spaces
        self.spaces = []

        # Divide width by three, divide height by three and subtract some
        # space for lines
        spaceWidth = screen.get_width() / 3
        spaceHeight = screen.get_height() / 3