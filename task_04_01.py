
fz1 = open('out-1.txt', 'w')
fz2 = open('out-2.txt', 'w')

n = int(input())

with open('data.txt') as f:
    a = f.read()
    for i in a.split():
        b = int(i) % n
        if b == 0:
            fz1.write(i + ' ')
        else:
            continue

p = int(input())

with open('data.txt') as f:
    a = f.read()
    for i in a.split():
        b = int(i) ** p
        fz2.write(str(b) + ' ')


fz1.close()
fz2.close()
