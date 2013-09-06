import constants

class layer_obj():
    """ The main class that holds a layer """
    def __init__(self, name = "Unnamed"):
        self.name = name
        self.surface = None
        self.location = None
        self.size = 800, 600
        self.speed = [2, 2]

    def stamp(self, message):
        if constants.debug:
            print '%s: %s' % (self.name, message)

# EOF
