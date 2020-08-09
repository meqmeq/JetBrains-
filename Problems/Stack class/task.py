class Stack():

    def __init__(self):
        self.a = []


    def push(self, el):
        self.a.append(el)

    def pop(self):
        lastel = self.a[-1]
        del self.a[-1]
        return lastel

    def peek(self):
        return self.a[-1]

    def is_empty(self):
        if not self.a:
            return True
        else:
            return False


