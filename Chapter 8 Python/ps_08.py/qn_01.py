# def largest(n1,n2,n3):
#     if(n1>n2):
#         if(n1>n3):
#             return n1
#         else:
#             return n3
#     else: 
#         if(n2>n3):
#             return n2
#         else:
#             return n3
        
# l  = largest(22,33,44)
# print(l)

def largest(n1,n2,n3):
    if(n1>n2 and n1>n3):
        return n1
    elif(n2>n3 and n2>n1):
        return n2
    else:
        return n3
l  = largest(22,33,44)
print(l)
