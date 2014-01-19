#!/usr/bin/env python
# encoding: utf-8
"""
lcd_stub.py

used as a stub when developing the code on a host machine

Created by Sebastian Krüger on 2014-01-19.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

import sys
import os

class Lcd_Emsystech(object):
    
    def __init__(self):
        print 'LcdEmsystech.init'
        
    def backlight_on(self):
		print('Backlight Enabled')
		return True

	def backlight_off(self):
		print('Backlight Disabled')
		return True

	def contrastSet(self, contrast):
		print('LCD.contrast: old= ', self.contrast, ' new=', contrast)
        return True

	def lcdDrawLine(self, x0, y0, len):
		print('lcd.drawLine: x0=', x0, ' y0=', y0, ' len=', len)
		return True

	def lcdPutPixel(self, x, y, color):
		print('lcd.putPixel: x=', x, ' y=', y, ' color=', color)
		return True

	def lcdPrintTxt(self, x, y, txt):
		print('lcd.print: x=', x, ' y=', y, ' txt=', txt)
		return True

def main():
    pass

