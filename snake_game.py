import pygame
import random
import sys
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
    # 初始化对象的属性
    def __init__(self, speed=5):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.color = (26, 140, 255)
        self.size = 10
        self.direction = 'RIGHT' #初始方向
        self.change_to = self.direction # 新方向
        self.speed = speed   # 蛇的速度（每帧移动的像素数）

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, self.color, (segment[0], segment[1], self.size, self.size))

    def update(self):
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

        # 更新蛇的身体
        if self.direction == 'UP':
            new_head = (self.body[0][0], self.body[0][1] - self.speed)
        elif self.direction == 'DOWN':
            new_head = (self.body[0][0], self.body[0][1] + self.speed)
        elif self.direction == 'LEFT':
            new_head = (self.body[0][0] - self.speed, self.body[0][1])
        elif self.direction == 'RIGHT':
            new_head = (self.body[0][0] + self.speed, self.body[0][1])

        # 添加新头部
        self.body.insert(0, new_head)
        # 移除尾部
        self.body.pop()       

    def is_dead(self):
        # 检查蛇头是否超出边界
        head_x, head_y = self.body[0]
        return head_x < 0 or head_x >= screenWidth or head_y < 0 or head_y >= screenHeight             

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
snake = Snake(speed=5)
food = Food()


# 重新开始游戏函数
def reset_game():
    global snake, food
    snake = Snake(speed=5)
    food = Food()


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 检测键盘事件
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                snake.change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                snake.change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                snake.change_to = 'RIGHT'

    if snake.is_dead():
        # 显示“死亡”消息
        font = pygame.font.SysFont(None, 55)
        message = font.render("Game Over! Click to Restart", True, (255, 255, 255))
        message_rect = message.get_rect(center=(screenWidth // 2, screenHeight // 2))
        screen.fill(backgroundColor)
        screen.blit(message, message_rect)
        pygame.display.flip()

        # 等待重新开始
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    reset_game()  # 重新开始游戏
                    waiting = False
    else:
        snake.update()  # 更新蛇的位置
    screen.fill(backgroundColor)

    # 绘制蛇和食物
    snake.draw(screen)
    food.draw(screen)

    # 双缓冲  将当前绘制缓冲区的内容切换到显示缓冲区
    pygame.display.flip()

    clock.tick(60) 

pygame.quit()