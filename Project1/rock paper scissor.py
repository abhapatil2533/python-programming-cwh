def game(x,y):
    if x=="rock" and y=="paper":
        return y
    elif x=="rock" and y=="scissors":
        return x
    elif x=="paper" and y=="scissors":
        return y
    elif x=="paper" and y=="rock":
        return x
    elif x=="scissors" and y=="paper":
        return x
    elif x=="scissors" and y=="rock":
        return y
    elif x=="rock" and y=="rock":
        return None
    elif x=="scissors" and y=="scissors":
        return None
    elif x=="paper" and y=="paper":
        return None
    
x = str(input("p1 enters rock paper scissor"))
y = str(input("p2 enters rock paper scissor"))
result = game(x,y)
print(result)