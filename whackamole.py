import pygame
import random


def main():
    try:
        pygame.init()

        # mole setup
        mole_image = pygame.image.load("mole.png")
        mole_size = 32
        molex = 0
        moley = 0

        # grid making
        grid_width, grid_height = 20, 16
        screen_width = grid_width * mole_size
        screen_height = grid_height * mole_size

        # screeeeen
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Whack-a-Mole")

        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():

                # ends the game
                if event.type == pygame.QUIT:
                    running = False

                # mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    # checks to see if mouse position = mole position
                    if (molex <= mouse_x < molex + mole_size and moley <= mouse_y < moley + mole_size):

                        # new mouse
                        # makes sure that it stays within a grid space and not outside of it
                        molex = random.randrange(0, grid_width) * mole_size
                        moley = random.randrange(0, grid_height) * mole_size

            # grid
            screen.fill("light green")
            for x in range(0, 640, 32):
                pygame.draw.line(screen, "black", (x, 0), (x, 512))
            for y in range(0, 512, 32):
                pygame.draw.line(screen, "black", (0, y), (640, y))

            screen.blit(mole_image, mole_image.get_rect(topleft=(molex, moley)))

            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
