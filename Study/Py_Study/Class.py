# coding: utf-8
class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print_score(self):
        print('%s %s'%(self.__name,self.__score))

    def get_grade(self):
        if self.__score>=90:
            return 'A'
        elif self.__score>=60:
            return 'B'
        else:
            return 'C'
bart=Student('Mike',95)
lisa=Student('Jack',65)
lbds=Student('Sone',55)
bart.print_score()
print(bart.get_grade())
print(lisa.get_grade())
print(lbds.get_grade())
bart.__score=90
bart.print_score()