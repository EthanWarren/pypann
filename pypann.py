import pygame
pygame.init()
pygame.mixer.set_num_channels(10000)
class Source() :
    def __init__(self,file) :
        self.sound=pygame.mixer.Sound(file)
        self.channel=pygame.mixer.find_channel()
        self.channel.play(self.sound,loops=-1)
        self.channel.set_volume(0.0,0.0)
        self.volume=[0.0,0.0]
        self.pos=-11
    def set_position(self,pos) :
        volumes={-10:[0.1,0.0],-9:[0.2,0.0],-8:[0.3,0.0],-7:[0.4,0.0],-6:[0.5,0.0],-5:[0.6,0.0],-4:[0.7,0.0],-3:[0.8,0.0],-2:[0.9,0.0],-1:[1,0],0:[1,1],1:[0,1],2:[0,0.9],3:[0,0.8],4:[0,0.7],5:[0,0.6],6:[0,0.5],7:[0,0.4],8:[0,0.3],9:[0,0.2],10:[0,0.1],-11:[0.0,0.0],11:[0.0,0.0]}
        if pos in range(-11,12) :
            self.volume=volumes[pos]
            self.pos=pos
    def get_position(self) :
        return self.pos
    def update(self) :
        self.channel.set_volume(self.volume[0],self.volume[1])