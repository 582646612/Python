import random
def Dlt():
    list1 = []
    for i in range(1, 36):
        list1.append(i)
    list2 = []
    for i in range(1, 13):
        list2.append(i)
    x = random.sample(list1, 5)
    y = random.sample(list2, 2)
    return sorted(x) + sorted(y)

def Ssq():
    list1 = []
    for i in range(1, 34):
        list1.append(i)
    list2 = []
    for i in range(1, 17):
        list2.append(i)
    x = random.sample(list1, 6)
    y = random.sample(list2, 1)
    return sorted(x) + sorted(y)

def Exchange(x):
    return str(x).zfill(2)

if __name__ == '__main__':
    for x in range(0, 2):
        num = Dlt()
        print(Exchange(num[0]), Exchange(num[1]), Exchange(num[2]), Exchange(num[3]), Exchange(num[4]), ' ',
              Exchange(num[5]), Exchange(num[6]))
    print("")
    for x in range(0, 2):
        num = Ssq()
        print(Exchange(num[0]), Exchange(num[1]), Exchange(num[2]), Exchange(num[3]), Exchange(num[4]),
              Exchange(num[5]), ' ', Exchange(num[6]))