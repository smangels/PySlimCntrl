#!/usr/bin/env python
# encoding: utf-8
"""
timeBox.py

Created by Sebastian Krüger on 2014-01-19.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import unittest
import math

from text_box import TextBox


class TimeStamp(TextBox):
    
    def __init__(self, posx=0, posy=0):
        print 'TimeBox.init'
        self.min = 0
        self.sec = 0
        TextBox.__init__(self, posx, posy, "%3d:%2d" % (self.min, self.sec))
        
    def __str__(self):
        return "TimeBox.print %3d:%02d" % (self.min, self.sec)
        
    def setTimeSec(self, time):
        self.min = math.floor(time / 60)
        self.sec = math.floor(time - (self.min * 60))
        print 'TimeBox.set %3d:%02d' % (self.min, self.sec)
        return True
        
    def hasElapsed(self):
        if self.min == 0 and self.sec == 0:
            return True
        return False
        
    def getTime(self):
        return [self.min, self.sec]
        
    def timeElapsed(self, seconds):
        if seconds > 0:
            res = self.sec - seconds
            print 'Result: %d' % (res)
            if res < 0:
                if self.min > 0:
                    self.min -= 1;
                self.sec = 60 + (res)
            elif res == 0:
                self.sec = 0
            else:
                self.sec = res;
        return True
                


class timeBoxTests(unittest.TestCase):
    def setUp(self):
        self.tb = TimeStamp(0, 0)
        
    def test_initTime(self):
        self.assertEqual(self.tb.getTime(), [0, 0], "Unexpected initial time")
        
    def test_setTime(self):
        self.assertEqual(self.tb.setTimeSec(101.21), True, "Unexpected initial time")
        self.assertEqual(self.tb.getTime(), [1, 41], "Invalid time, expected 1:41")
        
    def test_hasElapsedNot(self):
        self.assertEqual(self.tb.setTimeSec(1.334), True, "Unexpected initial time")
        self.assertEqual(self.tb.hasElapsed(), False, "Unexpected initial time")

    def test_hasElapsed(self):
        self.assertEqual(self.tb.setTimeSec(2.33), True, "Unexpected initial time")
        self.assertEqual(self.tb.timeElapsed(1), True, "Invalid return value for timeElapsed")
        self.assertEqual(self.tb.hasElapsed(), False, "Unexpected initial time")
        self.assertEqual(self.tb.timeElapsed(1), True, "Invalid return value for timeElapsed")
        self.assertEqual(self.tb.hasElapsed(), True, "Unexpected initial time")
        
if __name__ == '__main__':
    unittest.main()