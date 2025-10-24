'''

'''

#I
import pygame
pygame.init()

#D
screen = pygame.display.set_mode((800,680))
pygame.display.set_caption("PRESS SPACE TO CHANGE BOX COLOR TO BLACK!!!!!!!")

#E
background_image = pygame.image.load("image-2.png")
background = pygame.Surface(screen.get_size())
background.fill(pygame.Color("red"))

box = pygame.Surface((25,25))
box = box.convert()
box.fill((0,0,0))

box_x = 5
box_y = 7
#A

    #A
clock = pygame.time.Clock()
keepgoing = True
    #L
loop_counter = 0
color_choice = 0
while keepgoing:

    #T
    clock.tick(30)    
    #E
    black = (0,0,0)
    blue = (0,0,225)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                color_choice += 1
            if event.key == pygame.K_e:
                box.fill((0,0,0))
                color_choice += 1
    box_y += 7
   
    if box_y > screen.get_width():
        box_y = 0
        loop_counter += 1
    #R
    if loop_counter % 2 != 0:
        screen.blit(background_image, (0,0))
    else:
        screen.blit(background, (0,0))
    if color_choice % 2 != 0:
        box.fill(black)
        pygame.display.set_caption("PRESS SPACE TO CHANGE BOX COLOR TO BLUE!!!!!!!")
    else:
        box.fill(blue)
        pygame.display.set_caption("PRESS SPACE TO CHANGE BOX COLOR TO BLACK!!!!!!!")
    screen.blit(box, (box_x,box_y))
    pygame.display.flip()
