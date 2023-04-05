from Arena import Arena
from Rover import Rover
from Hole import Hole
from Rock import Rock
from Alien import Alien
from Monster import Monster
from random import randrange
from random import randint
import Constants

class MoonPatrolGame:
    """Classe che istanzia i personaggi, gestisce il gioco"""
    def __init__(self):
        self._arena = Arena((Constants.W_ARENA, Constants.H_ARENA))
        self._rover = Rover(self._arena, (0, self._arena.size()[1] - Constants.H_LAND))
        self._random = randrange(Constants.SPAWN_MIN_RANDOM_RANGE, Constants.SPAWN_MAX_RANDOM_RANGE, 2)
        self._mins = Constants.DEFAULT_MINS
        self._secs = Constants.DEFAULT_SECS
        self._total_points, self._ticks = 0, 0
        self._alien, self._monster = None, None
     
    def arena(self):
        return self._arena
        
    def rover(self):
        return self._rover 

    def monster(self):
        return self._monster

    def attacks(self):
        for i in self._arena.actors():
            if isinstance(i, Alien):
                i.attack()
            elif isinstance(i, Monster):
                i.attack()
        
    def rover_attacks(self):
        for i in self._arena.actors():
            if isinstance(i, Rover):
                i.attack()

    def spawn_alien(self):
        pos = 0
        if not(self.are_there_aliens()):
            for i in range(0, Constants.MAX_N_ALIEN): 
                self._alien = Alien(self._arena, (pos, 0 + Constants.W_ALIEN))
                pos += Constants.POS_ALIEN

    def are_there_aliens(self):
        """Controlla se sono presenti alieni nell'arena"""
        n_aliens = 0
        for i in self._arena.actors():
            if isinstance(i, Alien):
                n_aliens += 1
        return n_aliens > 0

    def are_there_monsters(self):
        """Controlla se sono presenti mostri nell'arena"""
        n_monsters = 0
        for i in self._arena.actors():
            if isinstance(i, Monster):
                n_monsters += 1
        return n_monsters > 0

    def spawn_monster(self):
        if not(self.are_there_monsters()):
            self._monster = Monster(self._arena, (self._arena.size()[1], self._arena.size()[1] - Constants.H_LAND - Constants.H_MONSTER))

    def spawn_rock(self):
        self._random -= Constants.SPAWN_RATE_ROCK
        if self._random == 0:
            self._random = randrange(Constants.SPAWN_MIN_RANDOM_RANGE, Constants.SPAWN_MAX_RANDOM_RANGE, 2)
            if self._random > Constants.MIN_SPAWN_RATE_ROCK and self._random <= Constants.MAX_SPAWN_RATE_ROCK:
                Rock(self._arena, (Constants.W_ARENA, self._arena.size()[1] - Constants.H_LAND - 18))

    def spawn_hole(self):
        self._random -= Constants.SPAWN_RATE_HOLE
        if self._random == 0:
            self._random = randrange(Constants.SPAWN_MIN_RANDOM_RANGE, Constants.SPAWN_MAX_RANDOM_RANGE, 2)
            if self._random >= Constants.MIN_SPAWN_RATE_HOLE and self._random <= Constants.MAX_SPAWN_RATE_HOLE:
                Hole(self._arena, (Constants.W_ARENA, self._arena.size()[1] - Constants.H_LAND - 5))    

    def get_total_points(self):
        if self._ticks == Constants.FPS / 2:
            self._total_points += Constants.POINTS
        return self._total_points

    def survive_time(self):
        self._ticks += 1
        if self._ticks == Constants.FPS:
            self._ticks = 0
            self._secs -= 1
            if self._secs == 0 and self._mins >= 1:
                self._secs = 59
                self._mins -= 1
        return (self._mins, self._secs)

    def have_lost(self):
        return self._rover.is_died()

    def have_won(self):
        return self._mins == 0 and self._secs == -1