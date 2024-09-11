def sum(n):
    if(n==0 or n==1):
        return 1
    return n + sum(n-1)
k = sum(0)
print(k)

# n = int(input("ENter a number:"))
# def sum(n):
#    if n==0:
#       return 0
#       total = total+ sum(n-1)                  WRONG
#       return total
# s = sum(n)
# print(s)

