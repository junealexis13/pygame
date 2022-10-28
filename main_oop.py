import pygame

pygame.init()

screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption('Run Run Runner')

#Framerate Counter
fps = pygame.time.Clock()
fps_rate = 60

#Game Active Trigger
game_active = True

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        self.rect = self.image.get_rect(center=(screen_width/2, screen_height/2))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()                             #finds the pressed keys
        if keys[pygame.K_SPACE]:
            self.gravity = -20

    def gravity(self):
        self.gravity += 1
        self.rect += self.gravity

    def update(self):
        self.player_input()
        self.gravity()


    
player = pygame.sprite.GroupSingle()
player.add(Player())

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('White')
    player.draw(screen)
    fps.tick(fps_rate)

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        print('True')
    pygame.display.update()