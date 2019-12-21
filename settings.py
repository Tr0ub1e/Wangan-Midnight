from os import getcwd

class Settings():

    def __init__(self):

        self.res = (1280, 720)

        self.FPS = 60

        self.sound = getcwd()+"\\music\\strange.mp3"
        self.tree = getcwd()+"\\images\\tree.png"

        self.chords_lines = [
                        #left side (from bottom to mid)
                        [-500, 720], [100, 570], [200, 540], [300, 510], [400, 480], [500, 450], [610, 400],

                        #right side (from mid to bottom)
                        [670, 400], [780, 450], [880, 480], [980, 510], [1080, 540], [1180, 570], [1780, 720]
                                ]

        self.chords_bg = [
                        (0, 360), (1280, 360), (1280, 720), (0, 720)
                        ]

        self.color_bg = (150,0,150)
        self.color_rd = (250,250,250)
        self.color_imitate_speed = (25,25,25)
