# Hints: https://github.com/SoliGabiAnn/Functional-programming-course/wiki/08.-Currying
# https://github.com/SoliGabiAnn/Functional-programming-course/wiki/09.-Decorators

def curry(func):
    def curried(*args):
        if len(args) >= func.__code__.co_argcount:
            return func(*args)
        return lambda *more_args: curried(*(args + more_args))
    return curried


def validate_coin(func):
    def wrapper(coin):
        ... # Fill here
        return func(coin)
    return wrapper


... # Fill here
def coffee_machine(coin, drink):
    return f"Here's your {drink}"


try:
    order = coffee_machine(0)("espresso")  # Throws ValueError
except ValueError as e:
    print(e) 

success = coffee_machine(2)("espresso")
print(success) 

'''
Expected Output:

"Insert at least 1 coin"
"Here's your espresso"
'''
