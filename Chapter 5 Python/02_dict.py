myDict = {
    "fast": "to move in a quick manner",
    "abha": "a coder",
    "marks": [2,4,6,7],
    "anotherDict" : {"harry" : "player"}
}

'''print(myDict)
updateDict = {
    "lovish": "friend",
    "abha" : "a dancer" 
}
myDict.update(updateDict)
print(myDict)'''

print(myDict.get("abha1")) #doesnt throw an error if key doesnt exist
print(myDict["abha2"])   #throws an error if key doesnt exist