#  Base Class A
class A:
    def __init__(self):
        self.value = 10            # shared state 

    def foo(self):
        return "foo()implemented"


# Derived Class B
class B:
    def __init__(self, a):
        self.a = a                 # shared A instance

    def foo(self):
        return f"B implementation, value = {self.a.value}"


# Derived Class C
class C:
    def __init__(self, a):
        self.a = a                 # same shared A instance

    def foo(self):
        return f"C implementation, value = {self.a.value}"

# Final Derived Class D
class D(A):
    def __init__(self):
        A.__init__(self)           # create ONE A object
        self.b = B(self)           # pass same A to B
        self.c = C(self)           # pass same A to C

    # Resolve ambiguity and override foo()
    def foo(self):
        b_result = self.b.foo()
        c_result = self.c.foo()
        return f"D resolves -> [{b_result}] & [{c_result}]"


# Runtime Polymorphism
def call_foo(obj):
    print(obj.foo())
d = D()
call_foo(d)
