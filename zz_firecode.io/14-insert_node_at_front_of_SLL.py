class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
                      
    # Method for inserting a new node at the start of a Linked List   
    def insert_at_front(self,data):
        
        new_head = Node()
        new_head.data = data
        new_head.next = self.head
        self.head = new_head