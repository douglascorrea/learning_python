x = 501
y = 100000
z = 10000001

if z % 2 != 0 and y % 2 != 0 and x % 2 != 0:
    print("No numbers are odd")
else:
    if (x > y) or (y % 2 != 0):
        if x > z or (z % 2 != 0):
            if x % 2 == 0:
                print("The largest odd number is ", x)
    if (y > x) or (x % 2 != 0):
        if y > z or (z % 2 != 0):
            if y % 2 == 0:
                print("The largest odd number is ", y)
    if (z > x) or (x % 2 != 0):
        if z > y or (y % 2 != 0):
            if z % 2 == 0:
                print("The largest odd number is ", z)
