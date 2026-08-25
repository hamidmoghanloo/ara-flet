class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def divide(self):
        return self.a / self.b

    def multiply(self):
        return self.a * self.b

myclass = Calculator(a=1, b=2)
myclass_2 = Calculator(a=10, b=20)

print(myclass.divide())
print(myclass.multiply())
print(myclass_2.divide())
print(myclass_2.multiply())