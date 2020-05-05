class g_map():
    i = 0
    def shutoko_map(self):
        self.i += 1
        lst = ['left', None, 'left', 'right', 'right', None]
        return lst[self.i % len(lst) - 1]
