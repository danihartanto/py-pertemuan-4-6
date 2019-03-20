class BilKompleks:
    def __init__(self,a,b):
        self.real=a
        self.im=b
    def display(self):
        print(self.real,"+",self.im,"y")
    def __str__(self):
        return str(self.real)+"+"+str(self.im)+"i"
data=(BilKompleks(4,9))
print(data.display())
