import pygame


class Score(pygame.font.Font):
    def __init__(self, x, y, score):
        self.position = pygame.Vector2(x, y)
        self.score = score

    def draw():
        pass

    def increment_score(self):
        self.score += 1
