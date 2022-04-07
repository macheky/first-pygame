# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pygame

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((750, 500))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (0, 250, 250), (250, 250), 75)
        pygame.display.flip()

    pygame.quit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
