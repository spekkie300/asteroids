import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot


def main():
    # Initialize pygame and set screen
    # TODO: See if i can fix wayland issues with screen not floating
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #  Create groups and add asteroids to  them
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)  # type: ignore
    Asteroid.containers = (asteroids, updatable, drawable)  # type: ignore
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    # Setup clock and deltatime
    clock = pygame.time.Clock()
    dt = 0

    # s Setup player asteroid
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

        for asteroid in asteroids:
            if asteroid.check_collision(_player):
                print("Game over!")
                exit()

            for bullet in shots:
                if bullet.check_collision(asteroid):
                    bullet.kill()
                    asteroid.split()

        for asteroid in drawable:
            asteroid.draw(screen)

        # Render to display and update deltatime
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
