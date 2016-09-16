class Stack(object):
    def __init__(self):
        self.stack=[]
    def push(self,obj):
        self.stack.append(obj)
    def pop(self):
        return self.stack.pop()
    def show(self):
        print(self.stack)
if __name__ == '__main__':
    s=Stack()
    array = [1,2,3,4,5]
    for i in array:
        s.push(i)
    s.show()
    s.pop()
    s.show()
