
import os
import sys
import unittest
import font

from time import sleep

'''
    Display class that handles a singleton of a display object
    It is meant to hold a number of windows
    Provides factory function for new windows
'''

class display(object):
    
    _instance = None
    def __new__(cls, *args, **kwargs):
        print 'Run new.Display'
        if not cls._instance:
            cls._instance = super(Display, cls).__new__(cls, *args, **kwargs)
            return cls._instance
            
    def __init__(self, width=0, height=0):
        print 'Run init.Display'
        self.width = width
        self.height = height
        self.windows = []
    
    def append(self, item):
        
        if not item.type == 'Window':
            print 'display.append: Invalid type', item.type
            return False
        self.windows.append(item)
        print 'display.append: window added'
        
        
    def getNrItems(self):
        return self.windows.len()
        
    def update(self):
        '''
        updates the framebuffer content
        '''
        print 'Display.update'
        
    def window(self):
        '''
        Factory for a new Window
        '''
        self.windows.append()
        
    def __str__(self):
        str = "Display %dpx x %dpx\n" % (self.width, self.height)
        for i in range(len(self.windows)):
            str = str + "  Window %2d " % (i+1) + "Size: %3dpx x %2dpx" % (self.windows[i].width, self.windows[i].height) + "\n"    
        return str
        

class displayTests(unittest.TestCase):
    def setUp(self):
        pass

if __name__ == '__main__':
    unittest.main()