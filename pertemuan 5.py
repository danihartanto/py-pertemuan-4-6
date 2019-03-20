class BilanganKompleks:
    def __init__(self,a,b):
        self.real=a
        self.im=b
    def __str__(self,a):
        return str(self.real)+"+"+str(self.im)+"i"
    def display(self):
        temp=(self.real),"+",(self.im),"i"
        return temp
data=BilanganKompleks(4,6)

print(data.display) #kalo manggil make atribut


#type(data)
