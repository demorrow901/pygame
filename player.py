import pygame

class Player(pygame.sprite.Sprite): # Player должен унаследоваться от pygame.sprite.Sprite
	def __init__(self, screen): # конструктор класса
		super().__init__()
		self.image = pygame.Surface((20, 155))
		self.image.fill((255, 255, 255)) #RGB система цветов
		self.rect = self.image.get_rect() #игрок - это прямоугольник с X=0 и Y=0 в левом верхнем углу прямоугольника
		self.rect.center(screen//2)

	def update(self):
		pass