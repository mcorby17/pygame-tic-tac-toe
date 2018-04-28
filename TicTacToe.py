import pygame, sys
from Space import Space
from pygame.locals import *

pygame.init()

# Temporary player toggle function - should move into
# Board class
def TogglePlayer(player):
    if player == 'X':
        return 'O'
    if player == 'O':
        return 'X'

# Initialize screen
SCREEN = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Tic Tac Toe")
SCREEN.fill((255, 255, 255))

# keep around to note how to get the center of something
#screenRect = SCREEN.get_rect()
#screenCenter = screenRect.center

# Keep track of player turns
player = 'O'

# Create a square, fill it with a color and blit it to the screen
# Interesting, don't have to blit it)
testSpace = Space(SCREEN, location=(50, 50))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if testSpace.ShowPiece(player, pygame.mouse.get_pos()):
                player = TogglePlayer(player)

        #SCREEN.blit(mySquare, (0, 0))

        #SCREEN.blit(O, (0, 0))
        #SCREEN.blit(X, X_Rect)
        pygame.display.flip()