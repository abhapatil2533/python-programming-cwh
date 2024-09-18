class person:
    country="India"
    def takebreak(self):
        print("i am breathing")

class Employee:
    company = "honda"

    def getsalary(self):
        print(f"salary is{self.salary}")

    def takebreath(self):
        print("I am an employee so im luckily breathing")
    

def Programmer(Employee):
    company = "Fiverr"

    def gersalary(self):
        print(f"No salary to programmers")

    def takebreath(self):
        print("I am an programmer so im breanthing ++")

p = person()
p.takebreak()
e = Employee()
e.takebreath()
pr = Programmer()
pr.takebreath()

    