# Base Clas
class A:
    def __init__(self):
        print("implementing A")  

    def foo(self):
        pass

# Derived Class B
class B:
    def __init__(self,b):
        print("implementing B")  
        self.b =b
    def foo(self):
        return "Implement B"


# Derived Class C
class C:
    def __init__(self,c):
        print("implementing C")  
        self.c =c
    def foo(self):
        return "Implement C"


#Final Derived Class D 
class D(B,C):
    def __init__(self):
        A.__init__(self)       
        self.b = B(self)
        self.c = C(self)

    # Override foo() and resolve ambiguity
    def foo(self):
        b_result = self.b.foo()
        c_result = self.c.foo()
        return f"D is implemetion of {b_result} & {c_result}"


#Runtime Polymorphism 
def call_foo(obj):
    print(obj.foo())
d = D()
call_foo(d) 
