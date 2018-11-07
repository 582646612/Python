'''name = "jack"
city = "Beijing"
print("my name is %s and come form %s"%(name,city))---'''
class  Studet():
    def __init__(self,name,city):
        self.name=name
        self.city=city
        print("My naem is %s and come form %s" %(name,city))
    def talk(self):
        print("Hello Word")
stu1=Studet('Jack',"Beijing")
stu1.talk()
stu1=Studet('Marry',"KunMing")
stu1.talk()
