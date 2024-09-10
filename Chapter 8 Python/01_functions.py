def percent(marks):
    return ((marks[0] + marks[1] + marks[2] + marks[3]))/400*(100)


marks = [78,88,98,89]
percentage = percent(marks)
print(percentage)



def greet(name="stranger"):
    return (print(name + ", Good day!"))

#name = str(input("Enter your name: "))
#greeting= greet(name)

greet("harry")
greet()