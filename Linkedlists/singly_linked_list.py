class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data): #O(1)
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def insert_at_end(self, data): #O(N)
        if self.head is None:
            self.head = Node(data,None)
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        node = Node(data)
        temp.next = node
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def get_length(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def remove_at_index(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        temp = self.head
        while temp:
            if count == index - 1:
                temp.next = temp.next.next
                break
            temp = temp.next 
            count += 1
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        temp = self.head
        
        while temp:
            if count == index - 1:
                node = Node(data, temp.next)
                temp.next = node
                break
            temp = temp.next
    def print_list(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp:
                print("{} ".format(temp.data),end='')
                temp = temp.next

if __name__ == '__main__':
    obj = LinkedList()
    obj.insert_at_beginning(10)
    obj.insert_at_beginning(20)
    obj.insert_at_beginning(30)
    obj.insert_at_beginning(40)
    obj.insert_at_end(50)
    obj.insert_at_end(60)
    obj.insert_values(["mango", "apple", "grapes", "oranges"])
    obj.print_list()
    print(obj.get_length())
    obj.remove_at_index(2)
    obj.print_list()
    print()
    obj.insert_at(1,"papaya")
    obj.print_list()