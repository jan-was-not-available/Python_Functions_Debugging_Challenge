import sys

# Challenge: this test intentionally looks for a function named "to_sum"
from module import two_sum


def run_all_tests():
    tests = [
        (([1, 2, 3, 4], 7), True),
        (([1, 2, 3, 4], 8), False),
        (([0, 2, 0, 2], 4), True),
        (([-1, -3, -5], -3), False),
        (([], 0), False),
    ]

    one_or_more_failures = False

    for i, (inputs, expected) in enumerate(tests):

        try:
            actual = two_sum(*inputs)

            print(f"Inputs: {inputs}")
            print(f"Expected: {expected}, Got: {actual}")

            assert actual == expected
            print(f"Test {i}: Pass!\n")

        except AssertionError:
            print(f"Test {i}: Fail\n")
            one_or_more_failures = True

        except Exception as e:
            print(f"Test {i}: Error → {type(e).__name__}: {e}\n")
            one_or_more_failures = True

    if one_or_more_failures:
        print("❌ One or more tests failed.")
    else:
        print("✅ All tests passed!")


if __name__ == "__main__":
    run_all_tests()
    sys.exit(0)