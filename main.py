# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import the connect_database function
# and the database_version variable
# from database.py into the current file
import constants

def main():
    print("Here is change")
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
