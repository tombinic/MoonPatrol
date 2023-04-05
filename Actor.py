class Actor():

    def move(self):
        raise NotImplementedError('Abstract method')

    def collide(self, other: 'Actor'):
        raise NotImplementedError('Abstract method')

    def position(self) -> (int, int, int, int):
        raise NotImplementedError('Abstract method')

    def symbol(self) -> (int, int, int, int):
        raise NotImplementedError('Abstract method')