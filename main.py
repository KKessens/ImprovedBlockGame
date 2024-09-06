import pygame
import BlockGame


def main():
    """
    Main method that runs the game
    """
    # start screen is only displayed at the start
    BlockGame.startScreen()
    run = True

    # loop that runs the game
    while run:
        BlockGame.run()
        BlockGame.endScreen()

        # checks if the application was quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

if __name__ == "__main__":
    main()








        