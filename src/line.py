class Line:
    def __init__(self, line):
        self.line = line

    def valid(self):
        if self.line != "" and self.line.startswith('Lclicksquid-'):
            self.line = self.line.replace('Lclicksquid-', '')
            return True
        else:
            return False
            