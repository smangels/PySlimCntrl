#!/usr/bin/env python
# encoding: utf-8
"""
graph_objects.py

Created by Sebastian Krüger on 2014-01-18.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import unittest

class window_item(object):

    def __init__(self, posX=0, posY=0, type='Unknown'):
        self.posX = posX
        self.posY = posY
        self.type = type
        print 'Item.construct: type: ',type

    def getType(self):
        return self.type

    def move(self,x,y):
        if x < 0 or y < 0:
            return False
        self.posX = x
        self.posY = y
        print 'item.move: move to x=', x, ' y=', y
        return True

    def getPos(self):
        return [self.posX, self.posY]

    def __str__(self):
        if self.type == 'Text':
            return "Type: %s, pos: %d:%d" % (self.type, self.posX, self.posY)
        else:
            return "Type: unknown"



class graph_itemTests(unittest.TestCase):
    def setUp(self):
        self.item = window_item()
        
    def test_initGraphItem(self):
        self.assertEqual(self.item.getType(), 'Unknown', "Invalid type")
        
    def test_initGetPos(self):
        self.assertEqual(self.item.getPos(), [0, 0], "invalid position after INIT")
        
    def test_moveItemInvalidX(self):
        self.assertEqual(self.item.move(-2, 0), False, "Invalid type")
        
    def test_moveItemInvalidY(self):
        self.assertEqual(self.item.move(-2, -2), False, "Invalid type")
        
    def test_moveItemValid(self):
        self.assertEqual(self.item.move(10, 20), True, "Invalid type")
        self.assertEqual(self.item.getPos(), [10, 20], "Invalid new position after move")

if __name__ == '__main__':
    unittest.main()
