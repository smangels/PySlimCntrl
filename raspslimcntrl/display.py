
import os
import sys
import unittest
import font
import math

from time import sleep
from widget import Widget


'''
    Display class that handles a singleton of a display object
    It is meant to hold a number of windows
    Provides factory function for new windows
'''

class Display(object):
    
    _instance = None
    def __new__(cls, *args, **kwargs):
        print 'Display.new'
        if not cls._instance:
            cls._instance = super(Display, cls).__new__(cls, *args, **kwargs)
            return cls._instance
            
    def __init__(self, width=0, height=0):
        print 'Display.init'
        self.width = width
        self.height = height
        self.widgets = []
        self.framebuffer = None
    
    def append(self, item):
        if not item.type == 'Window':
            print 'display.append: Invalid type', item.type
            return False
        self.widgets.append(item)
        print 'display.append: window added'
    
    def getDimensions(self):
        return [self.width, self.height]
        
    def getNrItems(self):
        return self.widgets.len()
        
    def update(self):
        '''
        updates the framebuffer content
        '''
        print 'Display.update'
        
    def CreateWindow(self):
        '''
        Factory for a new Window
        '''
        self.windows.append(0)
        return True
        
    def posToIndex(self, x, y):
        if x < 0 or y < 0 or x > (self.width - 1) or y > (self.height - 1):
            return [0, 0]
        else:
            return [ math.floor(x/8), y]
        
    def __str__(self):
        str = "Display %dpx x %dpx\n" % (self.width, self.height)
        for i in range(len(self.windows)):
            str = str + "  Window %2d " % (i+1) + "Size: %3dpx x %2dpx" % (self.windows[i].width, self.windows[i].height) + "\n"    
        return str
        

class displayTests(unittest.TestCase):
    def setUp(self):
        self.disp = Display(128, 64)
    
    def tearDown(self):
        self.disp = None

class GetDimensionTestCase(displayTests):
    def runTest(self):
        self.assertEqual(self.disp.getDimensions(), [128, 64], "Invalid Display Size")
        self.assertEqual(self.disp.posToIndex(-1, 2), [0, 0], "Expected 0,0")
        self.assertEqual(self.disp.posToIndex(7, 2), [0, 2], "Expected 0,0")

if __name__ == '__main__':
    unittest.main()
