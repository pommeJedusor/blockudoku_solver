import pygame
import funcs

def change_color_square(pos, grid, blockudoku_squares, pieces_squares, pieces_grid):
    for i in range(81):
        if blockudoku_squares[i].collidepoint(pos):
            grid[i] = (grid[i]+1)%2
            return
    for i in range(75):
        if pieces_squares[i].collidepoint(pos):
            pieces_grid[i] = (pieces_grid[i]+1)%2
            return

def update_view(screen, blockudoku_board, blockudoku_squares, pieces_grid, pieces_squares):
    screen.fill("blue")
    #update the view of the grid
    pygame.draw.rect(screen, "black", blockudoku_board)
    for i in range(81):
        if grid[i]==1:
            pygame.draw.rect(screen, "blue", blockudoku_squares[i])
        elif grid[i]==2:
            pygame.draw.rect(screen, "white", blockudoku_squares[i])
        else:
            pygame.draw.rect(screen, "grey", blockudoku_squares[i])
        pygame.draw.rect(screen, "black", blockudoku_squares[i], 1)
    
    #update the view of the moves
    pygame.draw.rect(screen, "red", pieces_board)
    for i in range(75):
        if pieces_grid[i]==1:
            pygame.draw.rect(screen, "blue", pieces_squares[i])
        else:
            pygame.draw.rect(screen, "white", pieces_squares[i])
        pygame.draw.rect(screen, "black", pieces_squares[i], 1)
    pygame.draw.rect(screen, "green", valid_button)

def is_valid_pressed(pos, valid_button):
    if valid_button.collidepoint(pos):
        return True
    else:
        return False
    
def bot(grid, pieces_grid):
    pieces = []
    for i in range(3):
        if not pieces_grid[i*25:i*25+25]==[0 for i in range(25)]:
            pieces.append(funcs.make_piece(pieces_grid[i*25:i*25+25]))
    grid = funcs.Grid(grid, pieces, [])
    funcs.blockudoku(grid, len(pieces))
    for move in grid.moves:
        print(f"move: {move[0]}, piece: {move[1].piece}")


pygame.init()
screen = pygame.display.set_mode((1920, 990))
clock = pygame.time.Clock()
running = True

blockudoku_board = pygame.Rect(0, 0, 990, 990)
blockudoku_squares = []
grid = [0 for i in range(81)]

pieces_board = pygame.Rect(990, 0, 930, 990)
pieces_squares = []
pieces_grid = [0 for i in range(75)]

valid_button = pygame.Rect(1725, 445, 100, 100)

size = 990/9
for y in range(9):
    for x in range(9):
        blockudoku_squares.append(pygame.Rect(size*x, size*y, size, size))

size = 930/15
for z in range(3):
    z_size = size*5*z+(z*20)
    for y in range(5):
        for x in range(5):
            pieces_squares.append(pygame.Rect(size*x+990+(1920-990)/2-(2.5*size), size*y+z_size, size, size))

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
                change_color_square(pos, grid, blockudoku_squares, pieces_squares, pieces_grid)
                if is_valid_pressed(pos, valid_button) and not 3 in grid:
                    bot(grid, pieces_grid)
                elif is_valid_pressed(pos, valid_button) and 3 in grid:
                    pass
                    

    # update the view
    update_view(screen, blockudoku_board, blockudoku_squares, pieces_grid, pieces_squares)



    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()
