def first():
    second()
    print("I'm the first")

def second():
    third()
    print("I'm the second")


def third():
    fourth()
    print("I'm the third")

def fourth():
    print("I'm the fourth.")

first()