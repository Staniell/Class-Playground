def call_Class(SomeC, f, r):
    SomeC = SomeClass()
    SomeC.pro = "yes"
    return SomeC.pro


class SomeClass:
    def hi():
        print("hello")

b = SomeClass()
a = call_Class(b, 1, 2)

print(a)



