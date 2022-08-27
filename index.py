class Empty(Exception):
  pass


class ArrayQueue:

  def __init__(self):
    self._data = [] # this is a private array 
    self._size = 0
    self._front = 0

  #return the len of the queue
  def __len__(self):
    return self._size
  
  #checks if the queue is empty
  def is_empty(self):
    return self._size == 0


  #this shows the first element in the queue
  def first(self):
    if self.is_empty():
      raise Empty('The queue is empty')
    return self._data[self._front]
  
  #removes the  first element of the queue
  def dequeue(self):
    if self.is_empty():
      raise Empty(' the queue has no element')
    answer = self._data[self._front]
    self._data[self._front] = None
      
    
