class Node:
    def __init__(self,init_data):
        self.data = init_data
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, new_next):
        self.next = new_next
class Linked_List:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        return self.head == None
    def add(self,item):
        Temp=Node(item)
        Temp.setNext(self.head)
        self.head=Temp
    def size(self):
        Current=self.head
        Count = 0
        while Current != None:
            Count = Count+1
            Current = Current.getNext()
        return Count
    def search(self,item):
        current=self.head
        found=False
        while current != None and not found:
            if current.getData()==item:
                found=True
            else:
                current=current.getNext()
        return found

    #def search(self,item):
        
    
#contoh gunakan Node
#a=Node(93)
#b=Node(20
#print(a.getData())
#print(a.getNext())
#print(b.getData())

#myList=Linked_List()
#myList.add(23)
#print(myList.head.data)
#myList.add(34)
#print(myList.head)#ini membuat mylist baru yang di tunjuk oleh Temp
#print(myList.head.data)

mylist=Linked_List()
myList1=Linked_List()
mylist.add(12)
mylist.add(23)
mylist.add(34)
print(mylist.size())
print(mylist.head.data)
print(mylist.search(23))
print(mylist.search(34))

#pr tampilkan posisi node
