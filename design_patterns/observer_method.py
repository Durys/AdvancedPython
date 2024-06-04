class Subject:
    subscribers = []

    def notify(self):
        print("Updates were made.")

    def attach(self, sub):
        if sub not in Subject.subscribers:
            Subject.subscribers.append(sub)
        else:
            print("This person has already subscribed.")

    def detach(self, sub):
        if sub in Subject.subscribers:
            Subject.subscribers.append(sub)
        else:
            print("This person didn't yet subscribe.")


class Data(Subject):
    def __init__(self, name, data):
        self.name = name
        self._data = data

    @property
    def data(self):
        return self._data

    def setter(self, set):
        self._data = set
        Data.notify(self)


class HexViever():
    def update(self, Data):
        print(Data.name, hex(Data.data))


class OctalViever():
    def update(self, Data):
        print(Data.name, oct(Data.data))


class DecimalViever():
    def update(self, Data):
        print(Data.name, float(Data.data))


if __name__ == "__main__":
    data1 = Data("Film1", 2)
    data2 = Data("Film2", 4)

    hexa = HexViever()
    octa = OctalViever()
    deci = DecimalViever()

    hexa.update(data1)
    hexa.update(data2)
    octa.update(data1)
    octa.update(data2)
    deci.update(data1)
    deci.update(data2)

    data1.setter(4)
    data2.setter(8)

    hexa.update(data1)
    hexa.update(data2)
    octa.update(data1)
    octa.update(data2)
    deci.update(data1)
    deci.update(data2)
