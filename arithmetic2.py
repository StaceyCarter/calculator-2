"""Math functions for calculator."""
import functools

def add(nums):
    """Return the sum of the two inputs."""

    return round(sum(nums), 2)


def subtract(nums):
    """Return the second number subtracted from the first."""

    return round(functools.reduce(lambda a, b : a - b, nums), 2)


def multiply(nums):
    """Multiply the two inputs together."""

    return round(functools.reduce(lambda a, b : a * b, nums), 2)


def divide(nums):
    """Divide the first input by the second, returning a floating point."""

    return round(functools.reduce(lambda a, b : a / b, nums), 2)


def square(num1):
    """Return the square of the input."""

    # Needs only one argument

    return round(num1 * num1, 2)


def cube(num1):
    """Return the cube of the input."""

    # Needs only one argument

    return round(num1 * num1 * num1, 2)


def power(nums):
    """Raise num1 to the power of num and return the value."""

    return round(functools.reduce(lambda a, b : a ** b, nums), 2)


def mod(nums):
    """Return the remainder of num / num2."""

    return round(functools.reduce(lambda a, b : a % b, nums), 2)
