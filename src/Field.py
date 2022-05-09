class Field:
    """
        Class for the Field datas, as length, height, background.
    """
    def __init__(self, lengthX=720,
                 heightY=480,
                 background=None):  # default field size is 720x480
        if background is None:
            background = [0, 0, 0]
        self.lengthX = lengthX
        self.heightY = heightY
        self.background = background

    def get_length(self):
        """
            Returns length of the Field
        """
        return self.lengthX

    def get_height(self):
        """
            Returns height of the Field
        """
        return self.heightY

    def get_background(self):
        """
            Returns background of the Field
        """
        return self.background
