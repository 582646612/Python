import os

def localos():
    # curpath = os.path.realpath(__file__)
    curpath = os.path.dirname(__file__)
    return curpath
def lastos():
    curpath = os.path.dirname(os.path.dirname(__file__))
    return curpath


if __name__ == '__main__':
    print(localos())
    print(lastos())


