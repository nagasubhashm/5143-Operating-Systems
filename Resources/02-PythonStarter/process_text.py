

def readFile(fname):
    """
    Example read file method. Really here so we can
    import it into another file (as an example)
    """
    f = open(fname,'r')
    data = f.read()
    return data

def __repr__(self):
    """
    A "representation" of a class when printed to the screen
    """
    return "Filename: " + self.filename

def __str__(self):
    """
    Kind of the same as __repr__
    """
    return self.__repr__()

def countWords(data):
    """
    Counts words in chunk of text
    """
    words = data.split()
    return len(words)

class TextProcessing:
    """
    Example class to be imported from some other file.
    """

    def __init__(self,filename=None):
        """
        Default constructor
        """
        self.filename = filename

    def readFile(self,fname=None):
        """
        Simple read file method
        """
        data = []
        if not fname:
            fname = self.filename

        if fname:
            f = open(fname,'r')
            data = f.read()

        return data

    def countWords(self, data=[]):
        """
        Counts words in a list of sentences
        """
        words = data.split()
        return len(words)

"""
The following code block only gets run if this file is called directly.
"""
if __name__=='__main__':

    print("Running Tests...")
    data = readFile("text.txt")
    print(len(data) > 0)

