from os import getcwd

class Settings():

    def __init__(self):

        self.res = (1280, 720)

        self.FPS = 120
        #self.sound = "C:\\Users\\Tr0ub1e\\Desktop\\Wangan Midnight\\music\\strange.mp3"
        self.sound = getcwd()+"\\music\\strange.mp3"

        self.chords_lines = [
                        #left side (from bottom to mid)
                        [-200, 820], [195, 680], [387, 600], [610, 575],

                        #right side (from mid to bottom)
                        [670, 575], [892, 600], [1085, 680], [1480, 820]

                                ]

        self.chords_bg = [
                        (0, 360), (1280, 360), (1280, 720), (0, 720)
                        ]

        self.color_bg = (153,0,153)
        self.color_rd = (40,0,0)
        self.color_imitate_speed = (51,0,51)
