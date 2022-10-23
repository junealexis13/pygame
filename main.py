from cgi import test
from platform import python_branch
from xml.dom import minidom
import pygame
import sys

pygame.init()                                                                       #initializes game loop

####Setting up the screen
width = 800
height = 400
screen = pygame.display.set_mode((width,height))                                    #it sets the screen up

pygame.display.set_caption('Runner')                                                #the game title

#creating a font object
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)                              #accepts font type, and font size

#working with surface

#setting a framerate 
clock = pygame.time.Clock()
framerate = 60                                                                      #we are setting the FR to 60fps

# test_surface = pygame.Surface((100, 200))                                         #Test surface
sky_surface = pygame.image.load('graphics/sky.png').convert()                                 #Importing the Image as a surface
ground_surface = pygame.image.load('graphics/ground.png').convert()     
# test_surface.fill('Red')

#Text font surface
text_surface = test_font.render('My game', False, 'Green')

#importing moving snail and ANIMATION 
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()              #convert_alpha get rid of black and white stuff
snail_xpos = 600

snail_rectangle = snail_surface.get_rect(midbottom = (snail_xpos, height - 100))

#creating a player surface  -WORKING WITH RECTANGLES
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
# player_rectange = pygame.Rect()                                                     #Creates a rectangle Object this accepts(left, top, width, height)
player_rect = player_surface.get_rect(midbottom= (80,height - 100))                             #this creates a rectangle based on sprite dimension  
#the get_rect acts like an ANCHORPOINT
#can be substttd with top-mid-bottom + left-right

while True:                                                                         #The window will run indefinitely
    #Check all the EVENTS/ Looping all through events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:           #quitting
            pygame.quit()
            sys.exit()
            #the while loop terminates here with sys.exit()
            #clicking the close window will exit the code

        # #SOME MOUSE EVENTS
        # if event.type == pygame.MOUSEMOTION:     #Detects wether the mouse cursor moves
        #     if player_rect.collidepoint(event.pos):             # event pos returns the mouse position
        #         print('COLLIDE!')                         
        # if event.type == pygame.MOUSEBUTTONDOWN: #Detects any button pushes | Only gets during on click |
        #     print("Clicked!")
        # if event.type == pygame.MOUSEBUTTONUP:   #Detects any button pushes | Only gets during release |
        #     print("Click Releeased!")

    # screen.blit(test_surface, (0,0))                                               #showing surface
    screen.blit(sky_surface, (0,0))                                                  #showing sky surface        the tuple goes like (X,Y)
    screen.blit(ground_surface,(0,height - 100) )                                    #showing ground surface
    screen.blit(text_surface, (325, 50))

    #animating snail
    if snail_rectangle.left <= width - (width * 1.10):
        snail_rectangle.left = width + 100
        
    snail_rectangle.left += -2  
    screen.blit(snail_surface, snail_rectangle)
    
    #adding the player sprite
    screen.blit(player_surface, player_rect)
    player_rect.left += 2
    if player_rect.left >= width + (width * 0.10):
        player_rect.left = -100                                                 #moving the rectangle that contains the object moves it also

    # chcking for collisions
    collcheck = player_rect.colliderect(snail_rectangle)                                         #check for collisions
    if collcheck:
        #Your custom program here during collision
        player_rect.left += -80
        snail_rectangle.left += 40

    #using collidepoint | Checks if the object collides with a point | Can be used with mouse
    # if player_rect.collidepoint((pygame.mouse.get_pos())) and pygame.mouse.get_pressed() == (True, False, False):           #Drag and Drop
    #     player_rect.center = pygame.mouse.get_pos()

    pygame.display.update()                                                          #constantly updates the screen
    clock.tick(framerate)                                                            #showing the params 

