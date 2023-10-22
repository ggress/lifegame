import pygame


WHITE = (255, 255, 255)
BLACK = (0,0,0)

def generate_cells(width_screen, height_screen, width_cell, height_cell ):

    columns = list()

    for pos_x in range(0, width_screen // width_cell):
        
        rows = list()
        for pos_y in range(0, height_screen // height_cell): 
            
            rows.append(Cell(width_cell, height_cell, pos_x, pos_y))
        
        columns.append(rows)
    
    return columns

class Cell(pygame.sprite.Sprite):
    
    def __init__(self, width, height, pos_x, pos_y):
        
        pygame.sprite.Sprite.__init__(self)

        self.width = width
        self.height = height
        
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.check = False
        self.next_check = False

        self.update_rect()

    def update_rect(self):
        self.rect = self.get_rect()

        self.rect.x = self.pos_x * self.width
        self.rect.y = self.pos_y * self.height

    def get_rect(self):
        self.image = pygame.Surface( (self.width - 1, self.height -1 ) )

        if self.check:
            self.image.fill(BLACK)
        else:
            self.image.fill(WHITE)

        return self.image.get_rect()
    
    def change_next_state(self):
        self.next_check = not self.next_check

    def update(self):
        self.check = self.next_check
        self.update_rect()

    def select(self):
        self.change_next_state()
        self.update()
    
    def reset(self):
        self.next_check = False
        self.update()

    def get_neighborhoods(self, cells):
        neighborhoods = list()

        #Laterales
        for x in range(self.pos_x - 1, self.pos_x + 2):
            #Parte superior e inferior
            for y in range(self.pos_y - 1, self.pos_y + 2):

                if ( x >= 0 and y >= 0) and ( x < len(cells) and y < len(cells[0]) ):
                    
                    cell = cells[x][y]
                    if not ( x == self.pos_x and y == self.pos_y) and cell.check:
                        neighborhoods.append(cell)
                        
        return neighborhoods