# Bai 2
#A
def vy(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

so = 2
while so < 100:
    if vy(so):
        print(so, end=' ')
    so += 1


#B
aimer = 1
while aimer < 100:
    if (aimer ** 0.5).is_integer():
        print(aimer, end=' ')
    aimer += 1


#C
x, y = 0, 1
while x < 1000:
    print(x, end=' ')
    x, y = y, x + y