from Actor import Actor
from Bullet import Bullet
from random import randrange
from random import randint
import Constants

class Alien(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._dx = Constants.SPEED_LAND
        self._x_in_sprites, self._y_in_sprites = 0, 0
        self._count_movement = 0
        self._count = randint(Constants.MIN_RANGE_TYPE_ALIEN, Constants.MAX_RANGE_TYPE_ALIEN)
        self._count_bullet = randrange(Constants.SPAWN_MIN_RANDOM_RANGE, Constants.SPAWN_MAX_RANDOM_RANGE, Constants.ATTACK_RATE_ALIEN)
        self.alien_type()
        self._arena = arena
        arena.add(self)

    def move(self): 
        """Movimento casuale dell'alieno: se però urta uno dei due bordi torna indietro"""
        self._count_movement = randint(Constants.MOVEMENT_ALIEN_X, Constants.MOVEMENT_ALIEN_Y)
        if self._x + self._dx > Constants.W_ARENA - self._w or self._x + self._dx < 0 or (self._count_movement >= 0 and self._count_movement <= 1):           
            self._dx = -self._dx
        self._x += self._dx

    def collide(self, other):
        if isinstance(other, Alien):
            self._dx = -self._dx
        else:
            self._arena.remove(self)

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return self._x_in_sprites, self._y_in_sprites, self._w, self._h

    def alien_type(self):
        """Definisce il tipo di alieno"""
        if self._count % 2 == 0:
            self._x_in_sprites, self._y_in_sprites = Constants.X_ALIEN, Constants.Y_ALIEN
            self._w, self._h = Constants.W_ALIEN, Constants.H_ALIEN
        else:
            self._x_in_sprites, self._y_in_sprites = Constants.X_ALIEN_2, Constants.Y_ALIEN_2
            self._w, self._h = Constants.W_ALIEN_2, Constants.H_ALIEN_2
    
    def get_casual_movement(self):
        return self._count_movement

    def is_died(self):
        return not(self in self._arena.actors())
    
    def get_alien_type(self):
        return self._count % 2

    def attack(self):
        self._count_bullet -= Constants.ATTACK_RATE_ALIEN
        if self._count_bullet == 0:
            self._count_bullet = randrange(Constants.SPAWN_MIN_RANDOM_RANGE, Constants.SPAWN_MAX_RANDOM_RANGE, Constants.ATTACK_RATE_ALIEN)
            if self._count_bullet >= Constants.MIN_RANGE_ATTACK_ALIEN and self._count_bullet <= Constants.MAX_RANGE_ATTACK_ALIEN:
                Bullet(self._arena, (self._x, self._y + 20), Constants.BULLET_DOWN, self)
    