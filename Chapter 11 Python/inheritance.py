class employee:
    company  = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(employee):
    language = "Python"
    company = "Youtube"
    def getLanguage (self):
        print(f"The language is {self.language}") 

    def showDetails(self):
        print(f"This is a programmer") 

e = employee()
e.showDetails()
p = Programmer()
p.showDetails;()
print(p.company)