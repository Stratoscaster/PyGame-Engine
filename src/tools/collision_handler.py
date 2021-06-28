import pymunk
import pygame

class CollisionHandler():

    def __init__(self):
        self.pymunk_handlers = []

# TODO add collision handler callbacks from pymunk