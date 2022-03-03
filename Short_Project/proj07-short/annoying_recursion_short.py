def annoying_factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    elif n == 4:
        return 4 * annoying_factorial(n-1)
    elif n == 5:
        return 5 * annoying_factorial(n - 1)
    elif n == 6:
        return 6 * annoying_factorial(n - 1)
    else:
        return n * annoying_factorial(n-1)


def annoying_countdown(n):
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
        print(0)
    elif n == 2:
        print(2)
        print(1)
        print(0)
    elif n == 3:
        print(3)
        print(2)
        print(1)
        print(0)
    elif n == 4:
        print(4)
        annoying_countdown(n - 1)
    elif n == 5:
        print(5)
        annoying_countdown(n - 1)
    elif n == 6:
        print(6)
        annoying_countdown(n - 1)
    else:
        print(n)
        annoying_countdown(n - 1)


def annoying_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    elif n == 4:
        return annoying_fibonacci(n-1)+annoying_fibonacci(n-2)
    elif n == 5:
        return annoying_fibonacci(n-1)+annoying_fibonacci(n-2)
    elif n == 6:
        return annoying_fibonacci(n-1)+annoying_fibonacci(n-2)
    else:
        return annoying_fibonacci(n-1)+annoying_fibonacci(n-2)


def annoying_very_quizzical(n):
    if n == 0:
        return "what"
    elif n == 1:
        return "what?"
    elif n == 2:
        return "what?!"
    elif n == 3:
        return "what?!?"
    elif n == 4:
        return annoying_very_quizzical(n - 1) + "!"
    elif n == 5:
        return annoying_very_quizzical(n - 1) + "?"
    elif n == 6:
        return annoying_very_quizzical(n - 1) + "!"
    else:
        if n % 2 == 0:
            return annoying_very_quizzical(n - 1) + "!"
        else:
            return annoying_very_quizzical(n - 1) + "?"


def annoying_parens(n):
    if n == 0:
        return "x"
    elif n == 1:
        return "(x)"
    elif n == 2:
        return "((x))"
    elif n == 3:
        return "( ((x)) )"
    elif n == 4:
        return "("+ annoying_parens(n-1)+")"
    elif n == 5:
        return "( " + annoying_parens(n-1) + " )"
    elif n == 6:
        return "(" + annoying_parens(n-1) + ")"
    else:
        if n % 2 == 0:
            return "(" + annoying_parens(n-1) + ")"
        else:
            return "( " + annoying_parens(n-1) + " )"



