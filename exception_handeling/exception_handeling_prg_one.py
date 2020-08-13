class Bad(Exception):
    pass


def bad_method():
    raise Bad()


try:
    bad_method()
except Bad:
    print("Caught Bad")
