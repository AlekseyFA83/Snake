import pygame
import time
import random

# Инициализация pygame
pygame.init()

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Размеры экрана
dis_width = 600
dis_height = 400

# Настройки игры
snake_block = 10
snake_speed = 15

# Инициализация экрана
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Змейка")

# Часы для управления скоростью игры
clock = pygame.time.Clock()

# Шрифты
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def game_loop():
    game_over = False
    game_close = False

    # Начальная позиция змейки
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Изменение позиции
    x1_change = 0
    y1_change = 0

    # Тело змейки
    snake_list = []
    length_of_snake = 1

    # Позиция еды
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(black)
            message("Вы проиграли! Нажмите Q-выход или C-играть снова", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Проверка границ
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

        # Рисуем еду
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

        # Обновляем змейку
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Удаляем лишние сегменты
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Проверка на столкновение с собой
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)

        # Отображаем счет
        value = score_font.render("Ваш счет: " + str(length_of_snake - 1), True, white)
        dis.blit(value, [0, 0])

        pygame.display.update()

        # Проверка съедания еды
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
