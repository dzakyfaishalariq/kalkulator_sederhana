class hitung:
    # fungsi hitung a = bilangan utama, b = bilangan kedua, opr = oprasi yang di pakai
    def __init__(self,a,b,opr):
        self.a = a
        self.b = b
        self.opr = opr
    def tambah(self):
        return self.a + self.b
    def kurang(self):
        return self.a - self.b
    def bagi(self):
        return self.a / self.b