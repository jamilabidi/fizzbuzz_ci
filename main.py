from bottle import route, run, debug, template, request, static_file, default_app, error


@route('/fizzbuzz', method='GET')
# @route('/fizzbuzz', method='POST')
def fb_access():
    print("request : " + request.GET.number)
    if request.GET.num:
        number = request.GET.number

        return template('mysite/display-result', result=main(number))
    else:
        return template('mysite/fb_access.tpl')


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
    for i in range(1, int(value) +1):
        s += str(fizzbuzz(i))
    return s


application = default_app()
