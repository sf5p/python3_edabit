class Name:
  def __init__(self,fname,lname):
    self.fname = fname
    self.lname = lname
    
  @property
  def fullname(self):
    return "{} {}".format(self.fname, self.lname)

  @property
  def initials(self):
    fi = self.fname[:1]
    li = self.lname[:1]
    return "{}.{}".format(fi, li)


no = Name("Bob", "Jones")
print(no.fullname)
print(no.initials)

no.fname = "Harry"
print(no.fullname)
print(no.initials)
