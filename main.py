import pygame
import funcs

def remove_piece(piece, pieces_grid):
    pieces = []
    for i in range(3):
        if not pieces_grid[i*25:i*25+25]==[0 for i in range(25)]:
            temp = funcs.make_piece(pieces_grid[i*25:i*25+25])
            if temp.x == piece.x and temp.y==piece.y and temp.piece == piece.piece:
                for j in range(25):
                    pieces_grid[i*25+j]=0
                return


def ungrey(grid):
    for i in range(81):
        if grid[i]==-1:
            grid[i]=1

def up_color_square(pos, grid, blockudoku_squares, pieces_squares, pieces_grid):
    for i in range(81):
        if blockudoku_squares[i].collidepoint(pos):
            if grid[i]==-1:
                ungrey(grid)
                return   
            grid[i] +=1
            return
    #pieces grid
    for i in range(75):
        if pieces_squares[i].collidepoint(pos):
            pieces_grid[i] = (pieces_grid[i]+1)%2
            return

def down_color_square(pos, grid, blockudoku_squares):
    for i in range(81):
        if blockudoku_squares[i].collidepoint(pos):
            grid[i] -=1
            return
    #pieces grid
    for i in range(75):
        if pieces_squares[i].collidepoint(pos):
            pieces_grid[i] = (pieces_grid[i]+1)%2
            return


def show_next_move(piece, grid, move):
    print(piece)
    print(grid)
    for i in range(len(piece)):
        if piece[i]==1:
            grid[i+move]=-1


def update_view(screen, blockudoku_board, blockudoku_squares, pieces_grid, pieces_squares):
    screen.fill("blue")
    #update the view of the grid
    pygame.draw.rect(screen, "black", blockudoku_board)
    for i in range(81):
        if grid[i]==-1:
            pygame.draw.rect(screen, "grey", blockudoku_squares[i])
        elif grid[i]==0:
            pygame.draw.rect(screen, "white", blockudoku_squares[i])
        elif grid[i]==1:
            pygame.draw.rect(screen, "blue", blockudoku_squares[i])
        elif grid[i]==2:
            pygame.draw.rect(screen, "yellow", blockudoku_squares[i])
        elif grid[i]==3:
            pygame.draw.rect(screen, "orange", blockudoku_squares[i])
        elif grid[i]==4:
            pygame.draw.rect(screen, "red", blockudoku_squares[i])
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
    new_grid = funcs.Grid(grid, pieces, [])
    funcs.blockudoku(new_grid, len(pieces))
    for move in new_grid.moves:
        print(f"move: {move[0]}, piece: {move[1].piece}")
    next_piece = new_grid.moves[0][1]
    show_next_move(next_piece.piece, grid, new_grid.moves[0][0])
    remove_piece(next_piece, pieces_grid)


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
            numButton = event.button
            print(numButton)
            if numButton == 1:
                up_color_square(pos, grid, blockudoku_squares, pieces_squares, pieces_grid)
                if is_valid_pressed(pos, valid_button):
                    bot(grid, pieces_grid)
            elif numButton == 3:
                down_color_square(pos, grid, blockudoku_squares)
                    

    # update the view
    update_view(screen, blockudoku_board, blockudoku_squares, pieces_grid, pieces_squares)



    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()
