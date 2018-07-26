from hashlib import sha256
x = 1434346
y = 0
count = 0
while count != 10:
    while sha256(f'{x}{y}'.encode()).hexdigest()[:5] != "00000":
        y += 1
    print(f'The solution is y = {y}')
    x = y
    y = 0
    count +=1