"""
    ball(
        screen,
        centerx, #
        centery, # зависят от screen
        width,
        height,
        velosity_x,
        velocity_y,
        color,
    )
"""
import pygame


class Ball():
    def __init__(
        self,
        screen,
        width=20,
        height20,
        color=(255, 255, 255),
        centerx,
        centery,
        velosity_x=10,
        velosity_y=10
    ):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.velosity_x = velosity_x
        self.velosity_y = velosity_y

    def draw(self):
        self.screen.blit(self.image, self.rect)
