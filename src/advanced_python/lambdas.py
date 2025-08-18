def exercise_1():
    for i in range(21):
        b = lambda: print("Even") if i % 2 == 0 else print("Odd")
        b()


def exercise_2():
    a = lambda x, y: print(x, y, x * y)
    for i in range(11):
        for j in range(11):
            a(i, j)


if __name__ == "__main__":
    exercise_1()
    exercise_2()
