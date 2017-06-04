
def handle_numbers(num1, num2, num3):
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
