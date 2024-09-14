f = open("hiscore.txt", "r")
data = f.read()
data = int(data)
f.close
score = int(input("Enter the score: "))
print(type(data))
print(type(score))

if data<score:
    score = str(score)
    f = open("hiscore.txt", "w")
    f.write(score)
    f.close()