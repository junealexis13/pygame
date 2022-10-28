import pygame
import sys
from random import randint


def display_score():

    current_time = int(pygame.time.get_ticks() / 1000) - start_time                      #pygame.time.get_ticks() is in milliseconds so we converted that into seconds by dividing it by 1000
    score_surf = test_font.render("Score: " + str(current_time),False,(64,64,64))
    score_rect = score_surf.get_rect(center=(400,50))
    screen.blit(score_surf, score_rect)



pygame.init()                                                                       #initializes game loop

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()

        self.player_animation = [player_walk_1, player_walk_2]

        self.player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()
        self.player_index = 0
        self.image = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(200,300))

        self.gravity = 0

        self.timer = int(pygame.time.get_ticks())

    def player_input(self):
        keys = pygame.key.get_pressed()                             #finds the pressed keys
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.gravity = -1

    def animate(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        elif self.rect.bottom >= 300:
            self.player_index += 0.15
            ind = 0
            if self.player_index > len(self.player_animation):
                self.player_index = 0
            self.image = self.player_animation[int(self.player_index)]


    def update(self):
        self.animate()
        self.player_input()
        self.apply_gravity()


####Setting up the screen
width = 800
height = 400
screen = pygame.display.set_mode((width,height))                                    #it sets the screen up

start_time = 0
pygame.display.set_caption('Alien Jumper! HEHE')                                                #the game title

#creating a font object
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)                              #accepts font type, and font size
game_over_font = pygame.font.Font('font/Pixeltype.ttf', 80)
continueGame_font = pygame.font.Font('font/Pixeltype.ttf', 30)
logoFont = pygame.font.Font('font/Pixelmania.ttf', 10)
#working with surface

#setting a framerate 
clock = pygame.time.Clock()
framerate = 60                                                                      #we are setting the FR to 60fps

#Creating a game status update
game_active = True

# test_surface = pygame.Surface((100, 200))                                         #Test surface
sky_surf = pygame.image.load('graphics/sky.png').convert()                                 #Importing the Image as a surface
ground_surf = pygame.image.load('graphics/ground.png').convert()     
# test_surface.fill('Red')

#Text font surface
# score_surf = test_font.render("My Game", False, 'grey1')
# score_rect = score_surf.get_rect( center = (400, 50))                                   #the rect was used as a placeholder

#COntinue Text
textSurf = continueGame_font.render(' Press Space to Continue ', False, '#e4e716e8')
continueGame = textSurf.get_rect(center = (width/2, height - height/4))

#logo
logoSurf = logoFont.render("Game ni Junnie".upper(), False, '#66d7f3ee')
logoRect = logoSurf.get_rect(midleft = (20,30))


game_over = game_over_font.render('Game Over', False, 'White')
game_over_rect = game_over.get_rect(center = (400,200))

#importing moving snail and ANIMATION 
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()              #convert_alpha get rid of black and white stuff
snail_xpos = 600

snail_rectangle = snail_surf.get_rect(midbottom = (snail_xpos, height - 100))

#creating a player surface  -WORKING WITH RECTANGLES
player_walk1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_walk2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()

player = pygame.sprite.GroupSingle()
player.add(Player())


#animation
player_walk = [player_walk1, player_walk2]

player_index = 0

player_surf = player_walk[player_index]
player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()
# player_rectange = pygame.Rect()                                                     #Creates a rectangle Object this accepts(left, top, width, height)
player_rect = player_surf.get_rect(midbottom= (100,280))                             #this creates a rectangle based on sprite dimension  
#the get_rect acts like an ANCHORPOINT
#can be substttd with top-mid-bottom + left-right
player_gravity = 0 



#Idle Screen 
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand_rect = player_stand.get_rect(center = (height/2, width/2))

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)

while True:                                                                         #The window will run indefinitely
    #Check all the EVENTS/ Looping all through events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:           #quitting
            pygame.quit()
            sys.exit()
            #the while loop terminates here with sys.exit()
            #clicking the close window will exit the code


        if game_active:
            #Execute if a KEY was pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom == 300:    
                        player_gravity = -20
                    
                    #Enable FLAPPING
                    # elif player_rect.bottom <= 300:
                    #     player_gravity = -13
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rectangle.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

        # if event.type == obstacle_timer and game_active:
        #     print('Test this uevent')


            #Execute if MOUSE was pressed
            # if event.type == pygame.MOUSEBUTTONDOWN:  
            #     if player_rect.bottom == 300:    
            #         player_gravity = -20

                #ENABLE Flapping
                # elif player_rect.bottom <= 300:                       
                #     player_gravity = -13

            # if event.type == pygame.MOUSEMOTION:
            #     print(pygame.mouse.get_pos())

            #Execute if a KEY was released
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_SPACE:
            #         player_rect.y += +50

            # # #SOME MOUSE EVENTS
            # if event.type == pygame.MOUSEMOTION:     #Detects wether the mouse cursor moves
            #     if player_rect.collidepoint(event.pos):             # event pos returns the mouse position
            #         print('COLLIDE!')                         
            # if event.type == pygame.MOUSEBUTTONDOWN: #Detects any button pushes | Only gets during on click |
            #     print("Clicked!")
            # if event.type == pygame.MOUSEBUTTONUP:   #Detects any button pushes | Only gets during release |
            #     print("Click Releeased!")


    #CONTROLS EVERYTHING ON SCREEN
    if game_active:
        # screen.blit(test_surface, (0,0))                                               #showing surface
        screen.blit(sky_surf, (0,0))                                                    #showing sky surface        the tuple goes like (X,Y)
        screen.blit(ground_surf, (0,300))                                            #showing ground surface
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)                                 #surface, color, position, width,  border radius
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 5)
        # screen.blit(score_surf, score_rect)
        # pygame.draw.line(screen,'Red',(0,0),pygame.mouse.get_pos(),3)                 #drawing a line from (0,0) to mouse position
        # pygame.draw.ellipse(screen,'Yellow',pygame.Rect(50,200,100,100))              #drawing an ellipse
        #animating snail

        player.draw(screen)
        player.update()
        screen.blit(logoSurf,logoRect)

        display_score()
        if snail_rectangle.left <= width - (width * 1.10):
            snail_rectangle.left = width + 100
            
        snail_rectangle.left += -6  
        screen.blit(snail_surf, snail_rectangle)
        
        #adding the player sprite and gravity influence
        player_gravity += 1
        player_rect.y += player_gravity

        #Setting a non-collision based floor
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)



        # if player_rect.left >= width + (width * 0.10):
        #     player_rect.left = -100                                                 #moving the rectangle that contains the object moves it also


        #input mechanics
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print('JUMPING!')


        # chcking for collisions
        # collcheck = player_rect.colliderect(snail_rectangle)                                         #check for collisions
        # if collcheck:
        #     #Your custom program here during collision
        #     player_rect.left += -80
        #     snail_rectangle.left += 40

        #using collidepoint | Checks if the object collides with a point | Can be used with mouse
        # if player_rect.collidepoint((pygame.mouse.get_pos())) and pygame.mouse.get_pressed() == (True, False, False):           #Drag and Drop
        #     player_rect.center = pygame.mouse.get_pos()

                                                                 #constantly updates the screen
        clock.tick(framerate)                                                            #showing the params 

        if player_rect.colliderect(snail_rectangle):
            game_active = False
            clock.tick(framerate) 

    else:
        screen.fill((94,129,162))

        screen.blit(textSurf, continueGame)
        pygame.draw.rect(screen, "White", continueGame, 2, border_radius= 6)
        screen.blit(game_over, game_over_rect)
        clock.tick(framerate) 

    pygame.display.update()
    