# class Student:
#     def __init__(self, name, course, level):    # This runs automatically
#         print("Creating a new student...")
#         self.name = name
#         self.course = course
#         self.level = level
#         print(f"Student {name} has been crreated!")

# # When you create a student, __init__ runs automatically
# kemi = Student("Kemi Adebayo", "Computer", 300)
# name = Student("TUnji Paul", "Man U", 8)

# class NigerianStudent:
#     def __init__(self, name, state, course):
#         print(f"Step 1: Creating student object...")
#         self.name = name
#         self.state_of_origin = state
#         self.course = course
#         self.student_id = self.generate_id()
#         print(f"Step 6: {self.name} from {self.state_of_origin} is ready!")

#     def generate_id(self):
#         import random
#         return f"UNISAIL{random.randint(1000, 9999)}"
    
# ayo = NigerianStudent("Ayo Daniel", "Lagos", "Street Statistics")
# print(ayo.name)
# print(ayo.student_id)

class PhoneUser:
    def __init__(self, name, network):
        self.name = name
        self.network = network
        self.airtime = 0
        print(f"{self.name} joined {self.network} network")

    def buy_airtime(self, amount):
        self.airtime += amount  # self ensures it goes to the RIGHT person
        return f"{self.name} now has ₦{self.airtime} airtime"

# Creating multiple users  
abeeb = PhoneUser("Abeeb Bakare", "MTN")
onisemo = PhoneUser("Onisemo Williams", "Airtel")

# Each person's actions affect only their own account
print(abeeb.buy_airtime(500))
print(onisemo.buy_airtime(1000))
print(abeeb.airtime)
print(onisemo.airtime)


# Defining Attributes of a student
class Student:
    def __init__(self, name, course, level, state_of_origin):
        self.name = name
        self.course = course
        self.level = level
        self.state_of_origin = state_of_origin
        self.cgpa = 0.0

# creating a student object
Fathia = Student("Fathia Abdul", "Biochemistry", 300, "Ogun State")

# Accessing attributes
print(Fathia.name)
print(Fathia.course)
print(Fathia.state_of_origin)


# Types of Attributes
#1. Instance Attributes - Unique to each object
student1 = Student("Anthony Johnson", "Engineering", 200, "Ogun")
student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos")

print(student1.name)
print(student2.name)


#2. Class Attribute - Shared by all objects of the class
class Student:
    university =  "Federal University of Technology Akure"

    def __init__(self, name, course):
        self.name = name
        self.course = course

student1 = Student("Lionel Messi", "Football")
student2 = Student("Andrew Tete", "Fraud")
print(Student.university)
print(student1.university)
print(student1.name)
print(student1.course)
print(student2.university)
print(student2.name)
print(student2.course)


# Methods
# Methods are functions that belong to a class. They define what actions an object can perform. They answer the question "What can this object do?
class Student:
    def __init__(self, name, course, level):
        # Attributes
        self.name = name
        self.course = course
        self.level = level
        self.cgpa = 0.0
        self.fees_paid = False


     # Method: action the student can do
    def pay_school_fees(self):
        self.fees_paid = True
        return f"{self.name} has paid school fees for {self.level} level"
    
    # Method: another action
    def register_courses(self):
        if self.fees_paid:
            return f"{self.name} has registered courses for {self.course}"
        else:
            return f"{self.name} must pay school fees first!"
        
    # Method: calculate CGPA
    def calculate_cgpa(self, grades):
        if grades:
            self.cgpa = sum(grades) / len(grades)
            return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
        return "No grades provided"
    
# Using methods
Abiodun = Student("Abiodun Akinola", "Gistology", 600)
print(Abiodun.pay_school_fees())
print(Abiodun.register_courses)