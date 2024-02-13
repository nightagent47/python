class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def onyesha(self):
        print(f"My name is {self.name} and I am {self.age} years.")
p1=Person("Isaac",17)
p2=Person("Dalmas",16)
p3=Person("Abdi",15)
p4=Person("Julie",17)
p5=Person("Becky",18)

p1.onyesha()
p2.onyesha()
p3.onyesha()
p4.onyesha()
p5.onyesha()
