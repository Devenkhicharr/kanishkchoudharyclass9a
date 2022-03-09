
import pygame, sys

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((500,600))

#creating objects of game
tomatoes=[]
mushrooms=[]
carrots=[]
brinjals=[]
pumpkins=[]

carrot_img=pygame.load.image("carrot.png").convert_alpha()
carrot_img=pygame.load.image("carrot.png").convert_alpha()
carrot_img=pygame.load.image("carrot.png").convert_alpha()
carrot_img=pygame.load.image("carrot.png").convert_alpha()
carrot_img=pygame.load.image("carrot.png").convert_alpha()

        
while True:    
    screen.fill((30,80,20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
             
    for tomato in tomatoes:        
        #pygame.draw.rect(screen,(288,00,20),tomato)
    for mushroom in mushrooms:
        #pygame.draw.rect(screen,(200,200,20),mushrooms)
    for carrot in carrots:
        #pygame.draw.rect(screen,(100,50,20),carrots)
    for brinjal in brinjals:
        #pygame.draw.rect(screen,(223,50,200),brinjals)
    for pumpkin in pumpkins:
        #pygame.draw.rect(screen,(223,200,20),pumpkins)






    
    pygame.display.update()
    clock.tick(30)

