import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                return

        screen.fill(0x0000)
        pygame.display.flip()


if __name__ == "__main__":
    main()
