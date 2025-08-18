"""This file is created to show the order of code being executed,
and the importance of the if __name__ == "__main__" statement"""
import import_me

"""Since python is a top to bottom language, the order of execution, and thus the order in which we see the results 
will be as follows: imported files, everything above the if __name__ == __main__" and finally everything below """


def second():
    print("Even thought the function was parsed before the first string, this will be shown second.")


def only_main():
    print("This line will be visible only when this file is the main file, and is not imported.")


this_will_be_first = "In the body of the main file, above the if __name__ statement. Im gonna be shown after imports"
print(this_will_be_first)

second()


if __name__ == "__main__":
    only_main()
