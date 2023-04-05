from Actor import Actor
from Bullet import Bullet
import Constants

class Rover(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._w, self._h = Constants.W_ROVER, Constants.H_ROVER
        self._state = Constants.ROVER_NULL
        self._speed = Constants.SPEED
        self._dx, self._dy = 0, 0
        self._arena = arena
        arena.add(self)

    def move(self):     
        self._y += self._dy

        if self._dy > 0:
            self._state = Constants.ROVER_DOWN
        if self._y < 0:
            self._y = 0
        elif self._y >= self._arena.size()[1] - self._h - Constants.H_LAND:
            self._y = self._arena.size()[1] - self._h - Constants.H_LAND
            self._state = Constants.ROVER_NULL

        self._x += self._dx
        if self._x < 0:
            self._x = 0
        elif self._x > self._arena.size()[0] - self._w:
            self._x = self._arena.size()[0] - self._w
        
        if not (self._y >= self._arena.size()[1] - self._h - Constants.H_LAND):
            self._dy += Constants.G
        
    def go_left(self):
        self._dx = -self._speed
        self._dy = 0

    def go_right(self):
        self._dx = +self._speed
        self._dy = 0

    def go_up(self):
        self._state = Constants.ROVER_UP
        if(self._y >= self._arena.size()[1] - self._h - Constants.H_LAND):
            self._dx = 0
            self._dy = -self._speed

    def stay(self):
        self._dx, self._dy = 0, 0

    def collide(self, other):
        self._arena.remove(self)  
    
    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        if self._state == Constants.ROVER_UP:
            return Constants.X_CAR_UP, Constants.Y_CAR_UP, self._w, self._h
        elif self._state == Constants.ROVER_DOWN:
            return Constants.X_CAR_DOWN, Constants.Y_CAR_DOWN, self._w, self._h
        else: 
            return Constants.X_CAR, Constants.Y_CAR, self._w, self._h

    def attack(self):
        Bullet(self._arena, (self._x + self._w, self._y + 10), Constants.BULLET_RIGHT, self)
        Bullet(self._arena, (self._x, self._y - 20), Constants.BULLET_UP, self)
    
    def is_died(self):
        return not(self in self._arena.actors())

