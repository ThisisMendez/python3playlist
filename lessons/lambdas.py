nums = [1,2,3,4,5,6]

# Old Way
def square(n):
     return n*n

lambda n: n*n

print(list(map(square, nums)))

# New Way 
print(list(map(lambda n: n*n, nums)))


#lambadas are in line anonymous functions. It's used if your only going to use a function once. 