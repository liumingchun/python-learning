import sys, pygame
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load("beach_ball.jpg")
screen.blit(my_ball,[50,50])
pygame.display.flip()

# move
pygame.time.delay(2000)
screen.blit(my_ball,[150,50])

pygame.draw.rect(screen,[255,255,255],[50,50,90,90],0)
pygame.display.flip()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
