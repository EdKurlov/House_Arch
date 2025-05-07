import pygame

def draw_picture(screen, x, y, weidth, height):
	"""
	Рисует картинку с домиком на фоне травы и неба.

	:param screen: дисплей pygame, на котором будет изображение
	:param x: левая координата прямоугольника с рисунком
	:param y: верхняя координата прямоугольника с рисунком
	:param weidth: ширина прямоугольника
	:param height: высота прямоугольника
	"""
	print("as if I were drawing a picture", x, y, weidth, height)

pygame.init()
weidth, height = screen_size = (600, 400)
screen = pygame.display.set_mode(screen_size)

# Здесь нужно рисовать
draw_picture(screen, 0, 0, weidth, height)


pygame.display.update()

work_flag = True
while work_flag:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			
			work_flag = False

print('Program is over')
