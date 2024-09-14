f = open("sample.txt", "r")
data = f.read()

data = data.replace("donkey", "######")

f = open("sample.txt", "w")
f.write(data)
