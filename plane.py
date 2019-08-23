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
        self.move_size = 2

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update_location(self):
        if self.move_left:
            self.rect.centerx -= self.move_size
        if self.move_right:
            self.rect.centerx += self.move_size
        if self.move_up:
            self.rect.bottom -= self.move_size
        if self.move_down:
            self.rect.bottom += self.move_size
