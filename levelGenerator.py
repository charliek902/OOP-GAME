# 1/2 of all tanks will be red, 1/3 will be blue and 1/6 will be green (order of powers and difficuly)

# this will be a factory class which will make numerous enemies
class levelGenerator():
    def __init__(self):
        self.level = 1
        self.tanks = 6
        self.red_tanks = 3
        self.enemy_health = 50
        self.blue_tanks = 2
        self.green_tanks = 1
        self.remaining_tanks = 6
        self.MAX = 96
        self.rendering = False
    def create_tanks(self):
        print('creates the tanks here with the level generation')
        # we should not go above the maximum amount of tanks, instead we should decrease the time between waves 
        # and increase enemy player health 
        self.create_wave()

    def level_up(self):
        self.level += 1
        self.tanks *= 2
        self.red_tanks *= 2
        self.blue_tanks *= 2
        self.green_tanks = 2
        self.create_tanks()
    
    def update_level(self):
        # need to get the number of tanks left on the screen
        if self.remaining_tanks == 0:
            self.render_level_up()
            self.level_up()
    
    def render_level_up(self):
        self.rendering = True
        print('levelling up side of things appear on the screen')
    
    def create_wave(self):
        # each wave should ideally have the maximum 10 seconds between waves 
        # each wave should be spaced out 
        # with evey level we need to also increase enemy health as well
        print('waves of enemies created!')


    



