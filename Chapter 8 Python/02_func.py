# n = int(input("Enter a number"))
# product = 1
# for i in range(n):
#     product = product*(i+1)
# print(product)


# def fact(n):
#     product = 1 
#     for i in range (n):
#         product = product*(i+1)
#     return product
# f = (fact(4))
# print(f)

def fact_rec(n):
    if(n==0 or n==1):
        return 1
    return n*fact_rec(n-1)
k = fact_rec(5)
print(k)