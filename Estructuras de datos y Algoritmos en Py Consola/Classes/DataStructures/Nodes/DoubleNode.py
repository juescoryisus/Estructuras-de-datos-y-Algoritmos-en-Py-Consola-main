from Classes.DataStructures.Nodes.Node import Node


class DoubleNode(Node):
    def __init__(self, data):
        Node.__init__(self, data)
        self.back = None
