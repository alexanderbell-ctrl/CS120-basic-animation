'''

'''

#I
import pygame
pygame.init()

#D
screen = pygame.display.set_mode((800,680))
pygame.display.set_caption("Hello World")

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
while keepgoing:

    #T
    clock.tick(30)    
    #E
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False

    box_y += 7
    loop_counter += 1
    if box_y > screen.get_width():
        box_y = 0
    #R
    if loop_counter % 2 != 0:
        screen.blit(background_image, (0,0))
    else:
        screen.blit(background, (0,0))
    screen.blit(box, (box_x,box_y))
    pygame.display.flip()
