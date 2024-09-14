f = open("timepass.txt", "r")
data = f.read()
if "twinkle" in data:
    print("Twinkle is present")
else:
    print("Twinkle is absent")
f.close