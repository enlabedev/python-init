from src.fizzbuzz import fizzbuzz


def test_multiples_of_3_return_fizz():
    fizzTest = fizzbuzz()
    assert fizzTest.multiple(1, 10, {3: "Fizz"}) == [
        1,
        2,
        "Fizz",
        4,
        5,
        "Fizz",
        7,
        8,
        "Fizz",
        10,
    ]


def test_multiples_of_5_return_buzz():
    fizzTest = fizzbuzz()
    assert fizzTest.multiple(1, 10, {5: "Buzz"}) == [
        1,
        2,
        3,
        4,
        "Buzz",
        6,
        7,
        8,
        9,
        "Buzz",
    ]


def test_multiples_of_3_and_5_return_fizzbuzz():
    fizzTest = fizzbuzz()
    assert fizzTest.multiple(1, 15, {3: "Fizz", 5: "Buzz"}) == [
        1,
        2,
        "Fizz",
        4,
        "Buzz",
        "Fizz",
        7,
        8,
        "Fizz",
        "Buzz",
        11,
        "Fizz",
        13,
        14,
        "FizzBuzz",
    ]
