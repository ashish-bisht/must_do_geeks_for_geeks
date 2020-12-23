# A function which takes a function as param and add some functionalities and then returns a function


def decorator_function(func):
    def inner():
        print(func.__name__, "Function has been called")
        return func()
    return inner


@decorator_function
def login():
    print("Login")


@decorator_function
def logout():
    print("logout")


login()
logout()
