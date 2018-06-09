import pygame.mixer
import io

class GameSound:

    def __init__(self):

        pygame.mixer.init(frequency=44100, buffer=1024, channels=1)
        
        self.channel = pygame.mixer.Channel(0)
        
        io_start = io.BytesIO(open('start.wav', 'rb').read())
        io_game_over = io.BytesIO(open('game_over.wav', 'rb').read())
        io_eat = io.BytesIO(open('eat.wav', 'rb').read())
        io_walk3 = io.BytesIO(open('walk.wav', 'rb').read())
        
        self.snd_start = pygame.mixer.Sound(io_start)
        self.snd_game_over = pygame.mixer.Sound(io_game_over)
        self.snd_eat = pygame.mixer.Sound(io_eat)
        self.snd_walk = pygame.mixer.Sound(io_walk3)
        
        self.snd_start.set_volume(0.5)
        self.snd_game_over.set_volume(0.25)
        self.snd_eat.set_volume(0.5)
        self.snd_walk.set_volume(0.25)
        
        self.snd_walk_switch = True

    def play_start(self):

        self.snd_start.play()

    def play_game_over(self):

        self.snd_game_over.play()

    def play_walk(self):

        self.channel.play(self.snd_walk)
        self.snd_walk_switch = not self.snd_walk_switch

    def play_eat(self):

        self.snd_eat.play()
