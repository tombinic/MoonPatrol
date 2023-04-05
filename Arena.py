from Actor import Actor

class Arena():

    def __init__(self, size: (int, int)):
        self._w, self._h = size
        self._actors = []
        self._return = False

    def add(self, a: Actor):
        if a not in self._actors:
            self._actors.append(a)

    def remove(self, a: Actor):
        if a in self._actors:
            self._actors.remove(a)

    def move_all(self):
        actors = list(reversed(self._actors))
        for a in actors:
            a.move()         
            for other in actors:
                if other is not a and self.check_collision(a, other):
                        a.collide(other)
                        other.collide(a)
                        
    def check_collision(self, a1: Actor, a2: Actor) -> bool:
        x1, y1, w1, h1 = a1.position()
        x2, y2, w2, h2 = a2.position()
        return (y2 < y1 + h1 and y1 < y2 + h2
            and x2 < x1 + w1 and x1 < x2 + w2
            and a1 in self._actors and a2 in self._actors)

    def actors(self) -> list:
        return list(self._actors)

    def size(self) -> (int, int):
        return (self._w, self._h)