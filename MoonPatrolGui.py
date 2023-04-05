import Constants
from MoonPatrolGame import MoonPatrolGame
import g2d

class MoonPatrolGui:
    def __init__(self, moon_patrol: MoonPatrolGame):
        """Classe che gestisce la grafica del gioco MoonPatrol"""
        self._moon_patrol = moon_patrol
        self._arena = self._moon_patrol.arena()
        self._rover = self._moon_patrol.rover()
        self._is_jumped = False
        self._ticks = 0
        self._land_limit, self._mountain_limit, self._blue_mountain_limit = 0, 0, 0 
        self._sprites_car = g2d.load_image(Constants.SPRITES_CAR)
        self._sprites_land = g2d.load_image(Constants.SPRITES_LAND)

    def draw_all(self):
        """Disegna i tre livelli di sfondo e tutti i personaggi dell'arena"""
        g2d.clear_canvas()

        g2d.draw_image_clip(self._sprites_land, (Constants.X_BLUE_MOUNTAIN, Constants.Y_BLUE_MOUNTAIN, Constants.W_BLUE_MOUNTAIN, Constants.H_BLUE_MOUNTAIN), (self._blue_mountain_limit, self._arena.size()[1] - Constants.HIGH_MOUNTAIN * 2 - Constants.H_BLUE_MOUNTAIN, Constants.W_BLUE_MOUNTAIN, Constants.H_BLUE_MOUNTAIN))
        g2d.draw_image_clip(self._sprites_land, (Constants.X_BLUE_MOUNTAIN, Constants.Y_BLUE_MOUNTAIN, Constants.W_BLUE_MOUNTAIN, Constants.H_BLUE_MOUNTAIN), (self._arena.size()[0] + self._blue_mountain_limit, self._arena.size()[1] - Constants.HIGH_MOUNTAIN * 2 - Constants.H_BLUE_MOUNTAIN, Constants.W_BLUE_MOUNTAIN, Constants.H_BLUE_MOUNTAIN))
        
        g2d.draw_image_clip(self._sprites_land, (Constants.X_MOUNTAIN, Constants.Y_MOUNTAIN, Constants.W_MOUNTAIN, Constants.H_MOUNTAIN), (self._mountain_limit, self._moon_patrol.arena().size()[1] - Constants.HIGH_MOUNTAIN - Constants.H_MOUNTAIN, Constants.W_MOUNTAIN, Constants.H_MOUNTAIN))
        g2d.draw_image_clip(self._sprites_land, (Constants.X_MOUNTAIN, Constants.Y_MOUNTAIN, Constants.W_MOUNTAIN, Constants.H_MOUNTAIN), (self._arena.size()[0] + self._mountain_limit, self._arena.size()[1] - Constants.HIGH_MOUNTAIN - Constants.H_MOUNTAIN, Constants.W_MOUNTAIN, Constants.H_MOUNTAIN))

        g2d.draw_image_clip(self._sprites_land, (Constants.X_LAND, Constants.Y_LAND, Constants.W_LAND, Constants.H_LAND), (self._land_limit, self._arena.size()[1] - Constants.H_LAND, Constants.W_LAND, Constants.H_LAND))
        g2d.draw_image_clip(self._sprites_land, (Constants.X_LAND, Constants.Y_LAND, Constants.W_LAND, Constants.H_LAND), (self._arena.size()[0] + self._land_limit, self._arena.size()[1] - Constants.H_LAND, Constants.W_LAND, Constants.H_LAND))

        for a in self._arena.actors():
            g2d.draw_image_clip(self._sprites_car, a.symbol(), a.position())

        if(self._land_limit * - 1 >= self._arena.size()[0]):
            self._land_limit = 0
        if(self._mountain_limit * -1 >= self._arena.size()[0]):
            self._mountain_limit = 0
        if(self._blue_mountain_limit * -1 >= self._arena.size()[0]):
            self._blue_mountain_limit = 0

        self._land_limit -= Constants.SPEED_LAND
        self._mountain_limit -= Constants.SPEED_MOUNTAIN
        self._blue_mountain_limit -= Constants.SPEED_BLUE_MOUNTAIN
    
    def spawn_hole(self): 
        self._moon_patrol.spawn_hole()

    def spawn_rock(self): 
        self._moon_patrol.spawn_rock()
    
    def spawn_alien(self):
        self._moon_patrol.spawn_alien()

    def spawn_monster(self):
        self._moon_patrol.spawn_monster()

    def enemies_attack(self):
        self._moon_patrol.attacks()

    def check_end(self):
        if self._moon_patrol.have_won():
            g2d.alert(Constants.WIN + str(self._moon_patrol.get_total_points()) + " points.")
            g2d.close_canvas()
        elif self._moon_patrol.have_lost():
            g2d.alert(Constants.LOSE + str(self._moon_patrol.get_total_points()) + " points.")
            g2d.close_canvas()       

    def draw_time(self):
        var = self._moon_patrol.survive_time()
        timeformat = '{:02d}:{:02d}'.format(var[0], var[1])
        g2d.draw_text("TIME: " + str(timeformat), (Constants.X_TIME, Constants.Y_TIME), Constants.DIM_TIME)

    def draw_points(self):
        g2d.draw_text("SCORE: " + str(self._moon_patrol.get_total_points()), (Constants.X_POINTS, Constants.Y_POINTS), Constants.DIM_POINTS)

    def tick(self):
        self.spawn_alien()
        self.spawn_monster()
        self.control_game()
        self.spawn_hole()
        self.spawn_rock()  
        self.enemies_attack() 
        self._arena.move_all()
        self.draw_all()
        self.draw_time()
        self.draw_points()
        self.check_end()

    def control_game(self):
        if g2d.key_pressed(Constants.ARROW_UP):
            self._is_jumped = g2d.key_pressed(Constants.ARROW_UP)
        elif g2d.key_pressed(Constants.ARROW_RIGHT):
            self._rover.go_right()
        elif g2d.key_pressed(Constants.ARROW_LEFT):
            self._rover.go_left()
        elif g2d.key_released(Constants.ARROW_UP) and self._is_jumped == True:
            self._rover.go_up()
            self._is_jumped = not (g2d.key_pressed(Constants.ARROW_UP))
        elif g2d.key_pressed(Constants.SPACE_BAR):
            self._moon_patrol.rover_attacks()
        elif (g2d.key_released(Constants.ARROW_UP) or
            g2d.key_released(Constants.ARROW_RIGHT) or
            g2d.key_released(Constants.ARROW_LEFT)):
            self._rover.stay()

def gui(game: MoonPatrolGame):
    g2d.init_canvas(game.arena().size())
    gui = MoonPatrolGui(game)
    g2d.main_loop(gui.tick, Constants.FPS)

