def extra(self,arg):
    print(arg)
    print(self)
def required(x):
    if x is True:
        return True
    else:
        return False
class Client(object):
    def __init__(self, x):
        self.x =x
    if required(self.x):
        Client.extra = extra

