import pygame 
from player import Player

pygame.init() #начало создания экрана
screen = pygame.display.set_mode((800, 600)) #в скобках высота и ширина соответственно
pygame.display.set_caption("Моя игра") #название окна

all_sprites = pygame.sprite.Group() #все спрайты хранятся в "списке" класса Group из pygame
player = Player() # создаем игрока из импортированного на второй строке класса Player
all_sprites.add(player) # добавляем игрока к остальным спрайтам в общий "список"
clock = pygame.time.Clock() 


while True: # работает как в скретче
    screen.fill((0, 0, 0))
    for event in pygame.event.get(): # в цикле постоянно происходят события
        if event.type == pygame.QUIT: # событие означает: нажата кнопка X в правом верхнем углу окна
            pygame.quit() # при этом событии окно с игрой должно закрыться
        elif event.type == pygame.KEYDOWN: #кнопка(любая на клавиатуре) нажата
            if event.key == pygame.K_DOWN: #кнопка "вправо"
                player.rect.y += 15 #изменяем координаты
            elif event.key == pygame.K_UP: #кнопка "вправо"
                player.rect.y -= 15

    all_sprites.update() # спрайты постоянно обновляются
    all_sprites.draw(screen)
    pygame.display.flip() # двойная буферизация
    clock.tick(60) # в скобках FPS игры
