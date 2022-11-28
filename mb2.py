a = 20
b = 10



s = 0
for i in range(a):
    #This line will raise ZeroDivisionError
    s += a/b
    b -= 1