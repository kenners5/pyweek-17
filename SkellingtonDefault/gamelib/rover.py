import random
import pygame

from util import layer_obj

class Rover:
    def __init__(self, _name="rover"):
        self.name = _name
        self.layer = layer_obj(self.name)
        self.surface = None
        self.location = None

    def load(self, game_pack, image):
        self.layer.surface = pygame.image.load(image)
        self.layer.location = self.layer.surface.get_rect()

        # Move to random start location
        new_x = random.random() * (game_pack['dims']['x']-self.layer.surface.get_width())
        new_y = random.random() * (game_pack['dims']['y']-self.layer.surface.get_height())
        self.layer.stamp("Initializing head to %s" % repr([int(new_x), int(new_y)]))
        self.layer.location = self.layer.location.move([int(new_x), int(new_y)])

    def step(self, game_pack):
        """ Prepare the rover for interaction with other things """
        pass

    def render(self, game_pack):
        """ Prepare the layer for blitting """
        self.layer.stamp("Current loc: %s" % repr([self.layer.location.left, self.layer.location.right]))
        self.layer.location = self.layer.location.move(self.layer.speed)
        if self.layer.location.left < 0 or self.layer.location.right > game_pack['dims']['x']:
            self.layer.speed[0] = -self.layer.speed[0]
        if self.layer.location.top < 0 or self.layer.location.bottom > game_pack['dims']['y']:
            self.layer.speed[1] = -self.layer.speed[1]

        # Output the surface and the loc
        return self.layer.surface, self.layer.location

# EOF
