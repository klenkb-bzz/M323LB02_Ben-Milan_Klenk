from flask import Flask, request
from functools import reduce

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "<h2>Portfolio-Flask-App für die LB02 im Modul 323 von Ben-Milan Klenk</h2>"


@app.route("/A1G", methods=["GET"])
def A1G():
    def pure(x, y, z):
        return str(x + y + z)

    return f"Sum of x, y and z: {pure(5, 6, 7)}"


@app.route("/A1F", methods=["GET"])
def A1F():
    the_tupel = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    def adding_items(tupel, num):
        try:
            tupel += num
        except Exception as error:
            return error

    return f"Output: {adding_items(the_tupel, 22)}"


@app.route("/A1E", methods=["GET"])
def A1E():
    numbers = [1, 2, 3, 4]

    """Prozedural"""

    def double_numbers(nums):
        doubled = []
        for num in nums:
            doubled.append(num * 2)
        return doubled

    """Funktional"""

    def functional(nums):
        doubled = list(map(lambda x: x * 2, nums))
        return doubled

    return f"{double_numbers(numbers)}{functional(numbers)}"


@app.route("/B1G", methods=["GET"])
def B1G():
    def bubblesort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    nums_bef = [2, 5, 1, 5, 3, 21, 222]
    nums = [2, 5, 1, 5, 3, 21, 222]
    bubblesort(nums)
    return f"Before sort: {nums_bef} <br>After sort: {nums}"


@app.route("/B1F", methods=["GET"])
def B1F():
    def bubble_pass(lst):
        if len(lst) <= 1:
            return lst
        if lst[0] > lst[1]:
            return [lst[1]] + bubble_pass([lst[0]] + lst[2:])
        return [lst[0]] + bubble_pass(lst[1:])

    def sorting(lst, n=None):
        if n is None:
            n = len(lst)
        if n == 1:
            return lst
        lst = bubble_pass(lst)
        return sorting(lst, n - 1)

    nums = [2, 5, 1, 5, 3, 21, 333]

    sorted_list = sorting(nums)

    return f"Before sort: {nums} <br>After sort: {sorted_list}"


@app.route("/B1E", methods=["GET"])
def B1E():
    def new_squares(lst):
        new_nums = list(filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, lst)))
        return new_nums

    nums = [0, 3, 5, 6, 7]
    new_nums = new_squares(nums)

    return f"Alle geraden Hochzahlen sind: {new_nums}"


@app.route("/B2G", methods=["GET"])
def B2G():
    def square(x):
        return x ** 2

    square_of_number = square

    result = square_of_number(10)
    return f"Das Quadrat von 10 ist: {result}"


@app.route("/B2F", methods=["GET"])
def B2F():
    def doubler(x):
        return x * 2

    def minus_double(num, func):
        return num - func(num)

    return f"Wenn man von der Zahl 5 das Doppelte abzieht erhält man: {minus_double(5, doubler)}"


@app.route("/B2E", methods=["GET"])
def B2E():
    def power(exp):
        def number_by_power(num):
            return num ** exp

        return number_by_power

    power_of_5 = power(5)

    return f"10 hoch 5 ergibt: {power_of_5(10)}"


@app.route("/B3G", methods=["GET"])
def B3G():
    string = "Das Wetter ist echt schön!"

    def uppercase(text):
        to_upper = lambda x: x.upper()
        return to_upper(text)

    return f"Der Satz: {string} sieht mit Grossbuchstaben so aus: {uppercase(string)}"


@app.route("/B3F", methods=["GET"])
def B3F():
    def multiply_pairs(num1, num2):
        new_nums = lambda x, y: x*y
        return new_nums(num1, num2)

    return f"Das multiplizierte Paar ist: {multiply_pairs(5, 255)}"


@app.route("/B3E", methods=['GET'])
def B3E():
    numbers = [5, 12, 33, 44]

    def showcase(numbers_list):
        if sum(map(lambda x: x ** 2, numbers_list)) > sum(numbers_list):
            return 'Greater'
        else:
            return 'Smaller'

    return showcase(numbers)


@app.route("/B4G", methods=['GET'])
def B4G():
    numbers = [786, 2234, 233, 4]

    def map_func(numbers_list):
        square = map(lambda x: x ** 2, numbers_list)
        return square

    def filter_func(numbers_list):
        even = filter(lambda x: x % 4 == 0, numbers_list)
        return even

    def reduce_func(numbers_list):
        number_sum = reduce(lambda x, y: x + y, numbers_list)
        return number_sum

    return f'Mapped List: {list(map_func(numbers))}</br>Filtered List: {list(filter_func(numbers))}' \
           f'<br>Reduced List: {reduce_func(numbers)} '


@app.route("/B4F", methods=['GET'])
def B4F():
    numbers = [654, 874, 100, 445, 555]

    def combined_func(numbers_list):
        square_div_five_sum = reduce(lambda x, y: x + y, filter(lambda x: x % 5 == 0, map(lambda x: x ** 2, numbers_list)))
        return square_div_five_sum

    return f'The Square of all sums that are dividable by 5: {combined_func(numbers)}'


@app.route("/B4E", methods=['GET'])
def B4E():
    json = [
        {
            "name": "Ben",
            "grade": 4.0
        },
        {
            "name": "Elias",
            "grade": 3.5
        },
        {
            "name": "Timo",
            "grade": 4.25
        },
        {
            "name": "Josiah",
            "grade": 3.25
        }
    ]

    def complex_function(json):
        updated_students = list(filter(lambda student: student["grade"] > 3.25,
                                       map(lambda student: {**student, "grade": student["grade"] + 1}, json)))
        return updated_students

    return f"Filtern aller Schüler, die bei einer Notenerhöhung von 1 höher als 3.25 sind: {complex_function(json)}"


@app.route("/C1G", methods=['GET'])
def C1G():
    def args_sum_all(*args):
        return sum(args)

    def kwargs_print_info(**kwargs):
        for key, value in kwargs.items():
            return f"{key}: {value}"

    def closure_outer_function(x):
        def closure_inner_function(y):
            return x + y

        return closure_inner_function

    closure_add_ten = closure_outer_function(10)
    closure_add_ten(30)

    kwargs_print_info(name="Thyme", age=18)
    args_sum_all(6, 20, 33, 14)

    return str(args_sum_all(6, 20, 33, 14))


@app.route("/C1F", methods=['GET'])
def C1F():
    def refactored_sum_all(*args):
        return sum(args)

    return f"Die Summe einer Reihe gegebener Zahlen ist: {str(refactored_sum_all(10, 1122, 33, 514, 541, 87))}"


@app.route("/C1E", methods=['GET'])
def C1E():
    def sum_all(x, y, z):
        return x + y + z

    def refactored_sum_all(*args):
        return sum(args)

    return f"Test ob eine Liste Zahlen gleich gross wie eine andere: {str(refactored_sum_all(33, 12, 32)) if refactored_sum_all(32, 12, 32) == sum_all(33, 12, 32) else str('Test failed')}"

    # Gewollte Ausgabe: "Test failed"


if __name__ == "__main__":
    app.run(debug=True)
