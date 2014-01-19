#!/usr/bin/env python
# encoding: utf-8
"""
window.py

Created by Sebastian Krüger on 2014-01-19.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import unittest

from widget import Widget
import progress_bar

class Window(Widget):

    def __init__(self, posX=0, posY=0, width=0, height=0):
        print "Construct a new Window, %d:%d:%d:%d" % (posX, posY, width, height)
        Widget.__init__(self, posX, posY, 'Window')
        self.width = width
        self.height = height
        self.widgets = []

    def append(self, item):
        self.widgets.append(item)
        print 'Window.append: type=', item.type, ' new len', len(self.objects)
        
    def TextBox(self):
        print 'Window.TextBox, not yet implemented'
        return False
        
    def ProgressBar(self, relX=0, relY=0, width=4, length=0):
        print 'Window.ProgressBar not yet implemented'
        return False
        
    def getDimensions(self):
        print 'Window.getDimension'
        return [self.posX, self.posY, self.width, self.height]

    def __str__(self):
        str = " Window, Size: %3d : %2d" % (self.width, self.height)
        return "Window: %d:%d:%d:%d" % (self.posX, self.posY, self.width, self.height)



class WindowTests(unittest.TestCase):
	def setUp(self):
	    self.w1 = Window(0,0, 128, 20)
		
	def test_initWindow(self):
	    self.assertEqual(self.w1.getDimension(), [0, 0, 128, 20])


if __name__ == '__main__':
	unittest.main()
