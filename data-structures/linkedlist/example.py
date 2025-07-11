class Node:
  # método construtor em python:
  # é chamado de __init__, self é o objeto que está sendo criado
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList: 
  def __init__(self):
    self.head = None
    self.tail = None
  
  def add_to_front(self, value):
    new_node = Node(value)
    new_node.next = self.head
    if self.head:
      self.head.prev = new_node
    else:
      self.tail = new_node
    self.head = new_node
    
    
  def add_to_end(self, value):
    new_node = Node(value)
    new_node.next = self.head
    if self.head:
      self.head.prev = new_node
    else:
      self.tail = new_node
    self.head = new_node
    
    
  def remove_from_front(self, value):
    pass
  def remove_from_end(self, value):
    pass