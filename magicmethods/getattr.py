class Count:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        print("get attrb called here")
        return super(Count, self).__setattr__(item, 'orphan')

    def __getattribute__(self, item):
        print("Get attribute has been called here", item)
        return super(Count, self).__getattribute__(item)


c = Count("Me")
print(c.name)
print("Name", c.noname)
print(c.__dict__)

