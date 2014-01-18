#!/usr/bin/env python
# encoding: utf-8
"""
graph_objects.py

Created by Sebastian Krüger on 2014-01-18.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

import sys


class window_items(object):

    def __init__(self, posX, posY, type='Unknown'):
        self.posX = posX
        self.posY = posY
        self.type = type
        print 'Item.construct: type: ',type

    def getType(self):
        return self.type

    def move(self,x,y):
        self.posX = x
        self.posY = y
        print 'item.move: move to x=', x, ' y=', y

    def getPos(self):
        return [self.posX, self.posY]

    def __str__(self):
        if self.type == 'Text':
            return "Type: %s, pos: %d:%d" % (self.type, self.posX, self.posY)
        else:
            return "Type: unknown"



class graph_itemTests(unittest.TestCase):
    def setUp(self):
        pass

if __name__ == '__main__':
    unittest.main()