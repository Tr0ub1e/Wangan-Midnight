from os import getcwd

class Settings():

    def __init__(self):

        self.res = (1280, 720)

        self.FPS = 60

        self.sound = getcwd()+"\\music\\strange.mp3"

        self.chords_lines = [
                        #left side (from bottom to mid)
                        [-100, 720], [0, 680], [100, 640], [200, 600], [300, 560], [400, 520], [550, 480],
                        #right side (from mid to bottom)
                        [720, 480], [880, 520], [980, 560], [1080, 600], [1180, 640], [1280, 680], [1380, 720]
                                ]


        self.chords_bg = [
                        (0, 360), (1280, 360), (1280, 720), (0, 720)
                        ]

        self.color_bg = (150,0,150)
        self.color_rd = (0,0,0)
        self.color_imitate_speed = (25,25,25)
