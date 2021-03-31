from node import Node


class LinkedList:
    def __init__(self):
        self.head = None


    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        temporary_node = self.head

        while temporary_node.next is not None:
            temporary_node = temporary_node.next

        temporary_node.next = node

    def add_to_beginning(self, data_inserted_in_beginning):
        data_inserted = Node(data_inserted_in_beginning)
        data_inserted.next = self.head
        self.head = data_inserted

    def contain_node(self, data):
        temporary_node = self.head

        while temporary_node.data is not data:
            temporary_node = temporary_node.next

        if temporary_node.data == data:
            return True
        else:
            return False


















