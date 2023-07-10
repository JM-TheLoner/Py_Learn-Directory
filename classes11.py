class A:
    def method(self):
        print(1)

class B(A):
    def method(self):
        print(11)

class C(B):
    def method11(self):
        print(111)

c = C()
c.method()
c.method()
c.method11()