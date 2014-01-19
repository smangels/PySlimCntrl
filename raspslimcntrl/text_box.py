#!/usr/bin/env python
# encoding: utf-8
"""
text_box.py

Created by Sebastian Krüger on 2014-01-19.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import unittest

from window_items import window_item

class TextBox(window_item):
    def __init__(self, posX=0, posY=0, font=None):
        window_item.__init__(self, posX, posY, 'TextBox')
        self.font = font
        self.text = ""
        
    def setText(self, text):
        self.text = text
        return True
        
    def getText(self):
        return self.text



class TextBoxTests(unittest.TestCase):
    def setUp(self):
        self.tb = TextBox()
        pass

    def test_InitGetText(self):
        self.assertEqual(self.tb.getText(), "", "Expected: no text at all")
        
    def test_InitGetType(self):
        self.assertEqual(self.tb.getType(), 'TextBox', "Expected: no text at all")
        
    def test_SetText(self):
        self.assertEqual(self.tb.getText(), "", "Expected: no text at all")
        self.assertEqual(self.tb.setText("Freunde sind selten"), True, "Expected: no text at all")
        self.assertEqual(self.tb.getText(), "Freunde sind selten", "Expected: no text at all")

if __name__ == '__main__':
    unittest.main()
