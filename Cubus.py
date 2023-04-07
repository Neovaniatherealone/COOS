import pygame
from pygame.locals import *
from math import cos, sin, radians

# Fenstergröße
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Würfelgröße
CUBE_SIZE = 100

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Pygame initialisieren
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Rotating 3D Cube")

clock = pygame.time.Clock()

# Würfelklasse
class Cube:
    def __init__(self, x, y, z, size):
        self.x = x
        self.y = y
        self.z = z
        self.size = size

    def draw(self, surface):
        # Zeichne Würfel auf der Oberfläche
        points = []
        for x in (-1, 1):
            for y in (-1, 1):
                for z in (-1, 1):
                    point = [self.x + x * self.size / 2, self.y + y * self.size / 2, self.z + z * self.size / 2]
                    points.append(point)

        for point1 in points:
            for point2 in points:
                if abs(points.index(point1) - points.index(point2)) == 3:
                    pygame.draw.line(surface, WHITE, (point1[0], point1[1]), (point2[0], point2[1]), 2)

# Würfelobjekt erstellen
cube = Cube(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, 0, CUBE_SIZE)

# Hauptprogrammschleife
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Hintergrund löschen
    window.fill(BLACK)

    # Würfel drehen
    angle_x = radians(pygame.time.get_ticks() / 7 % 360)
    angle_y = radians(pygame.time.get_ticks() / 13 % 360)
    angle_z = radians(pygame.time.get_ticks() / 20 % 360)

    # Würfel zeichnen
    pygame.draw.rect(window, WHITE, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT), 2)
    cube.draw(window)

    # Würfelkoordinaten aktualisieren
    cube.x = WINDOW_WIDTH/2 + CUBE_SIZE * cos(angle_x)
    cube.y = WINDOW_HEIGHT/2 + CUBE_SIZE * sin(angle_y)
    cube.z = CUBE_SIZE * sin(angle_z)

    pygame.display.flip()
    clock.tick(60)
