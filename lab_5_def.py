import pygame
import math

WIDTH = 800
HEIGHT = 500
SHIP_WIDTH = 40
SHIP_HEIGHT = 60
AMPLITUDE = 100
PERIOD = 50//1.5
FREQUENCY = 1
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (150, 0, 0)
DARKBROWN = (100, 0, 0)

class Ship:
    def __init__(self):
        self.x = 0
        self.y = HEIGHT // 2 - SHIP_HEIGHT // 2
        self.angle = 0
        
    def draw(self, surface):
        rect = pygame.Rect(self.x, self.y, 2*SHIP_WIDTH, 1.5*SHIP_HEIGHT // 3)
        machta = pygame.Rect((SHIP_WIDTH)+self.x - SHIP_WIDTH//8, self.y - SHIP_HEIGHT, SHIP_WIDTH // 4, SHIP_HEIGHT)

        pygame.draw.rect(surface, BROWN, rect)
        pygame.draw.polygon(surface, BROWN, ((self.x, self.y+1.5*SHIP_HEIGHT//3), (self.x - SHIP_WIDTH//2, self.y), (self.x, self.y)))
        pygame.draw.polygon(surface, BROWN, ((self.x+2*SHIP_WIDTH, self.y+1.5*SHIP_HEIGHT//3), (self.x +2*SHIP_WIDTH+ SHIP_WIDTH//2, self.y), (self.x+2*SHIP_WIDTH, self.y)))

        pygame.draw.line(surface, BLACK, ((SHIP_WIDTH)+self.x, self.y - 1.5*SHIP_HEIGHT), ((SHIP_WIDTH)+self.x-SHIP_WIDTH//2, self.y), 3)

        pygame.draw.rect(surface, DARKBROWN, machta)


        pygame.draw.polygon(surface, WHITE, (((SHIP_WIDTH)+self.x, self.y - SHIP_HEIGHT), ((SHIP_WIDTH)+self.x, self.y - SHIP_HEIGHT - SHIP_HEIGHT//2), ((SHIP_WIDTH)+self.x+SHIP_WIDTH//2, self.y - SHIP_HEIGHT - SHIP_HEIGHT//4)))
        
    def move(self):
        self.y = HEIGHT // 2 - SHIP_HEIGHT // 2 + AMPLITUDE * math.sin(FREQUENCY * self.x / PERIOD)
        self.x += 1


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

bg_image = pygame.image.load("sea.png")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

ship = Ship()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(bg_image, (0, 0))

    ship.draw(screen)
    ship.move()
    
    pygame.display.flip()
    
    pygame.time.wait(10)

pygame.quit()