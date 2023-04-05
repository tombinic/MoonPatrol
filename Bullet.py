from Actor import Actor
from Hole import Hole
from random import randint
import Constants

class Bullet(Actor):
    def __init__(self, arena, pos, direction, shot_from):
        self._shot_from = shot_from
        self._x, self._y = pos
        self._w, self._h = Constants.W_BULLET, Constants.H_BULLET
        self._dx, self._dy = Constants.SPEED_BULLET_ENEMIES, Constants.SPEED_BULLET_ENEMIES
        self._count = 0
        self._direction = direction
        self._arena = arena
        arena.add(self)

    def move(self):
        """Movimento in 4 direzioni: ogni tanto un missile può generare delle buche"""
        if self._direction == Constants.BULLET_RIGHT:
            self._dx = Constants.SPEED_BULLET
            self._x += self._dx
        elif self._direction == Constants.BULLET_UP:
            self._dy = Constants.SPEED_BULLET   
            self._y -= self._dy
        elif self._direction == Constants.BULLET_DOWN:
            self._y += self._dy
        elif self._direction == Constants.BULLET_LEFT:
            self._x -= self._dx

        if self._x > Constants.W_ARENA or self._y < 0 or self._x < 0:
            self._arena.remove(self)
        if self._y >= self._arena.size()[1] - Constants.H_LAND - self._h:
            self._count = randint(Constants.RANGE_CREATE_HOLE1, Constants.RANGE_CREATE_HOLE2)
            self._arena.remove(self)
            if self._count % 2 == 0:
                Hole(self._arena, (self._x, self._arena.size()[1] - Constants.H_LAND - 5)) 
               
    def collide(self, other):
        self._arena.remove(self)

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return Constants.X_BULLET, Constants.Y_BULLET, self._w, self._h
    
    def get_shot_from(self):
        return self._shot_from