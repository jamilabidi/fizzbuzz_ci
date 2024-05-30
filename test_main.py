import pytest

from fizzbuzz import fizzbuzz, fizzbuzzstr


@pytest.mark.parametrize("value", [3, 6, 9, 12, 18, 21])
def test_should_fizzbuzz_return_fizz_when_value_is_multiple_of_3(value):
    actual = fizzbuzz(value)
    expected = "Fizz"
    assert actual == expected


@pytest.mark.parametrize("value", [5, 10, 20, 25, 35])
def test_should_fizzbuzz_return_buzz_when_value_is_multiple_of_5(value):
    actual = fizzbuzz(value)
    expected = "Buzz"
    assert actual == expected


@pytest.mark.parametrize("value", [15, 30, 45, 60, 75])
def test_should_fizzbuzz_return_fizzbuzz_when_value_is_multiple_of_3_and_5(value):
    actual = fizzbuzz(value)
    expected = "Fizz Buzz"
    assert actual == expected


@pytest.mark.parametrize("value", [3, 13, 23, 30, 33])
def test_should_fizzbuzz_return_fizz_when_value_contain_3(value):
    actual = fizzbuzzstr(value)
    expected = "Fizz "
    assert actual == expected


@pytest.mark.parametrize("value", [5, 15, 25, 45, 55])
def test_should_fizzbuzz_return_buzz_when_value_contain_5(value):
    actual = fizzbuzzstr(value)
    expected = "Buzz"
    assert actual == expected


@pytest.mark.parametrize("value", [35, 53])
def test_should_fizzbuzz_return_fizzbuzz_when_value_contain_3_and_5(value):
    actual = fizzbuzzstr(value)
    expected = "Fizz Buzz"
    assert actual == expected
