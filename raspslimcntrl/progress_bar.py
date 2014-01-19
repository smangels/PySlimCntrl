#!/usr/bin/env python
# encoding: utf-8
"""
graph_textbox.py

Created by Sebastian Krüger on 2014-01-18.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import unittest

from widget import Widget


class progress_bar(Widget):
	def __init__(self, posx=0, posy=0, height=0, len=0):
	    Widget.__init__(self, posx, posy, 'ProgressBar')
	    self.elapsed = 0
	    self.height = 0
	    self.len = 0
	    self.max = 0
		
		
	def setMax(self, max):
	    self.max = max
	    return True
		
	def update(self, percent):
	    if percent < 0 or percent > 100:
	        return False
	    self.elapsed = percent
	    return True
	    
	def setElapsed(self, percent):
	    return False
	    
	def getElapsed(self):
	    '''
	        return the present positon in percent of the
	        total length
	    '''
	    return self.elapsed
	    
	def getMax(self):
	    return self.max
	    
	def reset(self):
	    '''
	        reset the progress bar to ZERO
	    '''
	    self.elapsed = 0
	    return False


class progress_barTests(unittest.TestCase):
	def setUp(self):
		self.pb = progress_bar(0,64, 3, 80)
		
	def test_initPb(self):
	    self.assertEqual(self.pb.update(10), True, "Invalid return values")
	    self.assertEqual(self.pb.getElapsed(), 10, "Invalid return values")
	    
	def test_setMax(self):
	    self.assertEqual(self.pb.setMax(310.225), True, "Invalid return values")
	    self.assertEqual(self.pb.getMax(), 310.225, "Invalid return values")

if __name__ == '__main__':
	unittest.main()
