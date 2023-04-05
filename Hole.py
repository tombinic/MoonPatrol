from Actor import Actor
from random import randint
import Constants

class Hole(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._count = randint(Constants.MIN_RANGE_TYPE_HOLE, Constants.MAX_RANGE_TYPE_HOLE)
        self._x_in_sprites, self._y_in_sprites = 0, 0
        self.hole_type()
        self._dx = 0
        self._arena = arena
        arena.add(self)

    def move(self):
        self._dx = Constants.SPEED_LAND
        self._x -= self._dx
        if self._x < 0 - self._w:
            self._arena.remove(self)
        
    def collide(self, other):
        pass

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return self._x_in_sprites, self._y_in_sprites, self._w, self._h

    def hole_type(self):
        """Definisce le dimensioni della buca: piccola o grande"""
        if self._count % 2 == 0:
            self._x_in_sprites, self._y_in_sprites = Constants.X_HOLE, Constants.Y_HOLE
            self._w, self._h = Constants.W_HOLE, Constants.H_HOLE
        else:
            self._x_in_sprites, self._y_in_sprites = Constants.X_HOLE_BIGGER, Constants.Y_HOLE_BIGGER
            self._w, self._h = Constants.W_HOLE_BIGGER, Constants.H_HOLE_BIGGER
    
    def is_bigger(self):
        return self._count % 2
    