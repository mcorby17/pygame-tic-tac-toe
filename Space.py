import pygame
from pygame.locals import *

class Space:
    """
    This class represents one of 9 spaces in a tic tac toe game

    It should be able to:
        1. Have a status (empty, what piece is in it)
        2. Show the particular piece inside of it relative to the size
           of the Space instance

    Notes:
        How am I going to align each Space? Constructor might need
        arguments as to where the Space should be blitted
    """
    def __init__(self, screen, height=100, width=100, location=(0, 0)):
        self.screen = screen
        self.height = height
        self.width = width
        self.location = location
        self.status = None
        self.X = pygame.image.load("X.png")
        self.X = pygame.transform.scale(self.X, (self.width, self.height))
        self.O = pygame.image.load("o.png")
        self.O = pygame.transform.scale(self.O, (self.width, self.height))
        self.rect = Rect(location + (self.height, self.width))
        # This works for centering, might need a better mechanism
        # since I can't change the rect once it's drawn
        #self.rect.center = (250, 250)

        # Automatically draw self
        # NOTE: Temporarily using blue to see where the spaces are
        pygame.draw.rect(self.screen, (0, 0, 255), self.rect)

    def ShowPiece(self, player, mousePos):
        """
        Show the player's piece if the rectangle has been clicked
        and update the status of the Space
        :return: Void
        """
        # Do nothing if the mousePos is not in this rect
        if not self.rect.collidepoint(mousePos):
            return False

        # Do nothing if there's already a piece here
        if self.status is not None:
            return False

        if player == 'X':
            self.screen.blit(self.X, self.rect)
        else:
            self.screen.blit(self.O, self.rect)

        self.status = player

        return True