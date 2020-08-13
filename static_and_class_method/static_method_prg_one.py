def print_number_of_instances():
    print(Static_Test.number_of_instances)


class Static_Test(object):
    number_of_instances = 0

    def __init__(self):
        Static_Test.number_of_instances += 1



