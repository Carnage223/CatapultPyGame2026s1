import pygame
import sys
import random


class Ball:
    def __init__(self, screen, x, y, radius, speed_x, speed_y,):
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = pygame.Color(  random.randrange(256),  random.randrange(256),   random.randrange(256) )

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x - self.radius <= 0 or self.x + self.radius >= self.screen.get_width():
            self.speed_x *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= self.screen.get_height():
            self.speed_y *= -1


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Bouncing Ball')
    clock = pygame.time.Clock()

    balls = []
    for _ in range(100):
        radius = random.randrange(10, 26)
        x = random.randrange(radius, screen.get_width() - radius)
        y = random.randrange(radius, screen.get_height() - radius)
        speed_x = random.choice([-1, 1]) * random.randint(1, 5)
        speed_y = random.choice([-1, 1]) * random.randint(1, 5)
        balls.append(Ball(screen, x, y, radius, speed_x, speed_y))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        for ball in balls:
            ball.move()
            ball.draw()

        pygame.display.update()


main()
