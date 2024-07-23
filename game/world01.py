import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 750), pygame.RESIZABLE)
width : int = 1000
height : int = 750
flag : int = 0
start_x : int = 0 # 绘制起始处左上的x坐标
start_y : int = 0 # 绘制起始处左上的y坐标
scale : int = 1000 # 实际宽度 代表缩放比例
screen.set_alpha(None)
pygame.display.set_caption("aaa")

clock = pygame.time.Clock()
FPS = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            width = event.w
            height = event.h
            if width < 1000 or height < 750:
                width = 1000
                height = 750
                screen = pygame.display.set_mode((1000, 750), pygame.RESIZABLE)
            flag = 3 * width - 4 * height
            if flag == 0:
                start_x = 0
                start_y = 0
                scale = width
            elif flag > 0:
                start_y = 0
                start_x = width // 2 - height // 3 * 2
                scale = width - 2 * start_x
            else:
                start_x = 0
                start_y = (height - width // 4 * 3) // 2
                scale = width // 4 * 4

    screen.fill((255, 255, 255))
    if flag > 0:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((0, 0), (start_x, height)))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((width - start_x, 0), (start_x, height)))
    elif flag < 0:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((0, 0), (width, start_y)))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((0, height - start_y), (width, start_y))) 
    pygame.display.flip()

    clock.tick(FPS)
