import pygame
import sys

pygame.init()                                                                       #initializes game loop

####Setting up the screen
width = 800
height = 400
screen = pygame.display.set_mode((width,height))                                    #it sets the screen up

score = 0
pygame.display.set_caption('Runner')                                                #the game title

#creating a font object
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)                              #accepts font type, and font size

game_over = pygame.font.Font('font/Pixeltype.ttf', 50)
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
score_surf = test_font.render("My Game", False, 'grey1')
score_rect = score_surf.get_rect( center = (400, 50))                                   #the rect was used as a placeholder

game_over = game_over.render('Game Over', False, 'White')
game_over_rect = game_over.get_rect(center = (400,200))

#importing moving snail and ANIMATION 
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()              #convert_alpha get rid of black and white stuff
snail_xpos = 600

snail_rectangle = snail_surf.get_rect(midbottom = (snail_xpos, height - 100))

#creating a player surface  -WORKING WITH RECTANGLES
player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
# player_rectange = pygame.Rect()                                                     #Creates a rectangle Object this accepts(left, top, width, height)
player_rect = player_surf.get_rect(midbottom= (100,280))                             #this creates a rectangle based on sprite dimension  
#the get_rect acts like an ANCHORPOINT
#can be substttd with top-mid-bottom + left-right
player_gravity = 0 
while True:                                                                         #The window will run indefinitely
    #Check all the EVENTS/ Looping all through events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:           #quitting
            pygame.quit()
            sys.exit()
            #the while loop terminates here with sys.exit()
            #clicking the close window will exit the code

        #Execute if a KEY was pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player_rect.bottom == 300:    
                    player_gravity = -20
                
                #Enable FLAPPING
                # elif player_rect.bottom <= 300:
                #     player_gravity = -13


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

    if game_active:
        # screen.blit(test_surface, (0,0))                                               #showing surface
        screen.blit(sky_surf, (0,0))                                                    #showing sky surface        the tuple goes like (X,Y)
        screen.blit(ground_surf, (0,300))                                            #showing ground surface
        pygame.draw.rect(screen, '#c0e8ec', score_rect)                                 #surface, color, position, width,  border radius
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 5)
        screen.blit(score_surf, score_rect)
        # pygame.draw.line(screen,'Red',(0,0),pygame.mouse.get_pos(),3)                 #drawing a line from (0,0) to mouse position
        # pygame.draw.ellipse(screen,'Yellow',pygame.Rect(50,200,100,100))              #drawing an ellipse
        #animating snail
        if snail_rectangle.left <= width - (width * 1.10):
            snail_rectangle.left = width + 100
            
        snail_rectangle.left += -5  
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
        screen.fill('Black')

        screen.blit(game_over, game_over_rect)
        clock.tick(framerate) 

    pygame.display.update()
    