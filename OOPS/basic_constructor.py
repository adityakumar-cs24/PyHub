class Student:
    name = "Aditya"
    def __init__(self,fullname,age):
        self.name = fullname
        self.age = age
        print("Happy New Year...")

s1 = Student("Adarsh Kumar",24)
print(s1.name,s1.age)
