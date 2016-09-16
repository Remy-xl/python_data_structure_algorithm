class Node(object):
    def __init__(self,val):
        self.data = val
        self.next = None

class LinkList(object):
    def __init__(self):
        self.head = 0
    def initlist(self,data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next
    def getlength(self):
        l = 0
        p = self.head
        while p:
            l = l+1
            p = p.next
        return l
    def clear(self):
        self.head = 0
    def insert(self,data,index):
        if index == 0:
            p = self.head
            q = Node(data)
            self.head = q
            q.next = p
        else:
            p = self.head
            j = 0
            while p and j<index:
                post = p
                p = p.next
                j = j+1
            if index == j:
                q = Node(data)
                post.next = q
                q.next = p
    def delete(self,index):
        if index == 0:
            p = self.head
            self.head = p.next
        else:
            p = self.head
            j = 0
            while p and j<index:
                post = p
                p = p.next
                j = j+1
            if index == j:
                post.next = p.next
    def index(self,index):
        p = self.head
        j = 0
        while p and j<index:
            p = p.next
            j = j+1
        return p.data
    def update(self,data,index):
        p = self.head
        j = 0
        while p and j<index:
            p = p.next
            j = j+1
        p.data = data
    def append(self,data):
        q = Node(data)
        p = self.head
        while p:
            post = p
            p = p.next
        post.next = q
    def reverse(self):
        p = self.head
        s = p.next
        while s.next:
            t = s.next
            s.next = p
            p = s
            s = t
        s.next = p
        self.head.next = None
        self.head = s
    def showlist(self):
        array = []
        p = self.head
        while p:
            array.append(p.data)
            p = p.next
        return array

# p -> s -> t
# p <- s -> t
# () <- p -> s -> t

l = LinkList()
l.initlist([1,2,3,4,5])
print l.showlist()
print l.getlength()
print l.index(4)
l.update(4,4)
print l.showlist()
l.append(6)
l.append(7)
print l.showlist()
l.reverse()
print l.showlist()
