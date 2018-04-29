import pygame, sys
from Space import Space
from Board import Board
from pygame.locals import *

pygame.init()

# TODO: Move into board class, if possible
SCREEN = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Tic Tac Toe")
SCREEN.fill((255, 255, 255))

# Test Board class
board = Board(SCREEN)
board.Draw()

# Test drawing a line
#                         Color      Start   End        Thicccness
#pygame.draw.line(SCREEN, (0, 0, 0), (1.2, 2.2), (500, 500), 15)

# keep around to note how to get the center of something
#screenRect = SCREEN.get_rect()
#screenCenter = screenRect.center

# Keep track of player turns
# player = 'O'

# Create a square, fill it with a color and blit it to the screen
# Interesting, don't have to blit it
#testSpace = Space(SCREEN, location=(50, 50))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            # Need a board.HandleClick function of some sort
            board.HandleClick(pygame.mouse.get_pos())

            #if testSpace.ShowPiece(player, pygame.mouse.get_pos()):
            #    player = TogglePlayer(player)

        #SCREEN.blit(mySquare, (0, 0))

        #SCREEN.blit(O, (0, 0))
        #SCREEN.blit(X, X_Rect)
        pygame.display.flip()