def lazy_sum(x):
 if x<15000:
    print('3')
 elif x<50000 and x>=15000:
    print('6')
 elif x<150000 and x>=50000:
    print('9')
 elif x<500000 and x>=150000:
    print('11')
 elif x<1500000 and x>=500000:
    print('13')
 elif x < 3000000 and x >= 1500000:
    print('15')
 else:
    print('20')
if __name__ == '__main__':
    for num in range(0,10):
     print("次数",num)
     data=float(input())
     lazy_sum(data)
