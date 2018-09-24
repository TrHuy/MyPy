import pygame
from pygame.locals import *
import time

pygame.mixer.music.load('beep1.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.stop()
