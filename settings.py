from os import getcwd

class Settings():

    def __init__(self):

        self.res = (1280, 720)

        self.FPS = 60

        self.sound = getcwd()+"\\music\\strange.mp3"
        self.start_sound = getcwd()+"\\music\\start.mp3"

        self.chords_lines = [
                        #left side (from bottom to mid)
                        [-240, 720], [0, 530], [120, 520], [240, 510], [360, 500], [480, 480], [620, 470],
                        #right side (from mid to bottom)
                        [660, 470], [800, 480], [920, 500], [1040, 510], [1160, 520], [1280, 530], [1520, 720]
                                ]

        self.chords_lines2 = [
                        #left side (from bottom to mid)
                        [0, 720], [320, 560], [380, 540], [440, 520], [500, 500], [560, 480], [620, 470],
                        #right side (from mid to bottom)
                        [660, 470], [700, 480], [780, 500], [840, 520], [900, 540], [960, 560], [1280, 720]
                                ]


        self.chords_bg = [
                        (0, 360), (1280, 360), (1280, 720), (0, 720)
                        ]

        self.color_bg = (150,0,150)
        self.color_rd = (0,0,0)
        self.color_imitate_speed = (45,45,45,196)#(20,20,20,196)#(25,25,25)
