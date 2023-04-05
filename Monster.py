from Actor import Actor
from Rover import Rover
from Hole import Hole
from Rock import Rock
from Bullet import Bullet
from random import randrange
import Constants

class Monster(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._w, self._h = Constants.W_MONSTER, Constants.H_MONSTER
        self._speed = Constants.SPEED
        self._dx, self._dy = Constants.SPEED_LAND, 0
        self._count = randrange(Constants.SPAWN_MIN_RANDOM_RANGE, Constants.SPAWN_MAX_RANDOM_RANGE, Constants.ATTACK_RATE_MONSTER)
        self._hitted = 0
        self._arena = arena
        arena.add(self)

    def move(self):  
        self._x += self._dx
        if self._x + self._dx + self._w >= Constants.W_ARENA or self._x + self._dx + self._w <= Constants.W_ARENA / 2:          
            self._dx = -self._dx
        
        self._y += self._dy

        if self._y >= self._arena.size()[1] - self._h - Constants.H_LAND:
            self._y = self._arena.size()[1] - self._h - Constants.H_LAND

        if not (self._y >= self._arena.size()[1] - self._h - Constants.H_LAND):
            self._dy += Constants.G

    def collide(self, other):
        """In caso di collisione salta rover, buche e rocce.
        Se il mostro viene colpito esclusivamente da un proiettile sparato
        dal rover, si decrementa la vita del mostro
        """
        if isinstance(other, Hole) or isinstance(other, Rock) or isinstance(other, Rover):
            self._dy = -self._speed
        elif isinstance(other, Bullet):
            if isinstance(other.get_shot_from(), Rover):
                self._hitted += Constants.HITTED_MONSTER
        if self._hitted == Constants.MAX_LIFE_MONSTER:
            self._arena.remove(self) 
    
    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return Constants.X_MONSTER, Constants.Y_MONSTER, self._w, self._h
        
    def is_died(self):
        return not(self in self._arena.actors())

    def attack(self):
        self._count -= Constants.ATTACK_RATE_MONSTER
        if self._count == 0:
            self._count = randrange(Constants.SPAWN_MIN_RANDOM_RANGE, Constants.SPAWN_MAX_RANDOM_RANGE, Constants.ATTACK_RATE_MONSTER)
            if self._count >= Constants.MIN_RANGE_ATTACK_MONSTER and self._count <= Constants.MAX_RANGE_ATTACK_MONSTER:
                Bullet(self._arena, (self._x - self._w, self._y - 5), Constants.BULLET_LEFT, self)