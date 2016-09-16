class Queue(object):
    def __init__(self):
        self.queue = []
    def add(self,obj):
        self.queue.append(obj)
    def delete(self):
        self.queue.pop(0)
    def show(self):
        print(self.queue)

if __name__ == '__main__':
    q = Queue()
    array = [1,2,3,4,5]
    for i in array:
        q.add(i)
    q.show()
    q.delete()
    q.show()
