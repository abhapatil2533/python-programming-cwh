class Employee:
    company="Microsoft"

    def __init__(self,name,product):
        self.name=name
        self.product=product

    def getinfo(self):
        print(f"the name if the programmer is {self.name} and the product is {self.product}")

abha = Employee("abha","toast")
rani = Employee("rani","butter")
abha.getinfo()


