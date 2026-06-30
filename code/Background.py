#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Entity import Entity
from code.Const import WIN_WIDTH, ENTITY_SPEED


class Background(Entity):
    def __init__(self, name: str, positon: tuple):
        super().__init__(name, positon)
        pass

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <=0:
            self.rect.left = WIN_WIDTH
