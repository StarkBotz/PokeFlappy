import numpy as np
import pygame
import pygame_menu
import math


# class Personagem:
#     def __init__(self) -> None:
#         pass

#     def poke(self, image):
#         pass


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("PokeFlappy")
    FPS = 60  # frames por segundo
    scroll_x = 0
    width = 1000
    height = 600
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    scene = pygame.image.load("images/background.jpg")

    game_on = True
    while game_on:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False

        for i in range(0, 2):  # garante que há continuidade na movimentação do cenário
            screen.blit(scene, (i * scene.get_width() + scroll_x, 0))

        scroll_x -= 2
        if (abs(scroll_x) > width):
            scroll_x = 0

        pygame.display.update()
    pygame.quit()
