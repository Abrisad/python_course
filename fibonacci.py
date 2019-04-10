def fib(number):
    result = [1, 1]

    if number == 0:
        print("Value should be 1 or higher")
        return 0
    elif number == 1:
        return [1]
    elif number == 2:
        return result
    else:
        for i in range(2, number):
            result.append(result[i - 1] + result[i - 2])
        return result


def main():
    fib(1)
    print(fib(0))
    print(fib(2))
    print(fib(5))
    print(fib(10))


main()



