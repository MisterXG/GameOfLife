import random
import pygame

width = 50
height = 50
tile_size = 20
max_cells_alive = width * height / 1.3
current = 0

world = [[0 for _ in range(height)] for _ in range(width)]
while current < max_cells_alive:
    for x in range(width):
        for y in range(height):
            if not world[x][y]:
                if current < max_cells_alive:
                    cell = random.randint(0, 1)
                    world[x][y] = cell
                    if cell:
                        current += 1
                else:
                    world[x][y] = 0

screen = pygame.display.set_mode((1024, 1024))
timer = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    if pygame.mouse.get_pressed(3)[0]:
        try:
            world[int(pygame.mouse.get_pos()[0] / tile_size)][int(pygame.mouse.get_pos()[1] / tile_size)] = 1
        except:
            pass
    elif pygame.mouse.get_pressed(3)[2]:
        try:
            world[int(pygame.mouse.get_pos()[0] / tile_size)][int(pygame.mouse.get_pos()[1] / tile_size)] = 0
        except:
            pass
    screen.fill('blue')
    for i, x in enumerate(world):
        for j, y in enumerate(x):
            pygame.draw.rect(screen, 'black' if y else ('white' if (i + j) % 2 == 0 else (245, 245, 245)), (i * tile_size, j * tile_size, tile_size, tile_size))
    pygame.display.flip()
    timer.tick(5)
    if not pygame.mouse.get_pressed(3)[0]:
        new_world = [row[:] for row in world]
        for x in range(width):
            for y in range(height):
                count = 0
                for x1 in range(-1, 2):
                    for y1 in range(-1, 2):
                        if 0 <= x + x1 <= width - 1 and 0 <= y + y1 <= height - 1 and (x1 != 0 or y1 != 0) and world[x + x1][y + y1]:
                            count += 1
                if world[x][y]:
                    if count < 2:
                        new_world[x][y] = 0
                    elif count > 3:
                        new_world[x][y] = 0
                elif count == 3:
                    new_world[x][y] = 1
        world = new_world
