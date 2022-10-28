import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (200,300))