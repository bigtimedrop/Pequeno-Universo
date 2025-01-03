import pygame
import random

# Configurções iniciais
screen_width, screen_height = 800, 600
FPS = 60

# Cores
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green= (0, 255, 0)

# Inicia o pygame
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("life")
clock = pygame.time.Clock()

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.energy = 100
        self.speed = random.uniform(1, 3)

    def move(self):
        dx = random.uniform(-self.speed, self.speed)
        dy = random.uniform(-self.speed, self.speed)
        self.x = max(0 , min(screen_width, self.x + dx))
        self.y = max(0, min(screen_height, self.y + dy))
        self.energy -= 0.1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 5)

# Lista de particulas
particles = [
    Particle(random.randint(0, screen_width), random.randint(0, screen_height), random.choice([red, blue, green]))
    for _ in range(50)
]

# Loop principar
running =  True
while running:
    screen.fill (white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualiza as particulas
    for particle in particles:
        particle.move()
        particle.draw(screen)
        if particle.energy <= 0:
            particles.remove(particle)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()