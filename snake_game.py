import pygame
import random
from settings import ICON_PATH


pygame.init()

# 窗口
screenWidth = 1280
screenHeight = 720
screen = pygame.display.set_mode([screenWidth, screenHeight])
# 帧率
clock = pygame.time.Clock()
# 主循环的运行状态
running = True
# 背景颜色
backgroundColor = (102, 153, 153)
# 加载图标
icon = pygame.image.load(ICON_PATH)
pygame.display.set_icon(icon)

# 蛇
class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.color = (26, 140, 255)
        self.size = 10

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, self.color, (segment[0], segment[1], self.size, self.size))

# 食物
class Food:
    def __init__(self):
        self.color = (255, 0, 0)
        self.size = 10
        self.position = self.randomize_position()

    def randomize_position(self):
        x = random.randint(0, (screenWidth // self.size) - 1 ) * self.size
        y = random.randint(0, (screenHeight // self.size) - 1) * self.size
        return (x, y)
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], self.size, self.size))
# 创建蛇和蛇对象
snake = Snake()
food = Food()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(backgroundColor)

    # 绘制蛇和食物
    snake.draw(screen)
    food.draw(screen)

    # 双缓冲  将当前绘制缓冲区的内容切换到显示缓冲区
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()