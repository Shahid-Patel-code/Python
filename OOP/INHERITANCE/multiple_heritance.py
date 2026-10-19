class parent1:
    pass
class parent2:
    pass
class child(parent1,parent2):
    pass

c=child()

class A: 
    def __init__(self):
        print("A")
class B:
    def __init__(self):
        print("B")
class C(A,B):
    def __init__(self):
        B.__init__(self)
        super().__init__()
        print("C")
c=C()
c.show()
print(C.mro())

