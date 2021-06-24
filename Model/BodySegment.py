from pygame.rect import Rect

class BodySegment(Rect):

    def __init__(self,left,top,width,height):
        super().__init__(left,top,width,height)