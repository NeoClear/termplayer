class Cache:
  def __init__(self, generator):
    self.cache = {}
    self.generator = generator

  def get(self, k):
    if k not in self.cache:
      self.cache[k] = self.generator(k)
    return self.cache[k]
