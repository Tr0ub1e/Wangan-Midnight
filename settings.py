class Settings():

    def __init__(self):

        self.res = (1280, 720)

        self.FPS = 60
        self.color_line = (255,255,255)
        self.chords_lines = [

                         (self.res[0]*7/16, self.res[1]/2), (0, self.res[1]*7/9),

                         (self.res[0]/2, self.res[1]/2), (self.res[0]/2, self.res[1]),

                         (self.res[0]*9/16, self.res[1]/2), (self.res[0], self.res[1]*7/9),

                         #for road
                         (self.res[0]+400, self.res[1]), (-400, self.res[1])

                                ]

        self.color_bg = (128,128,128)
        self.color_road = (64,64,64)
        self.color_imitate_speed = (255,32,64)

        #self.color_clouds = (15,181,247)
        #self.chords_clouds = (0, 0, self.res[0], self.res[1]/2)
