# --------------------------------------------------------------------
# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# -----------------------------------------------------------

class Member:
  
  mot_allowed_names = {"Hell","shit","bad"}
  
  def __init__(self, first_name, middle_name, last_name, gender):
    self.fname = first_name
    self.mname = middle_name
    self.lname = last_name
    self.mygender = gender  
    
  def full_name(self):
    if self.fname in Member.mot_allowed_names:
      raise ValueError("This Name Is Not Allowed")
    else:
      return f"{self.fname} {self.mname} {self.lname}"
  
  
  def name_with_title(self):
    if self.mygender == "Male":
      return f"Hello Mr {self.fname} "
    elif self.mygender == "Female":
      return f"Hello Miss {self.fname} "
    else:
      return f"Hello {self.fname} "
    
  def get_all_info(self):
    return f"{self.name_with_title()} Your Full Name Is {self.full_name()}"
  
member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
member_three = Member("Mona", "Ali", "Mahmoud", "Female")
member_four = Member("noor", "Ali", "Mahmoud", "Unknown")

print (member_two.full_name())

print (member_three.name_with_title())

print (member_four.name_with_title())

print (member_one.get_all_info())
# print(dir(member_one))

# print(member_one.fname, member_one.mname, member_one.lname)
# print(member_two.fname)
# print(member_three.fname)

