words = ["abha", "Ojas", "mumma", "donkey"]
f = open("sample.txt", "r")
data = f.read()

for word in words:
    data = data.replace(word, "######")

f = open("sample.txt", "w")
f.write(data)