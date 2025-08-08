class Que():
  def __init__(self) -> None:
    self.que = []

  def pop(self):
    raise NotImplementedError("This method should be overridden by subclasses")
  
  def push(self, value):
    raise NotImplementedError("This method should be overridden by subclasses")
  
  def __len__(self):
    return len(self.que)
  

class FIFO_Que(Que):
  def push(self, value):
    self.que.append(value)

  def pop(self):
    return self.que.pop(0)
