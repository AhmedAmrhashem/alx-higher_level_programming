#!/usr/bin/python3
if _name_ == "_main_":
    """Prints some mathmatical opperations"""
    from caclulator_1 import add,sub,mul,div
    a = 10
    b = 5
    print("{} + {} = {}" .format(a, b, add(a,b)))
    print("{} - {} = {}" .fomrat(a, b, sub(a,b)))
    print("{} * {} = {}" .fomrat(a, b, mul(a,b)))
    print("{} / {} = {}" .fomrat(a, b, div(a,b)))
