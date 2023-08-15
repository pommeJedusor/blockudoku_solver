"""

regarde tous les coups possibles el tous les coups possibles après avec profondeur trois
avec comme but d'avoir le moins de carrés bleu à la profondeur trois

"""

class Piece:
    def __init__(self, piece, x, y):
        #[1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1] pour une pyramide
        self.piece = piece
        #[1, 7] pour la pyramide
        self.x = x
        #[0, 7] pour la pyramide
        self.y = y

class Grid:
    def __init__(self, grid, pieces, moves):
        self.grid = [square for square in grid]
        self.pieces = [piece for piece in pieces]
        self.square_number = 1000
        self.moves = [move for move in moves]
        self.deep = 0
        self.children = []
        self.final_grid = grid

    def get_moves(self, piece):
        moves = []
        for x in range(9):
            if not (x >= piece.x[0] and x <= piece.x[1]):
                continue
            for y in range(9):
                if not (y >= piece.y[0] and y <= piece.y[1]):
                    continue
                possible = True
                for z in range(len(piece.piece)):
                    if piece.piece[z]==1 and self.grid[y*9+x+z] > 0:
                        possible = False
                        continue
                if possible:
                    moves.append(y*9+x)
                        
        return moves

    def get_square_number(self):
        square_number = 0
        for i in range(81):
            square_number+=self.grid[i]
        return square_number

    def play_move(self, piece, move):
        for i in range(len(piece.piece)):
            self.grid[move + i] = piece.piece[i]

    def see_grid(self):
        for i in range(81):
            print(self.grid[i],end="")
            if (i+1)%9==0:
                print()


"""
pyramide
00000
00100
01110
00000
00000

"""
def make_piece(piece):
    #adapt to 9x9 grid
    new_piece = [0 for i in range(81)]
    for y in range(5):
        for x in range(5):
            new_piece[y*9+x] = piece[y*5+x]
    piece = new_piece
    

    start = None
    for y in range(9):
        for x in range(9):
            if piece[y*9+x]==1 and start==None:
                last = [x, y]
                start = [x, y]
                temp_x = [x, x]
                temp_y = [y, y]
            elif piece[y*9+x]==1:
                last = [x, y]
                if x < temp_x[0]:
                    temp_x[0] = x
                if x > temp_x[1]:
                    temp_x[1] = x
                if y > temp_y[1]:
                    temp_y[1] = y
    print(f"temp x: {temp_x}")
    temp_x = [start[0]-temp_x[0], 8-(temp_x[1]-start[0])]
    print(f"temp y: {temp_y}")
    temp_y = [0, 8-(temp_y[1]-temp_y[0])]
    start = start[0] + start[1]*9
    last = last[0] + last[1]*9
    piece = Piece(piece[start:last+1],temp_x, temp_y)

    return piece
            

def blockudoku(grid, deepmax):
    if grid.deep==deepmax:
        grid.square_number = grid.get_square_number()
        return
    
    for piece in grid.pieces:
        moves = grid.get_moves(piece)
        #print(moves)
        for move in moves:
            child = Grid(grid.grid, grid.pieces, grid.moves)
            child.deep = grid.deep+1
            child.moves.append([move, piece])
            child.pieces.remove(piece)
            grid.children.append(child)
            child.play_move(piece, move)
            blockudoku(child, deepmax)
    for child in grid.children:
        if child.square_number < grid.square_number:
            grid.square_number = child.square_number
            grid.moves = child.moves
            grid.final_grid = child.grid
    return

"""
ami:
11

patate:
11
11

grand_angle_bd
001
001
111

grand_angle_hg
111
1
1

pyramide
010
111

petit_angle
1
11
"""
"""ami = Piece(3, 2, 1)
patate = Piece(1539, 2, 2)
grand_angle_bd = Piece(459265, 3, 3)
grand_angle_hg = Piece(262663, 3, 3)
pyramide = Piece(897, 3, 2)
petit_angle = Piece(1537, 2, 2)



grid = input("entrez la partie:\n")
#piece 1
temp_piece = input("entrez la pièce:\n")
temp_piece = get_piece_bin(temp_piece)
print(temp_piece)
temp_x = int(input("entrez son x:\n"))
temp_y = int(input("entrez son y:\n"))
piece1 = Piece(temp_piece, temp_x, temp_y)
#piece 2
temp_piece = input("entrez la pièce:\n")
temp_piece = get_piece_bin(temp_piece)
temp_x = int(input("entrez son x:\n"))
temp_y = int(input("entrez son y:\n"))
piece2 = Piece(temp_piece, temp_x, temp_y)
#piece 3
temp_piece = input("entrez la pièce:\n")
temp_piece = get_piece_bin(temp_piece)
temp_x = (int(input("entrez son x:\n")))
temp_y = int(input("entrez son y:\n"))
piece3 = Piece(temp_piece, temp_x, temp_y)

grid = Grid(get_grid_bin(grid), [piece1, piece2, piece3], [])
blockudoku(grid, 3)
print(f"score: {grid.square_number}")
print(f"nb children: {len(grid.children)}")
for child in grid.children:
    print(child.square_number)
    print(f"moves: {child.moves}")
    child.see_grid()
print("moves")
for move in grid.moves:
    print(f"move: {move[0]}, piece: {move[1].piece}")"""