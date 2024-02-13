class fruits:
    def __init__(self,name,price,color):
        self.name=name
        self.price=price
        self.color=color
    def onyesha(self):
        print(f"My favourite fruit is {self.name}"
              f", it costs Ksh.{self.price}"
              f" and its {self.color} in color.")
myobj=fruits("Apple",250,"red")
myobj2=fruits("grapes",350,"purple")
myobj.onyesha()
myobj2.onyesha()

