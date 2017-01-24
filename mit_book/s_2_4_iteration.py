questions_qty = 10
stop_asking = questions_qty
biggest_odd = 1
while stop_asking != 0:
    n = int(
        input('Tell me number (' + str(questions_qty - stop_asking + 1) + ')'))

    if n % 2 == 0 and biggest_odd < n:
        biggest_odd = n

    stop_asking = stop_asking - 1

if biggest_odd % 2 == 0:
    print(str(biggest_odd))
else:
    print('There is no odd numbers in the 10 numbers you inputed')
