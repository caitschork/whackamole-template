import pygame
import random

def main():
    def draw_grid():
        # draw horizontal lines
        for i in range(0, 16):
            pygame.draw.line(
                screen,
                "black",
                (0, i * 32),
                (640, i * 32),
            )
        # draw vertical lines
        for i in range(0, 20):
            pygame.draw.line(
                screen,
                "black",
                (i * 32, 0),
                (i * 32, 512)
            )
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        mole_rect = mole_image.get_rect(topleft = (0, 0))
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row = y // 32
                    col = x // 32
                    mole_row = mole_rect.y // 32
                    mole_col = mole_rect.x // 32
                    if (row, col) == (mole_row, mole_col):
                        row_rand = random.randrange(0, 16)
                        col_rand = random.randrange(0, 20)
                        mole_rect.topleft = (col_rand * 32, row_rand * 32)

            screen.fill("light green")
            draw_grid()
            screen.blit(mole_image, mole_rect)
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
