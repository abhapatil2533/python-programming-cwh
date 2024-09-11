def new(string,word):
    newstr = string.replace(word," ")
    return newstr.strip()

st="       ojas doesn't share money      "
n=new(st,"ojas")
print(n)