
def main(n):
    return iteration(n)


def fizzbuzz(value):
    value = int(value)
    if value % 3 == 0 and value % 5 == 0:
        return "Fizz Buzz"
    elif value % 3 == 0:
        return "Fizz"
    elif value % 5 == 0:
        return "Buzz"
    else:
        return value


def fizzbuzzstr(value):
    res = ""
    s = str(value)
    if '3' in s:
        res += "Fizz "
    if '5' in s:
        res += "Buzz"
    return res


def iteration(value):
    s = ""
    for i in range(1, int(value) + 1):
        s += str(fizzbuzz(i))
    return s
