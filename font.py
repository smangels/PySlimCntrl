
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