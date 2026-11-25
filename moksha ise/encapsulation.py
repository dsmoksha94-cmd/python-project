class Demo:
a=10
b=20
    self.c = c
    self.d = d
def display(self):
  print(self.c,self.d)
def ch_c(self,new):
  self.c = new
@classmethod
def disp(cls):
  print(cls.a,cls.b)
@staticmethod
def msg():
  print("Public Access Specifers")
 user=Demo(10,20)
 user.display()
 user.ch_c(30)
 user.dispalay()