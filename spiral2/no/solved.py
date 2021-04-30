import random


def spiralize(size, n=1):
    x = n  # 1
    counter = 0
    incrt = 2
    total = 0

    while x <= size ** 2 + n:
        total += x
        x += incrt
        counter += 1
        if counter == 4:
            incrt += 2
            counter = 0

    return total


if __name__ == "__main__":
    templ = """
def test_{0}():
    \"\"\"  Test the {0} from the assignments. \"\"\"
    assert homework.spiralize({0}, {1}) == {2}
"""

    # print("Starting at 1: ")
    # print(spiralize(5))
    # print("Starting at 3: ")
    # print(spiralize(5, n=3))
    # print("Starting at 10: ")
    # print(spiralize(5, n=10))
    # x = 10011
    x = 1

    while x <= 501:
        y = random.randint(1, 50)
        answer = spiralize(x, y)
        print(templ.format(x, y, answer))
        x += 10
