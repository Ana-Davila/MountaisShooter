#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC,abstractmethod
import pygame

class Entity(ABC):
    def __init__(self, name: str, positon: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png')
        self.rect = self.surf.get_rect(left=positon[0], top=positon[1])
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass
