import pygame

def change_color_square(pos, grid, squares):
    for i in range(81):
        if squares[i].collidepoint(pos):
            grid[i] = (grid[i]+1)%2
            return

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
blockudoku_board = pygame.Rect(0, 0, 720, 720)
blockudoku_squares = []
grid = [i%2 for i in range(81)]

for x in range(9):
    for y in range(9):
        blockudoku_squares.append(pygame.Rect(80*x, 80*y, 80, 80))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            numBouton = event.button
            if numBouton == 1:
                change_color_square(pos, grid, blockudoku_squares)

    # update the view
    screen.fill("blue")
    #update the view of the grid
    pygame.draw.rect(screen, "black", blockudoku_board)
    for i in range(81):
        if grid[i]==1:
            pygame.draw.rect(screen, "blue", blockudoku_squares[i])
        else:
            pygame.draw.rect(screen, "white", blockudoku_squares[i])
        pygame.draw.rect(screen, "black", blockudoku_squares[i], 1)
    
    #update the view of the moves



    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()
