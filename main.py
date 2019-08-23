import sys
import pygame
from setting import Setting
from plane import Plane
from game import check_events



def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    set_game = Setting()
    screen = pygame.display.set_mode((set_game.screen_width, set_game.screen_height))
    battel_plane = Plane(screen)
    bg_color = (35, 191, 234)
    pygame.display.set_caption("Alien Invasion")

    while True:
        check_events(battel_plane)
        # 让最近绘制的屏幕可见
        screen.fill(bg_color)
        battel_plane.blitme()
        battel_plane.update_location()
        pygame.display.flip()


run_game()
