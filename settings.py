from os import getcwd

class Settings():

    def __init__(self):

        self.res = (1280, 720)

        self.FPS = 30

        self.sound = getcwd()+"\\music\\strange.mp3"

        self.chords_lines = [
                        #left side (from bottom to mid)
                        [-240, 720], [0, 560], [120, 540], [240, 520], [360, 500], [480, 480], [600, 460],
                        #right side (from mid to bottom)
                        [680, 460], [800, 480], [920, 500], [1040, 520], [1160, 540], [1280, 560], [1520, 720]
                                ]

        self.chords_lines2 = [
                        #left side (from bottom to mid)
                        [0, 720], [320, 560], [380, 540], [440, 520], [500, 500], [560, 480], [620, 460],
                        #right side (from mid to bottom)
                        [660, 460], [700, 480], [780, 500], [840, 520], [900, 540], [960, 560], [1280, 720]
                                ]


        self.chords_bg = [
                        (0, 360), (1280, 360), (1280, 720), (0, 720)
                        ]

        self.color_bg = (150,0,150)
        self.color_rd = (0,0,0)
        self.color_imitate_speed = (0,0,0)#(25,25,25)
