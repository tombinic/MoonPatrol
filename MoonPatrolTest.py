from unittest import TestCase, main
from Rover import Rover
from Arena import Arena
from Rock import Rock
from Hole import Hole
from Bullet import Bullet
from Hole import Hole
from Alien import Alien
import Constants

arena = Arena((Constants.W_ARENA, Constants.H_ARENA))
pos = (0 , Constants.H_ARENA - Constants.H_LAND - Constants.H_ROVER)

class MoonPatrolTest(TestCase):
    
    def test_rover(self):
        rover = Rover(arena, pos)
        rover.go_right()
        rover.move()
        self.assertTrue(rover.position() == (pos[0] + Constants.SPEED, pos[1], Constants.W_ROVER, Constants.H_ROVER))
        self.assertTrue(rover.symbol() == (Constants.X_CAR, Constants.Y_CAR, Constants.W_ROVER, Constants.H_ROVER))
        rover.go_left()
        rover.move()
        self.assertTrue(rover.position() == (pos[0], pos[1], Constants.W_ROVER, Constants.H_ROVER))
        rover.go_up()
        rover.move()
        self.assertTrue(rover.position() == (pos[0], pos[1] - Constants.SPEED, Constants.W_ROVER, Constants.H_ROVER))
        self.assertTrue(rover.symbol() == (Constants.X_CAR_UP, Constants.Y_CAR_UP, Constants.W_ROVER, Constants.H_ROVER))
        rover.collide(Hole(arena, pos))
        self.assertTrue(rover.is_died())
    
    def test_rock(self):
        rock = Rock(arena, pos)
        rock.move()
        if rock.is_bigger():
            rock.collide(Bullet(arena, pos, Constants.BULLET_RIGHT, self))
            rock.collide(Bullet(arena, pos, Constants.BULLET_RIGHT, self))
            self.assertTrue(rock not in arena.actors())
            self.assertTrue(rock.symbol() == (Constants.X_ROCK_BIGGER, Constants.Y_ROCK_BIGGER, Constants.W_ROCK_BIGGER, Constants.H_ROCK_BIGGER))
            self.assertTrue(rock.position() == (pos[0] - Constants.SPEED_LAND, pos[1], Constants.W_ROCK, Constants.H_ROCK))
        else:
            rock.collide(Bullet(arena, pos, Constants.BULLET_RIGHT, self))
            self.assertTrue(rock.position() == (pos[0] - Constants.SPEED_LAND, pos[1], Constants.W_ROCK_BIGGER, Constants.H_ROCK_BIGGER))
            self.assertTrue(rock not in arena.actors())
            self.assertTrue(rock.symbol() == (Constants.X_ROCK, Constants.Y_ROCK, Constants.W_ROCK, Constants.H_ROCK))

    def test_hole(self):
        hole = Hole(arena, pos)
        hole.move()
        if hole.is_bigger():
            self.assertTrue(hole.position() == (pos[0] - Constants.SPEED_LAND, pos[1], Constants.W_HOLE_BIGGER, Constants.H_HOLE_BIGGER))
            self.assertTrue(hole.symbol() == (Constants.X_HOLE_BIGGER, Constants.Y_HOLE_BIGGER, Constants.W_HOLE_BIGGER, Constants.H_HOLE_BIGGER))
        else:
            self.assertTrue(hole.position() == (pos[0] - Constants.SPEED_LAND, pos[1], Constants.W_HOLE, Constants.H_HOLE))
            self.assertTrue(hole.symbol() == (Constants.X_HOLE, Constants.Y_HOLE, Constants.W_HOLE, Constants.H_HOLE))
    
    def test_bullet(self):
        bullet = Bullet(arena, pos, Constants.BULLET_RIGHT, self)
        bullet.move()
        self.assertTrue(bullet.position() == (pos[0] + Constants.SPEED_BULLET, pos[1], Constants.W_BULLET, Constants.H_BULLET))
        self.assertTrue(bullet.symbol() == (Constants.X_BULLET, Constants.Y_BULLET, Constants.W_BULLET, Constants.H_BULLET))
        bullet.collide(Rover(arena, pos))
        self.assertTrue(bullet not in arena.actors())
        bullet = Bullet(arena, pos, Constants.BULLET_UP, self)
        bullet.move()
        self.assertTrue(bullet.position() == (pos[0], pos[1] - Constants.SPEED_BULLET, Constants.W_BULLET, Constants.H_BULLET))
        bullet = Bullet(arena, pos, Constants.BULLET_DOWN, self)
        bullet.move()
        self.assertTrue(bullet.position() == (pos[0], pos[1] + Constants.SPEED_BULLET, Constants.W_BULLET, Constants.H_BULLET))
    
    def test_alien(self):
        alien = Alien(arena, pos)
        alien.move()
        if not(alien.get_alien_type()):
            if alien.get_casual_movement() >= 0 and alien.get_casual_movement() <= 1:
                self.assertTrue(alien.position() == (pos[0] - Constants.SPEED_LAND, pos[1], Constants.W_ALIEN, Constants.H_ALIEN))
            else:
                self.assertTrue(alien.position() == (pos[0] + Constants.SPEED_LAND, pos[1], Constants.W_ALIEN, Constants.H_ALIEN))
            self.assertTrue(alien.symbol() == (Constants.X_ALIEN, Constants.Y_ALIEN, Constants.W_ALIEN, Constants.H_ALIEN))
        else:
            if alien.get_casual_movement() >= 0 and alien.get_casual_movement() <= 1:
                self.assertTrue(alien.position() == (pos[0] - Constants.SPEED_LAND, pos[1], Constants.W_ALIEN_2, Constants.H_ALIEN_2))
            else:
                self.assertTrue(alien.position() == (pos[0] + Constants.SPEED_LAND, pos[1], Constants.W_ALIEN_2, Constants.H_ALIEN_2))
            self.assertTrue(alien.symbol() == (Constants.X_ALIEN_2, Constants.Y_ALIEN_2, Constants.W_ALIEN_2, Constants.H_ALIEN_2))      
        alien.collide(Bullet(arena, pos, Constants.BULLET_RIGHT, self))
        self.assertTrue(alien.is_died())

    
if __name__ == '__main__':
    main()