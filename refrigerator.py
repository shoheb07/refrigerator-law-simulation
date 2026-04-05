import pygame
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Refrigerator Law Simulation")

clock = pygame.time.Clock()

# Colors
BLUE = (0, 150, 255)
RED = (255, 80, 80)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Temperatures
cold_temp = 5
hot_temp = 35

font = pygame.font.SysFont(None, 28)

def draw_text(text, x, y):
    img = font.render(text, True, BLACK)
    screen.blit(img, (x, y))

def draw_arrow(start, end, color):
    pygame.draw.line(screen, color, start, end, 4)
    pygame.draw.circle(screen, color, end, 6)

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw fridge (cold area)
    pygame.draw.rect(screen, BLUE, (100, 150, 150, 200))
    draw_text("Cold Area", 110, 120)
    draw_text(f"{cold_temp}°C", 130, 180)

    # Draw outside (hot area)
    pygame.draw.rect(screen, RED, (550, 150, 150, 200))
    draw_text("Hot Area", 560, 120)
    draw_text(f"{hot_temp}°C", 580, 180)

    # Compressor
    pygame.draw.circle(screen, GRAY, (400, 250), 50)
    draw_text("Compressor", 350, 320)

    # Heat flow arrow (cold → compressor)
    draw_arrow((250, 250), (350, 250), BLUE)
    draw_text("Heat Absorbed", 260, 220)

    # Work input arrow
    draw_arrow((400, 150), (400, 200), BLACK)
    draw_text("Work Input", 370, 120)

    # Heat release arrow (compressor → hot)
    draw_arrow((450, 250), (550, 250), RED)
    draw_text("Heat Released", 460, 220)

    # Simulation logic
    cold_temp -= 0.01
    hot_temp += 0.01

    # Limits
    if cold_temp < 0:
        cold_temp = 0
    if hot_temp > 60:
        hot_temp = 60

    pygame.display.update()
    clock.tick(60)
