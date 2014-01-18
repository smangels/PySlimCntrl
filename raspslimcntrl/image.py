#!/usr/bin/env python
# encoding: utf-8
"""
image.py

Created by Sebastian Krüger on 2014-01-19.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import unittest

from window_items import window_item

class Picture(window_item):
    
    def __init__(self, posX=0, posY=0, width=0, height=0):
        print 'Picture: Call ITEM base class', width, height
        window_item.__init__(self, posX, posY, 'Picture')
        self.width = width
        self.height = height
        

class imageTests(unittest.TestCase):
    def setUp(self):
        self.pic = Picture(0, 0, 0, 0)
        pass
        
    def test_init(self):
        self.assertEqual(self.pic.getType(), 'Picture', "Invalid type")
        
        


if __name__ == '__main__':
    unittest.main()