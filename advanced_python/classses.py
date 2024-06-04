from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return "{}".format(self.__name)

    def introduction(self):
        print("My name is {} and I am {}".format(self.__name, self))

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def travel(self):
        pass


class FlyingAnimal(Animal, ABC):
    def _fly(self):
        print("{} is flying".format(self.name))


class SwimmingAnimal(Animal, ABC):
    def _swim(self):
        print("{} is swimming".format(self.name))


class RunningAnimal(Animal, ABC):
    def _run(self):
        print("{} is running".format(self.name))


class Duck(FlyingAnimal, SwimmingAnimal, RunningAnimal):
    def travel(self):
        return super()._fly(), super()._swim(), super()._run()

    def sound(self):
        print("Quack!")


class PolarBear(SwimmingAnimal, RunningAnimal):
    def travel(self):
        return super()._swim(), super()._run()

    def sound(self):
        print("Roar!")


class FlyingPolarBear(PolarBear, FlyingAnimal):
    def _fly(self):
        super()._fly()
        print("...but with magic!")

    def travel(self):
        return super().travel(), self._fly()


if __name__ == "__main__":
    zoo = []

    d = Duck("Lizzie")
    zoo.append(d)

    p = PolarBear("Bobby")
    zoo.append(p)

    fp = FlyingPolarBear("Well... Flying Bobby")
    zoo.append(fp)

    for pet in zoo:
        pet.introduction()
        pet.sound()
        pet.travel()
