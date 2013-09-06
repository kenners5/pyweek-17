'''Game main module.

Contains the entry point used by the run_game.py script.

Feel free to put all your game code here, or in other modules in this "gamelib"
package.
'''
import os
import time
import random
import pygame

import constants
import data
from rover import Rover
from textbox import TextBox

def loop(game_pack, screen):
    """ The main loop """

    # Exit if desired
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Yep, we're done.
            return True

    # Process the game mechanics
    for obj in game_pack['Objects']:
        obj.step(game_pack)

    # Poke the frame count
    game_pack['count'] = game_pack['count'] + 1
    game_pack['textbox_status'] = "Frame %d" % game_pack['count']

    # Draw the screen
    screen.fill(constants.BLACK)
    for obj in game_pack['Objects']:
        surf, loc = obj.render(game_pack)
        screen.blit(surf, loc)

    pygame.display.flip()

    # Snap a screenshot and see what happens
    if constants.record:
        frame_name = os.path.join(game_pack['output'],
                                  "frame%d.png" % len(game_pack['frames']))
        pygame.image.save(screen, frame_name)
        game_pack['frames'].append(frame_name)

    # Not done
    return False

def pygame_init(pack):
    """ Init Function for the game-level libraries"""
    pygame.init()
    pygame.font.init()

    pack['font'] = pygame.font.Font(None, 36)

    pack['dims'] = {'x': 800, 'y': 600}
    screen = pygame.display.set_mode([px for _, px in sorted(pack['dims'].items())])
    return screen

def main():
    random.seed(constants.seed)
    game_pack = {'count':   0,
                 'Objects': [],
                 'output':  None,
                 'frames':  [],
                 'font':    None,
                 'dims':    {},
                 'textbox_status': "",
                 }
    print "Let's get 'fired up'!"
    screen = pygame_init(game_pack)
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
    game_pack['Objects'].append(TextBox("status"))

    if constants.record:
        output_folder = os.path.join("game_output",
                                     time.strftime("%Y%m%d_%H%M%S"))
        os.makedirs(output_folder)
        game_pack['output'] = output_folder

    # Initialize objects
    for obj in game_pack['Objects']:
        fry_head = data.load('fry_head.png')
        obj.load(game_pack, image=fry_head)
        fry_head.close()
        obj.layer.speed = [2, 2]

    done = False
    while not done:
        done = loop(game_pack, screen)

    if constants.record:
        import cv2
        video_filename = os.path.join(game_pack['output'],
                                      "output.avi")
        video = cv2.VideoWriter(video_filename,     # Filename
                                -1, # cv2.cv.CV_FOURCC('Y','U','V','9'),  # FourCC
                                30.0,                  # Framerate
                                (game_pack['dims']['x'], # Dimensions tuple
                                 game_pack['dims']['y']))

        for still in game_pack['frames']:
            frame = cv2.imread(still)
            video.write(frame)

        cv2.destroyAllWindows()
        video.release()

        for still in game_pack['frames']:
            os.remove(still)

# EOF
