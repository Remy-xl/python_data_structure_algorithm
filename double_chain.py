class Node(object):
    def __init__(self,val):
        self.data = val
        self.next = None
        self.prev = None
class LinkList(object):
    def __init__(self):
        self.head = 0
    def initlist(self,data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            node.prev = p
            p = p.next
    def append(self,data):
        q = Node(data)
        p = self.head
        while p:
            p = p.next
        p.next = q
        q.prev = p
    def showlist(self):
        array=[]
        p = self.head
        while p:
            array.append(p.data)
            p = p.next
        return array

l = LinkList()
l.initlist([1,2,3,4,5])
print l.showlist()
