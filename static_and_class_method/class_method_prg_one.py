class A(object):
    def __init__(self):
        print("A has been called here")

    # @classmethod
    def method(obj):
        print("I am class method")
        obj()


A.method = classmethod(A.method)
A.method()
