import pygame
from player import Player
import ball

WIDTH = 800
HEIGH = 600

pygame.init()  # начало создания экрана
screen = pygame.display.set_mode((WIDTH, HEIGH))
# в скобках высота и ширина соответственно
pygame.display.set_caption("Моя игра")  # название окна

all_sprites = pygame.sprite.Group()
# все спрайты хранятся в "списке" класса Group из pygame
player = Player(screen, centerx=100)
opponent = Player(screen, centerx=700, is_auto=True)
ball = Ball(screen)
# создаем игрока из импортированного на второй строке класса Player

clock = pygame.time.Clock()


game = True
while game:  # работает как в скретче
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        # в цикле постоянно происходят события
        if event.type == pygame.QUIT:
            # событие означает: нажата кнопка X в правом верхнем углу окна
            game = False
            # при этом событии окно с игрой должно закрыться

    keys = pygame.key.get_pressed()

    player.draw()
    player.control(keys)
    opponent.draw()
    ball.draw()
    all_sprites.update()  # спрайты постоянно обновляются
    all_sprites.draw(screen)
    pygame.display.flip()  # двойная буферизация
    clock.tick(60)  # в скобках FPS игры

pygame.quit()
