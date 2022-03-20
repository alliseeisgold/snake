class Field:
    def __init__(self, lengthX = 720,
                 heightY = 480, 
                 background = [0, 0, 0]): #default field size is 720x480
        self.lengthX = lengthX
        self.heightY = heightY
        self.background = background

    def getWindowLength(self):
        return self.lengthX

    def getWindowHeight(self):
        return self.heightY

    def getBackgroundColor(self):
        return self.background

    
