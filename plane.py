import pygame


class Plane:
    def __init__(self,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/plane.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.move_speed = 2

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update_location(self):
        if self.move_left and self.rect.centerx > 0:
            self.rect.centerx -= self.move_speed
        if self.move_right and self.rect.centerx < 2 * self.screen_rect.centerx:
            self.rect.centerx += self.move_speed
        if self.move_up and self.rect.bottom > 0:
            self.rect.bottom -= self.move_speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += self.move_speed
        # 根据self.center更新rect对象
