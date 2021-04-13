class Node:
    
    # tao linked list
    def __init__(self, val):
        self.data = val
        self.next = None
        
    #in ra linked list
    def prinList(self):
        cur = self.next
        print(self.data)
        while cur != None:
            print(cur.data)
            cur = cur.next
    
    #them node vao dau linked list
    def appendHead(self, head):
        self.next = head
        head = self
    #them node vao cuoi linked list
    def appendTail(self,head):
        while head.next != None:
            head = head.next
        head.next = self
    
    #them node vao giua hai node
    def appendCenter(self,head,index):
        temp = 0
        while temp != index:
            head = head.next
            temp = temp + 1
        head.next = self
        self.next = head.next.next
          
    #xoa node o dau linked list
    def delHeadNode(self):
        self = None
        self= self.next
    
    #xoa node o cuoi linked list
    def delTailNode(self):
        while self.next.next != None:
            self = self.next
        self.next = None
    
    #xoa node o giua linked list theo vi tri
    def delCenterNode(self,index):
        temp = 0
        while temp != index - 1:
            self = self.next
            temp = temp + 1
        self.next = self.next.next
        
    #xoa node o giua theo data
    def delCenterNodeByData(self,data):
        if self.data == data:
            self = None
            self = self.next
        while self.next.data != data:
            self = self.next
        self.next = self.next.next
            
    #tim kiem 1 node theo du lieu
    def searchNode(self,head):
        cur = head
        if (self.data == head.data):
            print("found")
        else:
            while cur.next != None:
                if(self.data == cur.data):
                    print("found")
                else: cur = cur.next
        if (cur.next == head.endNode.next):
            print("Not Found!!!")
            
    def endNode(self):
        while(self.next != None):
            self = self.next
        return self

    def sumUp(self):
        total=0
        while (self.next != None):
            total = total + self.data
            self = self.next
        if self.next == None :
            total = total + self.data
        return total

data = [2, 3, 5, 7, 11, 13]
head = Node(2)
a = 0
for i in range(1,len(data)) :
    newNode = Node(data[i])
    head.endNode().next = newNode
head.prinList()
a = head.sumUp()
print(a)
