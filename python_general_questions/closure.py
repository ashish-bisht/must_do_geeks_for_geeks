
# closure

# We can see func() still have message even after our outer function is over
def outer_function():
    message = "hi"

    def inner_function():
        print(message)
    return inner_function


func = outer_function()
func()
func()
func()


def outer(msg):
    def inner():
        print(msg)
    return inner


hey = outer("Hey")
bye = outer("Bye")

hey()
bye()
