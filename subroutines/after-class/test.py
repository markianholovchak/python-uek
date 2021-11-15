def test(tests, func):
    for index, test in enumerate(tests):
        if func(**test["input"]) == test["output"]:
            print(f"Test {index +1} - passed")
        else:
            print(f"Test {index + 1} - failed")