from test import test


def power(x, n):
    """
    Function takes number x that is raised to the power of n using recursion
    If x == 0 and n == 0 function returns -1 (0^0 - indeterminate form)
    """
    if(x == 0 and n == 0):
        return -1
    if(n == 1):
        return x
    if(n == 0):
        return 1
    return x * power(x, n-1)


print(power(5, 3))

tests = [
    {
        "input": {"x": 3,
                  "n": 2,
                  },
        "output": 9
    },
    {
        "input": {"x": 5,
                  "n": 3,
                  },
        "output": 125
    },
    {
        "input": {"x": 2,
                  "n": 16,
                  },
        "output": 65536
    },
    {
        "input": {"x": 9,
                  "n": 4,
                  },
        "output": 6561
    },
    {
        "input": {"x": 16,
                  "n": 4,
                  },
        "output": 65536
    },
    {
        "input": {"x": -4,
                  "n": 3,
                  },
        "output": -64
    },
    {
        "input": {"x": 0,
                  "n": 0,
                  },
        "output": -1
    },
    {
        "input": {"x": 861,
                  "n": 0,
                  },
        "output": 1
    },

]

test(tests, power)
