class Test(object):
    static_counter = 0

    def __init__(self):
        Test.static_counter += 1

    @staticmethod
    def print_static_counter():
        print(Test.static_counter)

    # print_static_counter = staticmethod(print_static_counter)


test = Test()
test.print_static_counter()
test_one = Test()
test_one.print_static_counter()