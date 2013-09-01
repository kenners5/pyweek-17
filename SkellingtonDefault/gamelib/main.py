'''Game main module.

Contains the entry point used by the run_game.py script.

Feel free to put all your game code here, or in other modules in this "gamelib"
package.
'''
import sys
import random
import pygame

import data
import color_defs as colors

SEED = 3.14159
DEBUG = False

class layer_obj():
    def __init__(self, name = "Unnamed"):
        self.name = name
        self.surface_obj = None
        self.location = None
        self.size = 800, 600
        self.speed = [2, 2]

    def stamp(self, message):
        if DEBUG:
            print '%s: %s' % (self.name, message)


def render_layer(loop_pack, layer):
    layer.stamp("Current loc: %s" % repr([layer.location.left, layer.location.right]))
    layer.location = layer.location.move(layer.speed)
    if layer.location.left < 0 or layer.location.right > loop_pack['dims']['x']:
        layer.speed[0] = -layer.speed[0]
    if layer.location.top < 0 or layer.location.bottom > loop_pack['dims']['y']:
        layer.speed[1] = -layer.speed[1]

def loop(loop_pack, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(colors.BLACK)
    for layer in loop_pack['layers']:
        render_layer(loop_pack, layer)
        screen.blit(layer.surface_obj, layer.location)
    pygame.display.flip()

def pygame_init(pack):
    pygame.init()    
    pack['dims'] = {'x': 800, 'y': 600}
    pack['speed'] = [2, 2]
    screen = pygame.display.set_mode([px for _, px in sorted(pack['dims'].items())])
    return screen

def pygame_head(pack, name):
    layer = layer_obj(name)
    img_obj = data.load('fry_head.png')
    layer.surface_obj = pygame.image.load(img_obj)
    layer.location = layer.surface_obj.get_rect()
    new_x = random.random() * (pack['dims']['x']-layer.surface_obj.get_width())
    new_y = random.random() * (pack['dims']['y']-layer.surface_obj.get_height())
    layer.stamp("Initializing head to %s" % repr([int(new_x), int(new_y)]))
    layer.location = layer.location.move([int(new_x), int(new_y)])
    return layer

def main():
    random.seed(SEED)
    loop_pack = {}
    print "Let's get 'fired up'!"
    screen = pygame_init(loop_pack)
    loop_pack['layers'] = []
    loop_pack['layers'].append(pygame_head(loop_pack, "head1"))
    loop_pack['layers'].append(pygame_head(loop_pack, "head2"))
    loop_pack['layers'].append(pygame_head(loop_pack, "head3"))
    loop_pack['layers'].append(pygame_head(loop_pack, "head4"))
    loop_pack['layers'].append(pygame_head(loop_pack, "head1"))
    loop_pack['layers'].append(pygame_head(loop_pack, "head2"))
    loop_pack['layers'].append(pygame_head(loop_pack, "head3"))
    loop_pack['layers'].append(pygame_head(loop_pack, "head4"))
    loop_pack['layers'].append(pygame_head(loop_pack, "head1"))
    loop_pack['layers'].append(pygame_head(loop_pack, "head2"))
    loop_pack['layers'].append(pygame_head(loop_pack, "head3"))
    loop_pack['layers'].append(pygame_head(loop_pack, "head4"))
    loop_pack['layers'].append(pygame_head(loop_pack, "head1"))
    loop_pack['layers'].append(pygame_head(loop_pack, "head2"))
    loop_pack['layers'].append(pygame_head(loop_pack, "head3"))
    loop_pack['layers'].append(pygame_head(loop_pack, "head4"))

    while 1:
        loop(loop_pack, screen)

# EOF
