class BilKompleks:
    def __init__(self,a,b):
        self.real=a
        self.im=b
    def display(self):
        temp=(self.real),"+",(self.im),"i"
        return temp
    def addData(self,jumlah1,jumlah2):
        self.real=jumlah1.real+jumlah2.real
        self.im=jumlah1.im+jumlah2.im

    def jumlah1(self,jumlah):
        self.real=self.real+jumlah.real
        self.im=self.im+jumlah.im
    def __str__(self):
        return str(self.real)+"+"+str(self.im)+"i"
    
    def addKompleks(self,obj):
        a=self.real+obj.real
        b=self.im+obj.im
        return BilKompleks(a,b)
    #def __add__(self):
        #teruskan sendiri
data1=BilKompleks(4,9) #pendifinisian data kembali di sebut override
data2=BilKompleks(23,10)
#print(data2.display())
#data3=BilKompleks(data,data2)
print(data1)
#print(data2)
#data3=BilKompleks.addData(data1,data2)
#print(data3)

jumlah2=data1.addKompleks(data2)
print(jumlah2)
