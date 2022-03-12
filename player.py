import pygame

class Player(pygame.sprite.Sprite): # Player должен унаследоваться от pygame.sprite.Sprite
	def __init__(self): # конструктор класса
		super().__init__()
		self.image = pygame.Surface((50, 50))
		self.image.fill((255, 0, 0)) #RGB система цветов
		self.rect = self.image.get_rect() #игрок - это прямоугольник с X=0 и Y=0 в левом верхнем углу прямоугольника


	def update(self):
		pass