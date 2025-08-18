class Singleton:
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance is not None:
            return Singleton.__instance
        else:
            raise Exception("A Singleton object cannot be created twice.")

    def __init__(self):
        if Singleton.__instance is None:
            Singleton.__instance = self


singleton1 = Singleton().get_instance()
print(singleton1)
singleton2 = Singleton().get_instance()
print(singleton2)

print(singleton1 is singleton2)
