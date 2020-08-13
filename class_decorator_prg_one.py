class Decorator(object):
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        return self.function(*args, **kwargs)


@Decorator
def fun(*args, **kwargs):
    print("I have been called")


fun(4, 5, name="function")
