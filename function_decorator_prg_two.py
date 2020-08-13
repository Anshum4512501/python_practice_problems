def test_conditions(original_function):
    def conditions(**kwargs):
        if kwargs.get('name') == "Anshoo":
            print("Valid")
            original_function(**kwargs)
            return conditions
        else:
            print("Invalid")
            return False

    return conditions


@test_conditions
def test_me(**kwargs):
    print("I have been tested")


test_me(name="Ansho00", education="Btech")
