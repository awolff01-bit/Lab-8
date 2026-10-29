def rational(n,d):
  def select(name):
    if name=="n":
      return n
    elif name=="d":
      return d
  return select
  
def numerator(x):
  return x("n")

def denominator(x):
  return x("d")
