n = int(input('Insert a number: '))
max_pwr = 6
pwr = 2
while pwr < max_pwr:
    root = 1
    while root**pwr <= n:
        if root**pwr == n:
            print(root, pwr)
            break
        root = root + 1
    if root**pwr == n:
        break
    pwr = pwr + 1
if root**pwr != n:
    print('There are no perfect root with pwr between 0 and 6')
