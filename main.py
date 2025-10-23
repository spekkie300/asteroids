import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid


def main():
    # Initialize pygame and set screen
    # TODO: See if i can fix wayland issues with screen not floating
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #  Create groups and add objects to  them
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)  # type: ignore
    Asteroid.containers = (asteroids, updatable, drawable)  # type: ignore
    AsteroidField.containers = updatable

    # Setup clock and deltatime
    clock = pygame.time.Clock()
    dt = 0

    # s Setup player object
    _player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    _asteroid_field = AsteroidField()

    # Main game loop
    while True:
        # Wait for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Set background to black
        screen.fill(0x0000)

        # Call update and draw for groups that are updatable and drawable
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)

        # Render to display and update deltatime
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
