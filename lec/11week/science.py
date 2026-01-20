from student import Student

class Science(Student):
  def __init__(self, name, math, computer, science):
    super().__init__(name, computer)
    self.sciene = science

  def get_name(self):
    return self.name

  def get_math(self):
    return self.math

  def get_computer(self):
    return self.computer
  
  def get_average(self):
    return (self.math + self.computer)/2
  
s1 = Student('gunrein620',90,85)
print(s1.get_name(),s1.get_average())