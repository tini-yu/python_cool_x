def test_positive():
    assert nod(10, 5) == 5, "nod(10, 5) should be 5"
    assert nod(10, 50) == 10, "nod(10, 50) should be 10"
    assert nod(15, 27) == 3, "nod(15, 27) should be 3"
    assert nod(6, 14) == 2, "nod(6, 14) should be 2"
    assert nod(150, 120) == 30, "nod(150, 120) should be 30"
    assert nod(17, 120) == 1, "nod(17, 120) should be 1"


def test_negative():
    assert nod(0, 5) == 0, "Testing 0 failed..."
    assert nod(3, 0) == 0, "Testing 0 failed..."
    assert nod(0, 0) == 0, "Testing 0 failed..."
    assert nod(1, 0) == 0, "Testing 0 failed..."
    assert nod(0, 1) == 0, "Testing 0 failed..."
    assert nod(-1, 1) == 0, "Testing negative failed..."
    assert nod(-17, 17) == 0, "Testing negative failed..."
    assert nod(-22, -25) == 0, "Testing negative failed..."
    assert nod(0.5, 0.5) == 0, "Testing not natural failed..."
    assert nod(1, 0.5) == 0, "Testing not natural failed..."
    assert nod(10, 0.5) == 0, "Testing not natural failed..."
    assert nod(10.7, 355) == 0, "Testing not natural failed..."


def nod(num_1: int, num_2: int) -> int:
    while num_1 > 0 and num_2 > 0 and num_2 == int(num_2) and num_1 == int(num_1):
        while num_1-num_2 > 0:
            num_1 -= num_2
        while num_2-num_1 > 0:
            num_2 -= num_1
        if num_2 == num_1:
            return num_1
    return 0


if __name__ == "__main__":
    test_positive()
    test_negative()
    print("Everything passed")
    n1, n2 = map(int, input("Two natural numbers: ").split())
    print(f'nod = {nod(n1, n2)}')
