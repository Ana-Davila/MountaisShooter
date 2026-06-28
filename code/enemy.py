#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Entity import Entity
from code.Const import ENTITY_SPEED, WIN_WIDTH


class Enemy(Entity):
    def __init__(self, name, positon):
        super().__init__(name, positon)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

