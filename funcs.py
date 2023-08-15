"""

regarde tous les coups possibles el tous les coups possibles après avec profondeur trois
avec comme but d'avoir le moins de carrés bleu à la profondeur trois

"""

class Piece:
    def __init__(self, piece, x, y):
        self.piece = piece
        #1 pour le carré de 1 / 1
        self.x = x
        #1 pour le carré de 1 / 1
        self.y = y

class Grid:
    def __init__(self, grid, pieces, moves):
        self.grid = grid
        self.pieces = [piece for piece in pieces]
        self.square_number = 82
        self.moves = [move for move in moves]
        self.deep = 0
        self.children = []
        self.final_grid = grid

    def get_moves(self, piece):
        moves = 0
        for x in range(9):
            for y in range(9):
                #print(f"piece = piece.piece")
                if (((piece.piece << (y*9+x)) & self.grid) == 0) and ((piece.x + x) <= 9) and ((piece.y + y) <= 9):
                    print(f"x: {x}, y: {y}")
                    moves |= 2**(y*9+x)
        return moves

    def get_square_number(self):
        square_number = 0
        for i in range(81):
            if self.grid & 2**i:
                square_number+=1
        return square_number

    def play_move(self, piece, move):
        self.grid |= piece.piece << move
        #horizontal
        ligne = 511
        for i in range(9):
            if self.grid & (ligne << i*9) == (ligne << i*9):
                self.grid ^= ligne << i*9
        #vertical
        #100 000 000 9*
        ligne = 4731607904558235517441
        for i in range(9):
            if self.grid & (ligne << i) == (ligne << i):
                self.grid ^= ligne << i

        #square
        #111 000 000 3*
        ligne = 117670336
        for x in range(3):
            for y in range(3):
                if self.grid & (ligne << (y*27 + x*3)) == (ligne << (y*27 + x*3)):
                    self.grid ^= ligne << (y*27 + x*3)

    def see_grid(self):
        for i in range(81):
            if self.grid & (2**i):
                print(1,end="")
            else:
                print(0,end="")
            if (i+1)%9==0:
                print()


def get_grid_bin(grid):
    bin_grid = 0
    for i in range(81):
        if grid[i]=="1":
            bin_grid += 2**i
    return bin_grid

def get_piece_bin(piece):
    bin_piece = 0
    for i in range(1,len(piece)+1):
        if piece[-i]=="1":
            bin_piece += 2**(i-1)
    return bin_piece


def blockudoku(grid, deepmax):
    if grid.deep==deepmax:
        grid.square_number = grid.get_square_number()
        return
    
    for piece in grid.pieces:
        moves = grid.get_moves(piece)
        #print(moves)
        for i in range(81):
            if moves & (1 << i):
                child = Grid(grid.grid, grid.pieces, grid.moves)
                child.deep = grid.deep+1
                child.moves.append([i, piece])
                child.pieces.remove(piece)
                grid.children.append(child)
                child.play_move(piece, i)
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
ami = Piece(3, 2, 1)
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
    print(f"move: {move[0]}, piece: {move[1].piece}")