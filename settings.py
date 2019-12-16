class Settings():

    def __init__(self):

        self.res = (1280, 720)

        self.FPS = 120

        self.sound = "C:\\Users\\Tr0ub1e\\Desktop\\Wangan Midnight\\music\\strange.mp3"

        self.chords_lines = [
                        #left side (from bottom to mid)
                        [-1000, 720], [135, 515], [357, 437], [610, 360],

                        #right side (from mid to bottom)
                        [670, 360], [922, 437], [1145, 515], [2280, 720]

                                ]

        self.chords_bg = [
                        (0, 360), (1280, 360), (1280, 720), (0, 720)
                        ]

        self.color_bg = (128,128,128)
        self.color_rd = (64,64,64)
        self.color_imitate_speed = (96,96,96)
