import pygame

pygame.init()
weidth, height = screen_size = (600, 400)
screen = pygame.display.set_mode(screen_size)

# Здесь нужно рисовать
# draw_picture(screen)
pygame.display.update()

work_flag = True
while work_flag:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			
			work_flag = False

print('Program is over')
