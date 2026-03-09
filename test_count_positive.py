from module import count_positive
import sys


def run_all_tests():
    tests = [
        (([3,-1,2,-5],), 2),
        (([1,2,3],), 3),
        (([-1,-2,-3],), 0),
        (([0,1,-1],), 1),
    ]

    run_tests(tests, count_positive)


def run_tests(tests, function):
    failure = False

    for i, (inputs, expected) in enumerate(tests):
        try:
            actual = function(*inputs)

            print(f"Inputs: {inputs}")
            print(f"Expected: {expected}, Got: {actual}")

            assert actual == expected
            print(f"Test {i}: Pass!\n")

        except AssertionError:
            print(f"Test {i}: Fail\n")
            failure = True

        except Exception as e:
            print(f"Test {i}: Error → {type(e).__name__}: {e}\n")
            failure = True

    print("❌ Some tests failed." if failure else "✅ All tests passed!")


if __name__ == "__main__":
    run_all_tests()
    sys.exit(0)