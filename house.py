import pygame

pygame.init()

def draw_picture(screen, x, y, width, height):
	"""
	Рисует картинку с домиком на фоне травы и неба.

	:param screen: дисплей pygame, на котором будет изображение
	:param x: левая координата прямоугольника с рисунком
	:param y: верхняя координата прямоугольника с рисунком
	:param weidth: ширина прямоугольника
	:param height: высота прямоугольника
	"""
	
	draw_background(screen, x, y, width, height)
	house_x = x + width // 2
	house_y = y + 3 * height // 4  
	house_height = min(height, width) * 2 // 3
	house_width = int(house_height * 1.5)  
	draw_house(screen, house_x, house_y, house_width, house_height)
	sun_radius = min(width, height) // 10  
	draw_sun(screen, x, y, sun_radius)

def draw_background(screen, x, y, width, height):
	print('Типа рисую фон:', x, y, width, height)

def draw_house(screen, x, y, width, height):
	print('Типа рисую домик:', x, y, width, height)

def draw_sun(screen, x, y, radius):
	print('Типа рисую солнце:', x, y, radius)

width, height = screen_size = (600, 400)
screen = pygame.display.set_mode(screen_size)

# Здесь нужно рисовать
draw_picture(screen, 0, 0, width, height)


pygame.display.update()

work_flag = True
while work_flag:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			
			work_flag = False

print('Program is over')
