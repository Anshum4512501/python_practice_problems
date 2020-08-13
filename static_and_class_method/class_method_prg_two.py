class Test(object):
    def __init__(self, name, **kwargs):
        self.name = name
        self.kwargs = kwargs

    def show_attributes(self):
        print(self.name)
        print(self.kwargs)

    @classmethod
    def method(cls, name, **kwargs):
        cls(name, **kwargs)


print(Test.method("Anshu", qualificaation="btech"))



