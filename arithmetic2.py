"""Math functions for calculator."""
import functools

def add(nums):
    """Return the sum of the two inputs."""

    return sum(nums)


def subtract(nums):
    """Return the second number subtracted from the first."""

    return functools.reduce(lambda a, b : a - b, nums)


def multiply(nums):
    """Multiply the two inputs together."""

    return functools.reduce(lambda a, b : a * b, nums)


def divide(nums):
    """Divide the first input by the second, returning a floating point."""

    return functools.reduce(lambda a, b : a / b, nums)


def square(num1):
    """Return the square of the input."""

    # Needs only one argument

    return num1 * num1


def cube(num1):
    """Return the cube of the input."""

    # Needs only one argument

    return num1 * num1 * num1


def power(nums):
    """Raise num1 to the power of num and return the value."""

    return functools.reduce(lambda a, b : a ** b, nums)


def mod(nums):
    """Return the remainder of num / num2."""

    return functools.reduce(lambda a, b : a % b, nums)



li = [1,2,3,4,5,6]


print(functools.reduce(lambda a,b : a+b, li))