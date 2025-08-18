d = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j"}


if __name__ == "__main__":
    for i in range(0, 21):
        try:
            print(d[i])
        except KeyError as ke:
            print("Invalid Key!")
