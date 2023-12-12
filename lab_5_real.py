import pygame
import math

# Инит
pygame.init()

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Ширина и высота окна
screen_width = 400
screen_height = 400
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Clock")

# Для fps
clock = pygame.time.Clock()

done = False

# Define function to toggle size of objects
def toggle_size():
    global hour_hand_length, minute_hand_length
    if not size_toggle:
        # Increase size gradually
        for i in range(50):
            hour_hand_length += 1
            minute_hand_length += 1
            pygame.time.delay(1)
    else:
        # Decrease size gradually
        for i in range(50):
            hour_hand_length -= 1
            minute_hand_length -= 1
            pygame.time.delay(1)

hour_hand_length = 70
minute_hand_length = 100
size_toggle = False
scale = 0
space = False

# Игровой цикл
while not done:
    # --- События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_SPACE:
                space = True
    
    if space:
        # Toggle the size of all bodies
        if not size_toggle and scale < 50:
            # Increase size gradually
            hour_hand_length += 1
            minute_hand_length += 1
            scale += 1
        elif size_toggle and scale > 0:
            # Decrease size gradually
            hour_hand_length -= 1
            minute_hand_length -= 1
            scale -= 1
        if scale == 50 or scale == 0:
            size_toggle = not size_toggle
            space = False
    # --- Рисование

    # Очистить экран
    screen.fill(WHITE)

    # Нарисовать циферблат
    pygame.draw.circle(screen, BLACK, (200, 200), 150, 2)

    # Часовые засечки
    for i in range(12):
        angle = i * math.pi / 6
        x = int(200 + 120 * math.cos(angle))
        y = int(200 + 120 * math.sin(angle))
        # pygame.draw.circle(screen, BLACK, (x, y), 10)

        # Нарисовать числа
        font = pygame.font.Font(None, 36)
        num = 3+i%12 if (3+i%12) <= 12 else (3+i%12)%12
        text = font.render(str(num), True, BLACK)
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)

    # Нарисовать интервалы на циферблате
    for i in range(60):
        angle = i * math.pi / 30
        if i % 5 == 0:
            start_x = int(200 + 135 * math.cos(angle))
            start_y = int(200 + 135 * math.sin(angle))
        else:
            start_x = int(200 + 145 * math.cos(angle))
            start_y = int(200 + 145 * math.sin(angle))
        end_x = int(200 + 150 * math.cos(angle))
        end_y = int(200 + 150 * math.sin(angle))
        pygame.draw.line(screen, BLACK, (start_x, start_y), (end_x, end_y), 2)

    # Получить текущее время
    current_time = pygame.time.get_ticks()

    # Посчитать углы для часовой и минутной стрелок
    hour_angle = (current_time / 1000 / 60 % 12) * math.pi / 6 - math.pi / 2
    minute_angle = (current_time / 1000 % 60) * math.pi / 30 - math.pi / 2

    # Часовая стрелка
    hour_x = int(200 + hour_hand_length * math.cos(hour_angle))
    hour_y = int(200 + hour_hand_length * math.sin(hour_angle))
    pygame.draw.line(screen, BLACK, (200, 200), (hour_x, hour_y), 10)

    # Минутная стрелка
    minute_x = int(200 + minute_hand_length * math.cos(minute_angle))
    minute_y = int(200 + minute_hand_length * math.sin(minute_angle))
    pygame.draw.line(screen, BLACK, (200, 200), (minute_x, minute_y), 5)

    # Update the screen
    pygame.display.flip()

    # 60 fps
    clock.tick(60)

# Закрыть окно и выйти
pygame.quit()
