#week 3 Homework kurtis Henry

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
  
  


class Student(Person): 
  def __init__(self, fname, lname, year,studentID):
    super().__init__(fname, lname)
    self.graduationyear = year
    self.ID = studentID
    

  def welcome(self): #welcome message 
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
    if (self.graduationyear == 2020):
         print("welcome senior")
  
  def years_to_go(self): #years to go
      years = self.graduationyear - 2020
      print("you have", years," years to go!!!")
  
  def locker(self): #id locker/detremination
      if (self.ID < 1000):
          print ("please report to the office for locker assignment")
      
        
  
class Teacher (Person): #new attributes
  def __init__(self, fname, lname, experience, salary):
    super().__init__(fname, lname)
    self.YearsOfExperience = experience
    self.pay = salary
  
  def printname(self): #print names
    print(self.firstname, self.lastname)
    

  def level (self): #veteran status
       if (self.YearsOfExperience <= 5):
           print("welcome young professor")
       else:
           print("welcome back veteran scholar")
  
  def compensation (self): #compensation calculation 
      raises = self.pay * .15
      salaryincrease = self.pay + raises
      print ("Once this school year is complete, you salary will increase to: $" + str(salaryincrease))
      

class Admin (Person): #admin selections
    def __init__(self, fname, lname, position, team):
        super().__init__(fname, lname)
        self.position = position
        self.teams = team
        
    def location(self): #print what job based on clerical or not
        if ( self.position == "clerical"):
            print ("you will work with students to recieve lockers")
        else:
            print("we look forward to you helping out professors")
    
    def work_time(self): #afternoon worker is b is selected
        
        if (self.teams == "b"):
            print("you will work from 12 to 4")
        else:
            print("you will work 8 to 12")
 #test   
def main():
    x=Student("Kurtis","Henry",2020, 998)
    x.welcome()
    x.years_to_go()
    x.locker()
    
    print()
    print()
    print()
    
    y = Teacher ("Heather" ,"Bradley", 6, 55000)
    y.printname()
    y.level()
    y.compensation()
    
    print()
    print()
    print()
    
    x = Admin ("Steve" ,"Bell", "clerical", "b")
    x.printname()
    x.location()
    x.work_time()
    
    
    
    
main()
    
    
  
  