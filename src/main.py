import pygame
import sys

from cell import Cell
from cell import generate_cells


WIDTH = 1200
HEIGHT = 800
FPS = 60

start = False
current_second = 0

pygame.init()

fps = pygame.time.Clock()

surface = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Juego de la vida')

cells = generate_cells(WIDTH, HEIGHT, 20, 20)
sprites = pygame.sprite.Group()
sprites.add(cells)

def start_algorithm():
    for cell in sprites:
        neighborhoods = cell.get_neighborhoods(cells)
        
        if cell.check:
            if not len(neighborhoods) in (2,3):
                cell.change_next_state()
        else:
            if len(neighborhoods) == 3:
                cell.change_next_state()

while True:

    time = pygame.time.get_ticks()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            current_position = pygame.mouse.get_pos() # tupla (x,y)

            for cell in sprites:
                if cell.rect.collidepoint(current_position):
                    cell.select()

        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_SPACE]:
                start = not start
            
            if pressed[pygame.K_r]:
                print('RESET')
                start = False
                for cell in sprites:
                    cell.reset()

    if start:
        second = time // 500
        if second != current_second:
            start_algorithm()

            for cell in sprites:
                cell.update()

            current_second = second

    sprites.draw(surface)
    pygame.display.update()

    fps.tick(FPS)