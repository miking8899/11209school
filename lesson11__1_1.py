class Person:
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height=height
    #method

    def bsmi(self)->float:
        return self.weight/(self.height/100)**2


    def __str__(self)->str:
        return f"name={self.name}\nweight={self.weight}\n height={self.height}"
    
    def __name__ == '__main__':
        p1=Person("小南",89,180)
        print(p1)
        print(p1.bsmi())
    
p2=Person()
