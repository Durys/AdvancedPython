import math


def find_divisors(n):
    i = 1
    divs = []
    while i <= math.sqrt(n):
        if n % i == 0:
            if n / i == i:
                divs.append(i)
            else:
                divs.extend([i, int(n / i)])
        i = i + 1
    return divs


class ListExercises:
    def __init__(self):
        print("List exercises: ")
        self.exercise_1(self)
        self.exercise_2(self)
        self.exercise_3(self)
        self.exercise_4(self)
        self.exercise_5(self)
        self.exercise_6(self)

    @staticmethod
    def exercise_1(self):
        print("Exercise 1: ")
        l_e = []
        for i in range(10):
            l_e.append(i)
        print(l_e)

    @staticmethod
    def exercise_2(self):
        print("Exercise 2: ")
        l_a = ["a", "b", "c", "d", "e"]
        for i in enumerate(l_a):
            print(i)

    @staticmethod
    def exercise_3(self):
        print("Exercise 3: ")
        l_a = ["a", "b", "c", "d", "e"]
        l_n = [1, 2, 3, 4, 5]
        l_a.extend(l_n)
        print(l_a)

    @staticmethod
    def exercise_4(self):
        print("Exercise 4: ")
        l_a = ["a", "b", "c", "d", "e"]
        l_n = [1, 2, 3, 4, 5]
        l_o_e = []

        for i, j in zip(l_a, l_n):
            l_o_e.append(i)
            l_o_e.append(j)
        print(l_o_e)

    @staticmethod
    def exercise_5(self):
        print("Exercise 5: ")
        l_10 = [x for x in range(10)]
        l_10 = l_10[::-1]
        print(l_10)

    @staticmethod
    def exercise_6(self):
        print("Exercise 6: ")
        l_10 = [x for x in range(10)]
        for i in l_10:
            if i % 2:
                l_10.remove(i)
        print(l_10)


class DictExercises:
    def __init__(self):
        print("Dict exercises: ")
        self.exercise_1(self)
        self.exercise_2(self)
        self.exercise_3(self)
        self.exercise_4(self)
        self.exercise_5(self)

    @staticmethod
    def exercise_1(self):
        print("Exercise 1: ")
        d_e = {}
        l_a = ["a", "b", "c", "d", "e"]
        for i in range(len(l_a)):
            d_e[l_a[i]] = i
        print(d_e)

    @staticmethod
    def exercise_2(self):
        print("Exercise 2: ")
        d_2 = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4}
        for key in d_2:
            print(key)

    @staticmethod
    def exercise_3(self):
        print("Exercise 3: ")
        d_3 = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4}
        for key, value in d_3.items():
            print(key, value)

    @staticmethod
    def exercise_4(self):
        print("Exercise 4: ")
        d_4 = {}
        for i in range(51):
            d_4[i] = []
            divs = find_divisors(i)
            d_4[i] = divs
        print(d_4)

    @staticmethod
    def exercise_5(self):
        print("Exercise 5: ")
        d_5 = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j"}
        d_copy = dict(d_5)
        for key in d_copy:
            if key % 2 != 0:
                del d_5[key]
        print(d_5)


class SetExercises:
    def __init__(self):
        print("Set exercises: ")
        self.exercise_1(self)
        self.exercise_2(self)
        self.exercise_3(self)
        self.exercise_4(self)
        self.exercise_5(self)

    @staticmethod
    def exercise_1(self):
        print("Exercise 1: ")
        l_1 = []
        for i in range(10):
            for j in range(i):
                l_1.append(i)
        s_1 = set(l_1)
        print(s_1)

    @staticmethod
    def exercise_2(self):
        print("Exercise 2: ")
        s_2_1 = {1, 2, 3, 4, 5}
        s_2_2 = {3, 4, 5, 6, 7}
        print(s_2_2.intersection(s_2_1))

    @staticmethod
    def exercise_3(self):
        print("Exercise 3: ")
        s_2_1 = set(range(1, 6))
        s_2_2 = {3, 4, 5, 6, 7}
        print(s_2_1.difference(s_2_2))

    @staticmethod
    def exercise_4(self):
        print("Exercise 4: ")
        s_2_1 = set(range(1, 6))
        s_2_2 = {3, 4, 5, 6, 7}
        to_remove = s_2_2.intersection(s_2_1)
        print("This should be removed: ", to_remove)
        for i in to_remove:
            s_2_2.remove(i)
        print(s_2_2)

    @staticmethod
    def exercise_5(self):
        print("Exercise 5: ")
        s_2_1 = set(range(1, 6))
        s_2_2 = {3, 4, 5, 6, 7}
        print(s_2_2.union(s_2_1))


if __name__ == "__main__":
    list_exercises = ListExercises()
    dict_exercises = DictExercises()
    set_exercises = SetExercises()
