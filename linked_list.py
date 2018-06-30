class node:
    def __init__(self, data, isRoot=False):
        self.data = data
        self.isRoot = isRoot
        self.nextNode = None
        if self.isRoot:
            self.rear = self

    def addNode(self, node):
        self.rear.nextNode = node
        self.rear = node

    def traversalPrint(self):

        node = self
        while True:
            if node.nextNode is None:
                print("[{}]-->None".format(node.data))
                break
            else:
                print("[{}]-->".format(node.data), end="")
                node = node.nextNode

if __name__ == "__main__":
    x = node(2, True)
    for i in range(10):
        x.addNode(node(i))
    x.traversalPrint()
