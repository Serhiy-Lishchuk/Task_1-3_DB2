
def handle_numbers(num1, num2, num3):
    """
    Function that takes as
    :param num1: any integer numbers
    :param num2: any integer numbers
    :param num3: any integer numbers
    :return: count of integers that are divisible by num3.
    """
    result = []
    for n in range(num1, num2 + 1):
        if n % num3 == 0:
            result.append(n)
        else:
            pass
    count = len(result)
    return count, result

print(handle_numbers(1, 10, 2))


def handle_string(value):
    """
    Function that takes as
    :param value: any string
    :return: count number of letters and digits.
    """
    result = {
        "Letters": 0,
        "Digits": 0
    }
    for v in value:
        if v.isalpha():
            result["Letters"] += 1
        elif v.isdigit():
            result["Digits"] += 1
        else:
            pass
    return result

print(handle_string("Hello world! 123!"))


def handle_list_of_tuples(list_humans):
    """
    Function that takes as
    :param list_humans: list of tuples data about the person
    :return: a sorted list of tuples.
    """
    result = sorted(list_humans, key=lambda tup: (tup[1], tup[2], tup[3], tup[0]), reverse=True)
    return result

humans = [
    ("Tom", "19", "167", "54"),
    ("Jony", "24", "180", "69"),
    ("Json", "21", "185", "75"),
    ("John", "27", "190", "87"),
    ("Jony", "24", "191", "98"),
    ]

print(handle_list_of_tuples(humans))
