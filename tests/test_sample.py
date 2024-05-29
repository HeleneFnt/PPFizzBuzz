from fizzbuzz import calculate_fizzbuzz


def test_multiple_of_three():
    actual = calculate_fizzbuzz(3)
    expected = "Fizz"
    assert actual == expected


def test_multiple_of_five():
    actual = calculate_fizzbuzz(5)
    expected = "Buzz"
    assert actual == expected


def test_multiple_of_three_and_five():
    actual = calculate_fizzbuzz(15)
    expected = "FizzBuzz"
    assert actual == expected
