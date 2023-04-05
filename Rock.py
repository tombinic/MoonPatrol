from Actor import Actor
from Bullet import Bullet
from random import randint
import Constants

class Rock(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._count = randint(Constants.MIN_RANGE_TYPE_ROCK, Constants.MAX_RANGE_TYPE_ROCK)
        self._x_in_sprites, self._y_in_sprites = 0, 0
        self._count_bullet = 0
        self._dx = 0
        self.rock_type()
        self._arena = arena
        arena.add(self)

    def move(self):
        self._dx = Constants.SPEED_LAND
        self._x -= self._dx
        if self._x < 0 - self._w:
            self._arena.remove(self)
        
    def collide(self, other):
        """Se la roccia piccola è stata colpita 1 volta da un missile viene distrutta.
        Se la roccia è grande deve essere colpita 2 volte
        """
        if isinstance(other, Bullet):
            self._count_bullet += 1
            if self._count % 2 == 0:
                self._arena.remove(self)
            else:
                if self._count_bullet == Constants.MAX_HITTED_TIMES_ROCK:
                    self._count_bullet = 0
                    self._arena.remove(self)
        else:
            pass
        
    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return self._x_in_sprites, self._y_in_sprites, self._w, self._h
        
    def rock_type(self):
        """Definisce le dimensioni della roccia: piccola o grande"""
        if self._count % 2 == 0:
            self._x_in_sprites, self._y_in_sprites = Constants.X_ROCK, Constants.Y_ROCK
            self._w, self._h = Constants.W_ROCK, Constants.H_ROCK
        else:
            self._x_in_sprites, self._y_in_sprites = Constants.X_ROCK_BIGGER, Constants.Y_ROCK_BIGGER
            self._w, self._h = Constants.W_ROCK_BIGGER, Constants.H_ROCK_BIGGER

    def is_bigger(self):
        return self._count % 2
