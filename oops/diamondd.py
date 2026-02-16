class A:
    def show(self):
        print("class A")

class B(A):
    print("class B")

class C(A):
    print("class c")

class D(B,C):
    print("class D")

d = D()
d.show()
print(D.mro())