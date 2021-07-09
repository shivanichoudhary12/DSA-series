class Node(object):
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False

class BreadthFirstSearch(object):

    def bfs(self,startNode):
        queue = []
        queue.append(startNode)
        startNode.visited = True

        while queue:
            actual_node = queue.pop(0)
            print(actual_node.name)
            for i in actual_node.adjacency_list:
                if not i.visited:
                    i.visited =True
                    queue.append(i)




node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')
node6 = Node('F')
node7 = Node('G')
node8 = Node('H')

node1.adjacency_list.append(node2)
node1.adjacency_list.append(node6)
node1.adjacency_list.append(node7)
node2.adjacency_list.append(node3)
node2.adjacency_list.append(node4)
node4.adjacency_list.append(node5)
node7.adjacency_list.append(node8)

bfs = BreadthFirstSearch()
bfs.bfs(node1)
