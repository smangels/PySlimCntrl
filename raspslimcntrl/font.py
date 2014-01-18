import os
import sys
import unittest

class font(object):
    
    def __init__(self):
        print 'font.init'
        self.charBytes = 0
        self.charHeight = 0
        self.charWidth = 0
        self.name = "Empty"
        self.lines = None
        self.byteArray = None
        
    def loadCHeader(self, hFile):
        '''
        TODO : implement a load function that parses a standard C header file
        containing the image
        '''
        print 'font.loadCHeader, file=', hFile
        with open(hFile) as f:
            self.lines = f.read().splitlines()
            f.close()
        
    def getByteArray(self):
        print 'font.getByteArray'
        return self.byteArray
        
    def getFontStructure(self):
        print 'font.getFontStructure'
        return [self.charBytes, self.charHeight, self.charWidth]
        
    def __str__(self):
        str = ""
        str = str + "Font: %s, %d bytes/char, width=%dpx, height=%dpx" % (self.name, self.charBytes, self.charWidth, self.charHeight)
        if self.lines != None:
            str = str + " lines=%d" % (len(self.lines))
            
        return str


'''
    UNIT TESTS for "font" class
'''        
        
class fontTests(unittest.TestCase):
    def setUp(self):
        self.font = font()
        pass
        
    def tearDown(self):
        del self.font
        pass
        
    def test_init(self):
        self.assertEqual(self.font.getByteArray(), None, "Message")
        
    def test_init2(self):
        self.assertEqual(self.font.getFontStructure(), [0, 0, 0], "Invalid Font Structure in init")

if __name__ == '__main__':
    unittest.main()
