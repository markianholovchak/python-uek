def f1(a):
    return len(list(filter(lambda x: True if x > 8 and x % 2 == 0 else False, a)))
