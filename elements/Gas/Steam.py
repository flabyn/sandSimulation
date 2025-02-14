from elements.Gas.Gas import Gas
from elements.ElementTypeShh import ElementType #i dont like this

class Steam(Gas):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self.colour = (179, 198, 230)
        self.viscosity = 0.4
    
    def lifeStep(self, matrix):
        if self.life == 0:
            matrix.DieAndReplace(self.position,ElementType.WATER)
        else:
            self.life -= 1