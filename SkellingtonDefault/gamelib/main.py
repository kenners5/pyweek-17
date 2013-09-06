'''Game main module.

Contains the entry point used by the run_game.py script.

Feel free to put all your game code here, or in other modules in this "gamelib"
package.
'''
import sys
import random
import pygame

import constants
import data
import color_defs as colors
from rover import Rover

def loop(game_pack, screen):
    """ The main loop """

    # Exit if desired
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Process the game mechanics
    for obj in game_pack['Objects']:
        obj.step(game_pack)

    # Draw the screen
    screen.fill(colors.BLACK)
    for obj in game_pack['Objects']:
        surf, loc = obj.render(game_pack)
        screen.blit(surf, loc)
    pygame.display.flip()

def pygame_init(pack):
    """ Init Function for the game-level libraries"""
    pygame.init()    
    pack['dims'] = {'x': 800, 'y': 600}
    screen = pygame.display.set_mode([px for _, px in sorted(pack['dims'].items())])
    return screen

def main():
    random.seed(constants.seed)
    game_pack = {}
    print "Let's get 'fired up'!"
    screen = pygame_init(game_pack)
    game_pack['Objects'] = []
    game_pack['Objects'].append(Rover("head1"))
    game_pack['Objects'].append(Rover("head2"))
    game_pack['Objects'].append(Rover("head3"))
    game_pack['Objects'].append(Rover("head4"))
    game_pack['Objects'].append(Rover("head1"))
    game_pack['Objects'].append(Rover("head2"))
    game_pack['Objects'].append(Rover("head3"))
    game_pack['Objects'].append(Rover("head4"))
    game_pack['Objects'].append(Rover("head1"))
    game_pack['Objects'].append(Rover("head2"))
    game_pack['Objects'].append(Rover("head3"))
    game_pack['Objects'].append(Rover("head4"))
    game_pack['Objects'].append(Rover("head1"))
    game_pack['Objects'].append(Rover("head2"))
    game_pack['Objects'].append(Rover("head3"))
    game_pack['Objects'].append(Rover("head4"))

    # Initialize objects
    for obj in game_pack['Objects']:
        fry_head = data.load('fry_head.png')
        obj.load(game_pack, fry_head)
        fry_head.close()
        obj.layer.speed = [2, 2]

    while 1:
        loop(game_pack, screen)

if __name__ == "__main__":
    main()

# EOF
