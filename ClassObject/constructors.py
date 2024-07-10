class ope:
    def __init__(self, a, b):
        print("constructor is called")
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)


a2 = ope(50, 500)
a2.add()
