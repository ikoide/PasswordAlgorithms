class Password():
  def __init__(self, passType, content):
    self.passType = passType
    self.content = content
    self.time = 0.0
    self.cracked = False

  def getLength(self):
    return len(self.content)