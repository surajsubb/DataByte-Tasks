for i in range(1,101):
    op = ""
    if i%3 == 0:
        op += "Fizz"
    if i%5 == 0:
        op += "Buzz"
    
    if op == "":
        op = i
    print(op)