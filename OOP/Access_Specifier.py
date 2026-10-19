# public: Accessible from anywhere
class test:
    a=10
t=test()            # Public
print(t.a)

# Protected: Accesible for class and sub class
class test:
    _a=10
t=test()            # Protected 
print(t._a)

# Private: Accessible only for class where it is define 
class test:
    __a=20
t=test()            # Private
print(t.__a)
