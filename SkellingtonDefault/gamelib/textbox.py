import constants
from util import layer_obj

class TextBox():
    def __init__(self, name = "Unnamed"):
        self.name = name
        self.layer = layer_obj(name+"_layer")

    def load(self, game_pack, **kwargs):
        """As the first load, run a step"""
        self.step(game_pack)

    def step(self, game_pack):
        message = game_pack["textbox_" + self.name]
        self.layer.surface = game_pack['font'].render(message,
                                                      1,
                                                      constants.WHITE)
        self.layer.location = self.layer.surface.get_rect()

    def render(self, game_pack):
        return self.layer.surface, self.layer.location

# EOF
