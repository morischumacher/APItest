# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def g(y):
    return f(y)


def f(x):
    if (x < 0):
        d = 0
    if (x == 0):
        d = 1
    if (x > 0):
        d = (f((x-1)) + f((x-1)))
    return d

def divTwo(y):
    count = 0
    while (y > 1):
        y = (y-2)
        count = (count+1)
    return count

def binTwo(x):
    count = 0
    if (x < 0):
        count = (count+1)
        print(0)
    if (x == 0):
        count = (count + 1)
        print(0)
    while(x >= 1):
        if((divTwo((x+1))-divTwo((x-0))) == 1):
            count = (count + 1)
            print(1)
        else:
            count = (count + 1)
            print(0)
        x = divTwo(x)
    return count




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    binTwo(10)
    print("y")
    binTwo(2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


