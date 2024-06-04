def is_even(num):
    return num % 2 == 0


def args_kwargs(*args, **kwargs):
    return print(f"Args = {args}, Kwargs = {kwargs}")


# FILTER
lists = [1, 2, 3, 4, 5]
filtered = filter(is_even, lists)

print(*lists)
print(*filtered)

print(lists)
print(filtered)

if __name__ == '__main__':
    # MUTABLE
    lists = [1, 2, 3, 4, 5]
    dicts = {1: 2, 2: 3, 3: 4}
    sets = {1, 2, 3}
    # IMMUTABLE
    strings = "Python"
    ints = 2
    frozensets = frozenset([1, 2, 3])
    tuples = (1, 2, 3)

    # LAMBDA FUNCTIONS
    """A lambda function is an anonymous function (i.e., defined without a name)
   that can take any number of arguments but, unlike normal functions,
   evaluates and returns only one expression."""
    print(lambda x: ints + 1)  # < function <lambda > at 0x00000250CB0A5820 >
    (lambda x, y, z: x + y + z)(3, 8, 1)  # Can have many inputs
    print((lambda x: x if (x > 10) else 10)(5))  # Can support if else statements

    # * UNPACKING
    """Unpacking is returning the items of an iterable. Using two ** returns the keyword arguments e.g. values of a dict."""
    args_kwargs(1, 2, color="red")

    # ITERATORS, GENERATORS AND DECORATORS
    """A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. """


    def decor(func):
        def inner():
            print("Executing a function")
            ret = func()
            return ret

        return inner


    @decor
    def rand():
        x = 1
        return x


    rand()


    # GENERATOR
    def _gen():
        start = 0
        while start <= 0:
            start -= 2
            yield start


    gen = _gen()
    print(next(gen))
    print(next(gen))
    print(next(gen))


    # OBJECT ORIENTED PROGRAMMING
    class Dog:
        # ENCAPSULATION
        _species = "Canis familiaris"

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __str__(self):
            return f"{self.name} is {self.age} years old"

        def speak(self, sound):
            return f"{self.name} says {sound}"

        def is_scottish(self):
            return "Dogs are not scottish"


    psisko = Dog("Psisko", 2)
    print(psisko)
    print(psisko.speak("Hau"))
    print(psisko.age)


    class Terrier(Dog):
        # INHERITANCE
        def speak(self, sound="Woof"):
            return super().speak(sound)

        def is_scottish(self):
            return "Terriers can be scottish"


    afra = Terrier("Afra", 99)
    print(afra)
    print(afra.speak())

    # POLYMORPHISM
    for i in [psisko, afra]:
        print(i.is_scottish())


def funkcja(x):
    try:
        if type(x) is not int():
            y = x + 2
            return x, y

    except Exception as e:
        return e


"""
Task 1 (1 min)
Create a list of integers from 0 up to 100 inclusive.
"""
lst = [i for i in range(0, 101)]
print(lst)

"""
Task 2 (2 min)
Create a list generated from the sequence 0 up to 100 exclusive.
If an element is even, the list will contain its cube.
Otherwise, it will contain its square.


First several entries: [0^3, 1^2, 2^3, 3^2, 4^3, ...]
"""
lst = []
for i in range(0, 100):
    if i % 2 == 0:
        lst.append(i ** 3)
    else:
        lst.append(i ** 2)
print(lst)

"""
Task 3 (2 min)
Create dictionary:
Keys: Integers from 0 to 50 REPRESENTED AS A STRING
Values: Cube of the key (as int)


First entries:
{
   '0': 0,
   '1': 1,
   '2': 8,
   '3': 27,
   ...
}
"""
dct = {}

for i in range(0, 51):
    dct[str(i)] = i ** 3
print(dct)

"""
Task 4 (1 min)
Reverse this string
"""
s = 'abcdef'
rev_s = s[::-1]
print(rev_s)

"""
Task 5 (2 min)
Remove duplicates from L.
Order of the output does not matter.
Return a list.
"""
L = [0, 1, 0, 2, 3, 1, 5]
cleared = set(L)
print(list(cleared))

"""
Task 6 (2 min)


Write an infinite generator yielding negative even numbers
starting from -2
"""


def _gen():
    start = 0
    while start <= 0:
        start -= 2
        yield start


gen = _gen()
print(next(gen))
print(next(gen))
print(next(gen))

subtract_two_generator = (n - 2 for n in range(0, -6, -2))
print(subtract_two_generator)
print(*subtract_two_generator)

"""
Task 7 (5 min)


Write a class Point representing a point on the plane coordinate system.
Each point has 3 fields - x, y, and _d, where x, y are coordinates, and d is distance from P(0,0) in specified geometry.
Constructor should accept 2 kwargs, x and y.
    (This new geometry is form of Euclidean geometry, where distance function is replaced by a new metric
    in which the distance between two points is the sum of squared differences of their Cartesian coordinates)
Points should be comparable - they are equal if d is the same.


p1 = P(1, 1)
p2 = P(-1, 1)
p3 = P(2, 3)
p1 == p2 # True
p1 == p3 # False
"""


class P:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.d = x ** 2 - y ** 2

    def __eq__(self, other):
        if not isinstance(other, P):
            return NotImplemented

        return self.d == other.d


p1 = P(1, 1)
p2 = P(-1, 1)
p3 = P(2, 3)

print(p1 == p2)
print(p2 == p3)

"""
Task 8 (1 min)


The following function takes a lists of integers and returns the first index of -1 if it is in the list,
otherwise it returns None.


Add type annotations to the function.
"""


def bar(lst: list) -> int or None:
    for i, v in enumerate(lst):
        int: i
        int: v
        if v == -1:
            return i
    return None


a = [5, 2, 6, -1, 4, 8]
b = [1, 2, 3, 4]
print(bar(a))
print(bar(b))

"""
Task 9 (2 min)


Write a @timed decorator, which prints the execution time of a function.
"""
import time
from functools import wraps


def timed(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print("The function {} took {} seconds".format(f.__name__, str(end - start)))
        return result

    return wrap


@timed
def foo(x, y):
    time.sleep(1)
    return x + y


res = foo(23363664, 100)

"""
Task 10 (6 min)


Refactor complex_function to complex_function_refactored. Check if all tests passes.
"""


def complex_function(objects, dict):
    list = []
    i = 0
    while i < len(objects):
        x = objects[i]
        i = i + 1
        if not (x == None or x in dict.keys()):
            list.append(x)
    x = set(list)
    return x


a = [1, 2, 3, 4]
a_dict = {1: "a", 2: 2, 3: "c"}

print(complex_function(a, a_dict))


def complex_function_refactored():
    pass


"""
Task 11 (6 min)


Create infinite generator for superincreasing sequence (per Wiki: In mathematics, a sequence of positive real numbers (n1, n2, ...)
is called superincreasing if every element of the sequence is greater than the sum of all previous elements in the sequence.),
where every element in sequence is a composite number, starting with 4
"""


def _gener():
    start = 4
    while start > 0:
        start = 2 * start + 1
        yield start


gener = _gener()
print(next(gener))
print(next(gener))
print(next(gener))

"""
Task 12 (10 min)
Create simulation for dice rolling: 420 d6 dice are rolled,
results of "1", "2" and "3" are then re-rolled and dice with results of 3- (3 or less) are then removed.
In the next step, dice which are left are rolled again.
Results of "1" are re-rolled and dice with results of 4- are removed. How many dice are left? Repeat the simulation 2100 times.
What is the average from all simulations? How to calculate average of this dice rolling without running simulations?
"""
from random import randint


def dice_roll(nr_dice):
    results = [randint(0, 6) for p in range(420)]

    first_draw_less = [i for i in results if i <= 3]
    first_draw_more = [i for i in results if i < 3]
    first_draw_shuffle = [randint(0, 6) for p in range(len(first_draw_less))]
    second_draw = [i for i in first_draw_shuffle if i > 3]

    next_step = first_draw_more + second_draw
    next_step = [randint(0, 6) for p in range(len(next_step))]

    remove_4 = [i for i in next_step if i != 4]
    third_draw_ones = [i for i in remove_4 if i == 1]
    third_draw_others = [i for i in remove_4 if i != 1]
    last_shuffle = [randint(0, 6) for p in range(len(third_draw_ones))]
    result = third_draw_others + last_shuffle

    return len(result)


avg = []
for i in range(0, 2101):
    length = dice_roll(420)
    avg.append(length)

res = sum(avg) / len(avg)
print(res)

"""
Task 13 (6 min)
Per Wiki: A Cunningham chain of the second kind of length n is a sequence of prime numbers (p1, ..., pn) such that p_(i+1) = 2p_(i) - 1 for all 1 ≤ i < n.
A Cunningham chain is called complete if it cannot be further extended (element p_(n+1) is not a prime number).
Write function which will accept prime number and will create complete Cunningham chain of the second kind starting from given prime number
"""


def check_prime(num):
    is_prime = True
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
    else:
        is_prime = False
    return is_prime


def complete_cunningham_chain_second_kind(n):
    chain = [n]
    while True:
        next_in_chain = 2 * chain[-1] - 1
        status = check_prime(next_in_chain)
        if not status:
            break
        else:
            chain.append(next_in_chain)
    return chain


assert complete_cunningham_chain_second_kind(2) == [2, 3, 5]
assert complete_cunningham_chain_second_kind(2131) == [2131, 4261, 8521, 17041]
assert complete_cunningham_chain_second_kind(16651) == [16651, 33301, 66601, 133201, 266401, 532801, 1065601]
