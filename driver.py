import pygame

SCREEN_SIZE = (1000, 600)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
LOCATION = (500, 300)
RADIUS = 100

def main():
    pygame.init()

    screen = pygame.display.set_mode(SCREEN_SIZE)

    running = True
    while running:

        # If window was closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        pygame.draw.circle(screen, BLUE, LOCATION, RADIUS)

        pygame.display.update()


if __name__ == '__main__':
    main()

