class Kotowate:
    _list_of_animals = ["Lew", "Tygrys", "Koteczek"]

    def list_animals(self):
        return Kotowate._list_of_animals


class Psowate:
    _list_of_animals = ["Pies", "Kojot", "Wilk"]

    def list_animals(self):
        return Psowate._list_of_animals


class Szopowate:
    _list_of_animals = ["Szop", "Szopik", "Ostronos"]

    def list_animals(self):
        return Szopowate._list_of_animals


def task_1():
    ps = Psowate()
    list_2 = ps.list_animals()
    print(list_2)
    kt = Kotowate()
    list1 = kt.list_animals()
    print(list1)
    sz = Szopowate()
    list_3 = sz.list_animals()
    print(list_3)


def task_2():

    def factory(family):

        families = {"Kotowate": Kotowate(), "Szopowate": Szopowate(), "Psowate": Psowate()}

        return families[family]

    for i in ["Psowate", "Kotowate", "Szopowate"]:
        print(factory(i))


if __name__ == '__main__':
    task_1()
    task_2()
