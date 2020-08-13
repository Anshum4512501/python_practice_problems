def outer_function(display_argument):
    def inner_function():
        print("I am inner function executed")
        display_argument()

    return inner_function


@outer_function
def display():
    print("I am display function waiting to be executed")


# display = outer_function(display)

display()
#
# display = outer_function(display)
