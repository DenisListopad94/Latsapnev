class ChessPiece:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
    
    def can_attack(self, x, y):
        raise NotImplementedError("Subclass must implement abstract method")

class Queen(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
    
    def can_attack(self, x, y):
        if self.x == x or self.y == y or abs(self.x - x) == abs(self.y - y):
            return True
        return False

class Pawn(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
    
    def can_attack(self, x, y):
        if self.color == 'white':
            return x in [self.x-1, self.x+1] and y == self.y+1
        elif self.color == 'black':
            return x in [self.x-1, self.x+1] and y == self.y-1
        return False

class Knight(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
    
    def can_attack(self, x, y):
        dx = abs(self.x - x)
        dy = abs(self.y - y)
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

queen = Queen('white', 4, 4)
pawn = Pawn('black', 2, 6)
knight = Knight('white', 3, 4)

print(queen.can_attack(7, 4))  # True
print(pawn.can_attack(3, 5))   # True
print(knight.can_attack(5, 5))  # True