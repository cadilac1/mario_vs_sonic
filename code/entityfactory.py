from code.background import Background
from code.player import Player
from code.enemy import Enemy


class EntityFactory:

    @staticmethod
    def get_entity(name):

        if name == "Background":
            return Background()

        if name == "Player":
            return Player()

        if name == "Enemy":
            return Enemy()

        return None