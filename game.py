import sys
import pygame


def check_events(plane):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                plane.move_right = True
            if event.key == pygame.K_LEFT:
                plane.move_left = True
            if event.key == pygame.K_UP:
                plane.move_up = True
            if event.key == pygame.K_DOWN:
                plane.move_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                plane.move_right = False
            if event.key == pygame.K_LEFT:
                plane.move_left = False
            if event.key == pygame.K_UP:
                plane.move_up = False
            if event.key == pygame.K_DOWN:
                plane.move_down = False
