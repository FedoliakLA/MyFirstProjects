from math import sqrt
class Eq():
    def __init__(self, a, b, c, d = 0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def Disc(self):
        D = self.b**2 - 4 * self.a * self.c
        self.d = D
        return D
    def X1(self):
        i = 0 - self.b
        e = 2 * self.a
        if self.d < 0:
            return"Коренів немає"
        else:
            p = sqrt(self.d)
            x1 = (i + p) / e
            return x1
    def X2(self):
        i = 0 - self.b
        e = 2 * self.a
        if self.d < 0:
            return"Коренів немає"
        else:
            p = sqrt(self.d)
            x2 = (i - p) / e
            return x2

    def print_info(self):
        print("Дискримінант: ", self.Disc())
        if self.d < 0:
            print(self.X1())
        elif self.d == 0:
            print("Корінь: ", self.X1)
        else:
            print("Перший корінь: ", self.X1())
            print("Другий корінь: ", self.X2())

eq_1 = Eq(3, 10, -30)
eq_1.print_info()